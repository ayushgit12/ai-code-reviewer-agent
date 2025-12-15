import argparse
from agent.main import index_codebase, query_codebase
from agent.agents.watcher import start_watcher 

def main():
     parser = argparse.ArgumentParser(
          description="Autonomous Codebase Intelligence Agent"
     )

     subparsers = parser.add_subparsers(dest="command")

     # index command
     index_parser = subparsers.add_parser("index", help="Index a codebase")
     index_parser.add_argument("path", help="Path to codebase")

     # query command
     query_parser = subparsers.add_parser("query", help="Query the codebase")
     query_parser.add_argument("question", help="Question to ask")

     # watch command
     watch_parser = subparsers.add_parser(
          "watch", help="Watch codebase and auto-update index"
     )
     watch_parser.add_argument("path", help="Path to codebase")


     args = parser.parse_args()

     if args.command == "index":
          index_codebase(args.path)
     elif args.command == "query":
          query_codebase(args.question)
     elif args.command == "watch":
          start_watcher(args.path)
     else:
          parser.print_help()

if __name__ == "__main__":
     main()
