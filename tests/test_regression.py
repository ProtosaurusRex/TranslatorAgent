import pytest
import asyncio
import re
from agents import Agent, Runner

# ── Agent definitions (mirrors Translator.py) ──────────────────
spanish_agent = Agent(
    name='spanish_agent',
    instructions='You translate the user\'s message to Spanish.'
)
german_agent = Agent(
    name='german_agent',
    instructions='You translate the user\'s message to German.'
)
mandarin_agent = Agent(
    name='mandarin_chinese_agent',
    instructions='You translate the user\'s message to Mandarin Chinese. '
                 'Use transliterated pinyin in parentheses after the Chinese '
                 'characters to show pronunciation.'
)
arabic_agent = Agent(
    name='saudi_arabic_agent',
    instructions='You translate the user\'s message to Saudi Arabic. '
                 'Use transliterated Arabic in parentheses after the Arabic '
                 'script to show pronunciation.'
)
thai_agent = Agent(
    name='thai_agent',
    instructions='You translate the user\'s message to Thai. '
                 'Use transliterated Thai in parentheses after the Thai '
                 'script to show pronunciation.'
)

SAMPLE = 'Good morning, have a nice day!'

def run(agent, prompt):
    return asyncio.run(Runner.run(agent, prompt)).final_output

# ── Tests ──────────────────────────────────────────────────────
def test_spanish_non_empty():
    result = run(spanish_agent, f"Translate '{SAMPLE}' to Spanish.")
    assert result and len(result.strip()) > 0

def test_german_non_empty():
    result = run(german_agent, f"Translate '{SAMPLE}' to German.")
    assert result and len(result.strip()) > 0

def test_mandarin_contains_cjk():
    result = run(mandarin_agent, f"Translate '{SAMPLE}' to Mandarin Chinese.")
    assert re.search(r'[\u4e00-\u9fff]', result), \
        'Output missing CJK characters'

def test_mandarin_has_pinyin():
    result = run(mandarin_agent, f"Translate '{SAMPLE}' to Mandarin Chinese.")
    assert '(' in result and ')' in result, \
        'Output missing parenthetical pronunciation guide'

def test_arabic_contains_arabic_script():
    result = run(arabic_agent, f"Translate '{SAMPLE}' to Saudi Arabic.")
    assert re.search(r'[\u0600-\u06ff]', result), \
        'Output missing Arabic script characters'

def test_arabic_has_transliteration():
    result = run(arabic_agent, f"Translate '{SAMPLE}' to Saudi Arabic.")
    assert '(' in result and ')' in result, \
        'Output missing parenthetical pronunciation guide'

def test_thai_contains_thai_script():
    result = run(thai_agent, f"Translate '{SAMPLE}' to Thai.")
    assert re.search(r'[\u0e00-\u0e7f]', result), \
        'Output missing Thai script characters'
