🧠 Autonomous Codebase Intelligence Agent

An offline, agentic AI system that understands codebases, answers architecture and logic questions, detects changes automatically, and provides grounded explanations using local LLMs and vector memory — without relying on third-party APIs.

🚀 Overview

Modern codebases grow large and complex, making it difficult to:

Understand architecture quickly

Locate where logic is implemented

Onboard new developers

Maintain up-to-date mental models

This project solves that by building an autonomous code intelligence agent that:

Ingests a local or GitHub-hosted codebase

Builds semantic memory using embeddings

Retrieves relevant code context

Uses an LLM to reason only over retrieved code

Automatically updates itself when files change

All of this runs fully offline.

✨ Key Features
🔹 Semantic Code Understanding

Parses and chunks code into functions, classes, and logical blocks

Stores semantic embeddings in FAISS

Enables meaning-based search, not keyword matching

🔹 Grounded AI Reasoning (No Hallucinations)

Uses retrieval-augmented generation (RAG)

LLM answers strictly using retrieved code context

If information is missing, the agent explicitly says so

🔹 Autonomous / Agentic Behavior

Watches the codebase for file changes

Automatically re-indexes when code is modified

Keeps vector memory always up-to-date

Runs continuously without manual intervention

🔹 Offline & Self-Hosted

Uses local LLMs (Ollama + LLaMA 3)

No cloud APIs, no tokens, no rate limits

Works entirely on your machine

🔹 GitHub Repository Support

Accepts a GitHub URL

Clones the repository locally using git

Runs the same intelligence pipeline as for local folders

No GitHub API usage required

🔹 Modular & Extensible Architecture

Clean separation of concerns:

Ingestion

Chunking

Embeddings

Vector storage

Reasoning

Agent behaviors

Easy to extend with:

Bug detection

Refactoring suggestions

Architecture summarization


🏗️ System Architecture
Codebase (Local / GitHub)
        ↓
File Ingestion Agent
        ↓
Semantic Chunking (AST + Fallback)
        ↓
Embedding Generation
        ↓
FAISS Vector Store + Metadata DB
        ↓
Semantic Retrieval
        ↓
LLM Reasoning (Grounded)
        ↓
Human-Readable Answers


Autonomous mode adds:

File Watcher → Incremental Re-Indexing

🧰 Tech Stack

Language: Python 3.10+

LLM: LLaMA 3 (quantized, via Ollama)

Embeddings: Sentence Transformers (MiniLM)

Vector DB: FAISS

Metadata Store: SQLite

Agent Runtime: watchdog (file system events)

Version Control Ingestion: git (CLI)

Interface: CLI (extensible to FastAPI)

📦 Installation
1. Clone the repository
git clone <your-repo-url>
cd codebase-agent

2. Create virtual environment
python3 -m venv venv
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Install & run Ollama
ollama pull llama3:8b-instruct-q4_K_M

▶️ Usage
Index a local codebase
python -m agent.cli index ./my_project

Index a GitHub repository
python -m agent.cli index <repo-url>

Ask questions about the codebase
python -m agent.cli query "How does authentication work?"

Run in autonomous mode (watch for changes)
python -m agent.cli watch ./my_project