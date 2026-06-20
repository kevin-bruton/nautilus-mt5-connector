import pytest

from mt5connect.config import MT5Config


def make_config(**kwargs) -> MT5Config:
    params = {
        "account": 12345678,
        "password": "test_password",
        "server": "Exness-MT5Trial1",
        "symbols": ["EURUSD"],
    }
    params.update(kwargs)
    return MT5Config(**params)


def test_account_mode_defaults_to_netting():
    assert make_config().account_mode == "netting"


def test_account_mode_accepts_netting():
    assert make_config(account_mode="netting").account_mode == "netting"


def test_account_mode_accepts_hedging():
    assert make_config(account_mode="hedging").account_mode == "hedging"


def test_account_mode_rejects_unknown_value():
    with pytest.raises(ValueError, match="account_mode"):
        make_config(account_mode="invalid")
