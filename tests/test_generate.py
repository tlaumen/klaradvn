from pathlib import Path
import warnings

import ollama
import pytest

from klaradvn.generate import create_model, generate_tests
from klaradvn.extract import extract_function_code

def test_create_model():
    models = [m.model for m in ollama.list().models]
    if 'klaradvn:latest' in models:
        warnings.warn("klaravdn model already installed. Test is currently not representative on system!")
    create_model()
    assert 'klaradvn:latest' in models

def test_generate_tests():
    function = "another_function"
    code, path = extract_function_code(Path(__file__).parent / 'test-package', function)
    success, test_path = generate_tests(path, code, function)
    if success:
        pytest.main(["-x", test_path])