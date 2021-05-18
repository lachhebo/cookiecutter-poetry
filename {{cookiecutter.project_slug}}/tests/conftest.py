import pytest

@pytest.fixture
def debug(monkeypatch):
    monkeypatch.setenv('DEBUG', 'True')
    print('this is a fixture')
