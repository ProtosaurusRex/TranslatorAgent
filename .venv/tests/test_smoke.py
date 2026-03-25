import pytest
import asyncio
import re
import ast
import pathlib
from agents import Agent, Runner

# ── Import agents from Translator.py ───────────────────────────
import sys
sys.path.insert(0, '.')
from Translator import triage_agent


CASES = [
    ('Hello, how are you?', 'Spanish', None),
    ('Good morning, have a nice day!', 'German', None),
    ('Good morning, have a nice day!', 'Mandarin Chinese', r'[\u4e00-\u9fff]'),
    ('Good morning, have a nice day!', 'Saudi Arabic', r'[\u0600-\u06ff]'),
    ('Good morning, have a nice day!', 'Thai', r'[\u0e00-\u0e7f]'),
]

@pytest.mark.parametrize('phrase,lang,script_re', CASES)
def test_triage_routes_correctly(phrase, lang, script_re):
    prompt = f"Translate '{phrase}' to {lang}."
    result = asyncio.run(Runner.run(triage_agent, prompt)).final_output
    assert result and len(result.strip()) > 0, \
        f'Empty output for {lang}'
    if script_re:
        assert re.search(script_re, result), \
            f'{lang} output missing expected script characters'

# ── Structural check: all agents registered in handoffs ────────
EXPECTED_AGENTS = {
    'spanish_agent', 'german_agent', 'mandarin_chinese_agent',
    'saudi_arabic_agent', 'thai_agent'
}

def test_all_agents_in_triage_handoffs():
    handoff_names = {a.name for a in triage_agent.handoffs}
    missing = EXPECTED_AGENTS - handoff_names
    assert not missing, \
        f'Agents missing from triage handoffs: {missing}'
