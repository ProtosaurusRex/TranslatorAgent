import os
import re
import pytest
from dotenv import load_dotenv

load_dotenv()

PLACEHOLDER_VALUES = {
    'your_api_key_here',
    'your-api-key',
    'placeholder',
    'changeme',
    'todo',
}

def test_openai_key_present():
    key = os.getenv('OPENAI_API_KEY')
    assert key is not None, \
        'OPENAI_API_KEY is not set. Add it to .env or GitHub Secrets.'

def test_openai_key_non_empty():
    key = os.getenv('OPENAI_API_KEY', '')
    assert len(key.strip()) > 0, \
        'OPENAI_API_KEY is set but empty.'

def test_openai_key_format():
    key = os.getenv('OPENAI_API_KEY', '')
    # OpenAI keys start with 'sk-' and are at least 40 characters
    assert re.match(r'^sk-.{36,}$', key), \
        'OPENAI_API_KEY does not match expected format (sk-...)'

def test_openai_key_not_placeholder():
    key = os.getenv('OPENAI_API_KEY', '').strip().lower()
    assert key not in PLACEHOLDER_VALUES, \
        'OPENAI_API_KEY appears to be a placeholder value, not a real key.'
