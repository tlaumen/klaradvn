from pathlib import Path
import warnings
import subprocess

from _pytest.mark import pytest_addoption
import ollama
import pytest

from klaradvn.generate import create_model, generate_tests
from klaradvn.extract import extract_function_code, extract_class

PATH_PACKAGE = Path(__file__).parent / 'test-package'

def test_invoke_pytest_using_python():
    path = Path(__file__).parent / 'meta_test.py'
    try:
        # Required to use subprocess since pytest.main() has ModuleNotFoundError bug
        subprocess.run([f"pytest {path} --noconftest"], shell=True)
    except:
        assert False

def test_create_model():
    models = [m.model for m in ollama.list().models]
    if 'klaradvn:latest' in models:
        warnings.warn("klaravdn model already installed. Test is currently not representative on system!")
    create_model()
    assert 'klaradvn:latest' in models

def test_generate_tests_function():
    function = "another_function"
    code, path = extract_function_code(PATH_PACKAGE, function)
    success, test_path = generate_tests(path, code, function)
    try:
        if success:
            subprocess.run([f"pytest {test_path} --noconftest"], shell=True)
    except:
      assert False

def test_generate_tests_class():
    class_ = "CoolNewList"
    result = extract_class(PATH_PACKAGE, class_)
    success, test_path = generate_tests(Path(result['file_path']), result['source_code'], class_)
    print(test_path)
    try:
        if success:
            subprocess.run([f"pytest {test_path} --noconftest"], shell=True)
    except:
        assert False