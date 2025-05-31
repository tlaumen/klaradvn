from pathlib import Path

def pytest_sessionstart(session):
    """Removes all previously automatically created test files"""
    test_folder_test_package =  Path(__file__).parent / 'test-package' / 'tests'
    for f in test_folder_test_package.rglob('*.py'):
        if f.name != "__init__.py":
            f.unlink()