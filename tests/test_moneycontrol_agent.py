
import pytest
from unittest.mock import patch
from backend.agents.stealth.moneycontrol_agent import run

@patch('backend.agents.stealth.moneycontrol_agent.requests.get')
def test_moneycontrol_agent(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = '<html><div id="price">1500</div><div id="eps">30</div><div id="pe">20</div></html>'

    result = run('INFY')
    assert 'price' in result
    assert 'eps' in result
    assert 'pe' in result
