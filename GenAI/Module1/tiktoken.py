# ====================
# OpenAI Tokenizers
# ====================

import os
import sys


def load_env_file(file_path: str) -> None:
    """Load KEY=VALUE pairs into os.environ without overwriting existing vars."""
    if not os.path.exists(file_path):
        return

    with open(file_path, "r", encoding="utf-8") as env_file:
        for line in env_file:
            stripped = line.strip()
            if not stripped or stripped.startswith("#") or "=" not in stripped:
                continue
            key, value = stripped.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key and key not in os.environ:
                os.environ[key] = value


# This file is named `tiktoken.py`, so remove its directory from sys.path
# before importing the real third-party package to avoid self-import.
current_dir = os.path.abspath(os.path.dirname(__file__))
project_root = os.path.abspath(os.path.join(current_dir, ".."))
default_secrets_file = os.path.join(project_root, ".secrets", "keys.env")
secrets_file = os.getenv("GENAI_KEYS_FILE", default_secrets_file)
load_env_file(secrets_file)

sys.path = [
    path
    for path in sys.path
    if os.path.abspath(path or os.getcwd()) != current_dir
]

import tiktoken

# For GPT-5 and newer models
try:
    # Preferred when the model name is known by the installed tiktoken version.
    encoding = tiktoken.encoding_for_model("gpt-5")
except KeyError:
    # Fallback encoding for newer/unknown OpenAI models.
    encoding = tiktoken.get_encoding("o200k_base")

prompt = "Your prompt here"
token_count = len(encoding.encode(prompt))

print(f"[tiktoken local] Tokens: {token_count}")
# Also works with other OpenAI models


# ==============================
# Anthropic (Claude) tokenizers
# ==============================
"""
try:
    import anthropic
except ImportError:
    anthropic = None

anthropic_api_key = os.getenv("ANTHROPIC_API_KEY")
if anthropic and anthropic_api_key:
    client = anthropic.Anthropic(api_key=anthropic_api_key)
    message = client.messages.count_tokens(
        model="claude-sonnet-4-5",
        messages=[{"role": "user", "content": prompt}]
    )
    print(f"[Anthropic API] Input tokens: {message.input_tokens}")
else:
    print("[Anthropic API] Skipped (no package or no ANTHROPIC_API_KEY).")

"""

# Not working until buy subscription 

# =========================
# Google Gemini tokenizers
# =========================


try:
    import google.generativeai as genai
except ImportError:
    genai = None

google_api_key = os.getenv("GOOGLE_API_KEY")
if genai and google_api_key:
    genai.configure(api_key=google_api_key)
    model = genai.GenerativeModel("gemini-3.8-flash")
    token_count = model.count_tokens(prompt)
    print(f"[Gemini API] Tokens: {token_count.total_tokens}")
else:
    print("[Gemini API] Skipped (no package or no GOOGLE_API_KEY).")
