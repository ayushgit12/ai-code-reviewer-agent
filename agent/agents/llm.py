import ollama


def ask_llm(question: str, context: str) -> str:
    """
    Ask the LLM a question grounded in provided context.
    """
    prompt = f"""
You are a senior software engineer.

Answer the question ONLY using the code context provided.
If the answer is not present, say "Not found in the codebase".

QUESTION:
{question}

CODE CONTEXT:
{context}

EXPLANATION:
"""

    response = ollama.chat(
        model="llama3:8b-instruct-q4_K_M",
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
