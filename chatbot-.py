#!/usr/bin/env python3
"""
Terminal-based Chatbot using Google Gemini 2.5 Flash
----------------------------------------------------
This script connects to Google’s Gemini LLM (via google-genai SDK)
and allows the user to chat from the terminal.

Steps to run:
1. Install dependencies:
   pip install -U google-genai

2. Set your API key in an environment variable:
   - Windows CMD: set GEMINI_API_KEY=your_api_key_here
   - PowerShell: $Env:GEMINI_API_KEY="your_api_key_here"
   - Mac/Linux: export GEMINI_API_KEY=your_api_key_here

3. Run the script:
   python chatbot.py

Author: Warisha
"""

import os
import sys
from google import genai  # Import Google GenAI client


def make_client():
    """
    Creates a GenAI client using the API key.
    First, it tries to read the GEMINI_API_KEY environment variable.
    If not found, it asks the user to input the key.
    """
    api_key = os.getenv("GEMINI_API_KEY")  # Look for environment variable
    if api_key:
        return genai.Client(api_key=api_key)

    # Prompt user if environment variable is not set
    key = input("Enter GEMINI API key: ").strip()
    if key:
        return genai.Client(api_key=key)

    # If no key is provided, exit the program
    print("Error: No API key provided.")
    sys.exit(1)


def main():
    """Main chatbot loop. Accepts user input and displays Gemini responses."""
    try:
        client = make_client()
    except Exception as e:
        print("Failed to create GenAI client:", e, file=sys.stderr)
        sys.exit(1)

    print("Chatbot started! Type 'exit' or press Ctrl+C to quit.")

    # Infinite loop for chat until user exits
    while True:
        try:
            user_input = input("You: ")
        except (EOFError, KeyboardInterrupt):  # Handle Ctrl+C or Ctrl+D
            print("\nGoodbye.")
            break

        if not user_input:
            continue  # Skip empty input
        if user_input.lower() in ("exit", "quit"):
            print("Goodbye.")
            break

        try:
            # Send input to Gemini model
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=user_input,
            )
            # Print the model's response
            print("Chatbot:", getattr(response, "text", str(response)))
        except Exception as e:
            print("API error:", e, file=sys.stderr)


if __name__ == "__main__":
    main()
