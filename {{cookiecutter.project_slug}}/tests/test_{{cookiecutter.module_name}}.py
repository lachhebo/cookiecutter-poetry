"""Tests for `{{ cookiecutter.module_name }}` package."""
from unittest.mock import patch

from src.{{ cookiecutter.module_name }} import main

TESTED_MODULE =  'src.{{ cookiecutter.module_name }}'

@patch(f'{TESTED_MODULE}.version', return_value = 5)
def test_main__return_pytest_version_6(mock_version, debug):
    # given
      
    # when
    result = main()
     
    # then
    assert result == 5
