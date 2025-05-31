import warnings

import ollama

from klaradvn.build_model import create_model

def test_create_model():
    models = [m.model for m in ollama.list().models]
    if 'klaradvn:latest' in models:
        warnings.warn("klaravdn model already installed. Test is currently not representative on system!")
    create_model()
    assert 'klaradvn:latest' in models