import ast
import pathlib
import pytest

TRANSLATOR_PATH = pathlib.Path('Translator.py')

REQUIRED_AGENTS = {
    'spanish_agent',
    'german_agent',
    'mandarin_chinese_agent',
    'saudi_arabic_agent',
    'thai_agent',
}

def parse_triage_handoffs(source: str) -> set[str]:
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        for kw in node.keywords:
            if kw.arg == 'handoffs' and isinstance(kw.value, ast.List):
                return {
                    elt.id for elt in kw.value.elts
                    if isinstance(elt, ast.Name)
                }
    return set()

def test_all_required_agents_in_handoffs():
    source = TRANSLATOR_PATH.read_text()
    registered = parse_triage_handoffs(source)
    missing = REQUIRED_AGENTS - registered
    assert not missing, (...)

def test_triage_has_no_unknown_handoffs():
    source = TRANSLATOR_PATH.read_text()
    registered = parse_triage_handoffs(source)
    unknown = registered - REQUIRED_AGENTS
    assert not unknown, (...)