
import pytest
from unittest.mock import patch
from backend.orchestrator import run_agent

@patch('backend.orchestrator.importlib.util.spec_from_file_location')
def test_orchestrator_agent_interaction(mock_spec):
    mock_agent = lambda x: {"agent": "mock_agent", "symbol": x, "output": "integration_success"}
    mock_spec.return_value.loader.exec_module = lambda x: setattr(x, 'run', mock_agent)

    result = run_agent('INFY', '/path/to/mock_agent.py')
    assert result['symbol'] == 'INFY'
    assert result['output'] == 'integration_success'
