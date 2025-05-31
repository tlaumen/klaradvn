from pathlib import Path
import subprocess
import os

import typer

from klaradvn.build_model import create_model
from klaradvn.extract import extract_function_code
from klaradvn.extract import extract_class
from klaradvn.generate import generate_tests

app = typer.Typer()


@app.command()
def create_model():
    create_model()


@app.command()
def test_class(class_: str):
    result = extract_class(Path(os.getcwd()), class_)
    success, test_path = generate_tests(Path(result['file_path']), result['source_code'], class_)
    if success:
        subprocess.run([f"pytest {test_path} --noconftest"], shell=True)

@app.command()
def test_function(function: str):
    code, path = extract_function_code(os.getcwd(), function)
    success, test_path = generate_tests(path, code, function)
    if success:
        subprocess.run([f"pytest {test_path}"], shell=True)


if __name__ == "__main__":
    app()
