from pathlib import Path
import warnings
import subprocess


from klaradvn.generate import generate_tests
from klaradvn.extract import extract_function_code, extract_class

PATH_PACKAGE = Path(__file__).parent / 'test-package'

def test_invoke_pytest_using_python():
    path = Path(__file__).parent / 'meta_test.py'
    try:
        # Required to use subprocess since pytest.main() has ModuleNotFoundError bug
        subprocess.run([f"pytest {path} --noconftest"], shell=True)
    except:
        assert False

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
    try:
        if success:
            subprocess.run([f"pytest {test_path} --noconftest"], shell=True)
    except:
        assert False