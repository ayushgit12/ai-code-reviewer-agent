import subprocess
from pathlib import Path


def is_github_url(path: str) -> bool:
    return path.startswith("https://github.com")


def clone_repo(repo_url: str, repos_base_dir: Path) -> Path:
    """
    Clone a GitHub repo locally and return its path.
    """
    repos_base_dir.mkdir(parents=True, exist_ok=True)

    repo_name = repo_url.rstrip("/").split("/")[-1]
    clone_path = repos_base_dir / repo_name

    if clone_path.exists():
        print(f"[INFO] Repo already exists at {clone_path}")
        return clone_path

    print(f"[INFO] Cloning repository: {repo_url}")
    subprocess.run(
        ["git", "clone", repo_url, str(clone_path)],
        check=True
    )

    return clone_path
