# Translator.py

A multi-language translation agent system that uses AI agents to translate text into various languages including Spanish, German, Mandarin Chinese, Saudi Arabic, and Thai.

## Overview

This script demonstrates a hierarchical agent architecture where:
- **Specialized agents** handle translation tasks for individual languages
- **Triage agent** routes requests to the appropriate translator agent based on the target language

## Features

- **Multi-language support**: Spanish, German, Mandarin Chinese, Saudi Arabic, and Thai
- **Pronunciation guides**: For languages with non-Latin scripts (Chinese, Arabic, Thai), the output includes transliterated pronunciation
- **Async execution**: Uses async/await patterns for efficient agent orchestration

## Installation

1. Install dependencies from requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up your environment variables in a `.env` file with your OpenAI API credentials:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

Run the script directly:
```bash
python Translator.py
```

The script demonstrates five translation examples:
1. "Hello, how are you?" → Spanish
2. "Good morning, have a nice day!" → German
3. "Good morning, have a nice day!" → Mandarin Chinese
4. "Good morning, have a nice day!" → Saudi Arabic
5. "Good morning, have a nice day!" → Thai

## Agent Structure

### Specialized Agents
- **spanish_agent**: Translates to Spanish
- **german_agent**: Translates to German
- **mandarin_chinese_agent**: Translates to Mandarin Chinese with pinyin pronunciation
- **saudi_arabic_agent**: Translates to Saudi Arabic with transliterated pronunciation
- **thai_agent**: Translates to Thai with transliterated pronunciation

### Triage Agent
Routes incoming requests to the appropriate specialized agent based on the requested target language.

## Output

Each translation includes:
- The translated text
- Pronunciation guides (where applicable) in parentheses
- The final output from the selected agent

## Dependencies

See `requirements.txt` for the complete list of dependencies. Key packages include:
- `openai-agents` - AI agent orchestration library
- `openai` - OpenAI Python client
- `python-dotenv` - Environment variable management
- `httpx` - Async HTTP client
- `pydantic` - Data validation
