'''
this module contains basic rest api tests
'''

# --------------------------
# Imports
# --------------------------

import pytest
import requests

# --------------------------
# tests
# --------------------------


@pytest.mark.duckduckgo
@pytest.mark.rest_api
def test_duckduckgo_instant_answer_api():
    url = "https://duckduckgo.com/?q=python+programming&format=json"

    response = requests.get(url)
    body = response.json()

    assert response.status_code == 200
    assert "Python" in body['AbstractText']
