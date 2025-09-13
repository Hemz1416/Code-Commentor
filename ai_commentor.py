# ai_commentor.py
import requests
import json

OLLAMA_URL = "http://localhost:11434/api/generate"

def get_prompt_for_action(code_input: str, action: str) -> str:
    """
    Selects and formats the correct prompt based on the desired action.
    """
    
    prompts = {
        "comment": f"""
Your task is to be an expert Python programmer. 
Add clear, concise comments to the following Python code.
First, provide a high-level summary of the code in a docstring.
Then, add line-by-line comments where necessary to explain the key logic.
Return ONLY the fully commented Python code block.

---
Code to comment:
{code_input}
""",
        "explain": f"""
Your task is to be a helpful programming assistant.
Explain the following Python code in simple, easy-to-understand terms.
Describe what the code does, how it works, and what the expected output might be.
Format your explanation clearly using markdown.

---
Code to explain:
{code_input}
""",
        "refactor": f"""
Your task is to be a senior Python developer.
Refactor the following Python code to make it more efficient, readable, and Pythonic.
Provide the refactored code first, then add a brief explanation of the changes you made and why they are improvements.
Return the code inside a Python code block and the explanation below it.

---
Code to refactor:
{code_input}
""",
        "test": f"""
Your task is to be a software quality engineer.
Write pytest unit tests for the following Python code.
Make sure to cover the main functionality and any edge cases.
Return ONLY the Python code block containing the complete unit tests.

---
Code to test:
{code_input}
"""
    }
    return prompts.get(action, code_input) # Default to returning code if action is unknown

def perform_ai_action(code_input: str, action: str) -> str:
    """
    Sends code to a local Ollama model to perform a specific action.
    """
    print(f"Sending code to local Ollama model for action: {action}...")

    prompt = get_prompt_for_action(code_input, action)

    payload = {
        "model": "codellama",
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status() # Raise an exception for bad status codes
        result = response.json()
        
        # Ollama returns the result in the 'response' field
        processed_code = result.get("response", "")
        return processed_code.strip()
        
    except requests.exceptions.RequestException as e:
        print(f"Error communicating with Ollama: {e}")
        return "Error: Could not generate a response. Is the Ollama server running and accessible?"
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return "An unexpected error occurred."
