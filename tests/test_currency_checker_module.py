# import pytest
# from unittest.mock import patch
# from fetchai.fetchai.currency_checker_module import fetch_currency_rate
#
#
# @patch('currency_checker_module.requests.get')
# def test_fetch_currency_rate(mock_get):
#     mock_get.return_value.status_code = 200
#     mock_get.return_value.json.return_value = {'rates': {'USD': 1.2}}
#
#
#     fetch_currency_rate()
