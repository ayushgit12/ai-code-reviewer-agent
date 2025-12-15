from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from agent.config import SUPPORTED_EXTENSIONS, EXCLUDED_DIRS
from agent.main import index_codebase
from pathlib import Path
import time
from agent.utils.git_utils import is_github_url, clone_repo



class CodebaseChangeHandler(FileSystemEventHandler):
    def __init__(self, root_path):
        self.root_path = root_path

    def on_modified(self, event):
        if event.is_directory:
            return

        path = Path(event.src_path)

        if any(part in EXCLUDED_DIRS for part in path.parts):
            return

        if path.suffix not in SUPPORTED_EXTENSIONS:
            return

        print(f"[AGENT] Detected change in {path}")
        print("[AGENT] Re-indexing codebase...")
        index_codebase(self.root_path)


def start_watcher(root_path: str):

    if is_github_url(root_path):
        repos_dir = Path("data/repos")
        root_path = clone_repo(root_path, repos_dir)


    event_handler = CodebaseChangeHandler(root_path)
    observer = Observer()
    observer.schedule(event_handler, root_path, recursive=True)
    observer.start()

    print(f"[AGENT] Watching codebase: {root_path}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
