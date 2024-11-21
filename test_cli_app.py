import pytest
from click.testing import CliRunner
from src.feedme.cli import greet, factorial, reverse

@pytest.fixture
def runner():
    return CliRunner()

def test_greet(runner):
    result = runner.invoke(greet, ['Alice'])
    assert result.exit_code == 0
    assert result.output.strip() == 'Hello, Alice!'

def test_factorial(runner):
    result = runner.invoke(factorial, ['5'])
    assert result.exit_code == 0
    assert result.output.strip() == '120'
    
    result = runner.invoke(factorial, ['-1'])
    assert result.exit_code == 0
    assert result.output.strip() == 'Factorial is not defined for negative numbers'

def test_reverse(runner):
    result = runner.invoke(reverse, ['hello'])
    assert result.exit_code == 0
    assert result.output.strip() == 'olleh'
