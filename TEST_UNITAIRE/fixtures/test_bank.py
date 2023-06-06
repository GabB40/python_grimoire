import pytest
from bank import Account


@pytest.fixture
def account() -> Account:
    return Account(initial_balance=1000)


def test_deposit(account) -> None:
    account.deposit(amount=1000)
    assert account.balance == 2000


def test_withdraw(account) -> None:
    account.withdraw(amount=500)
    assert account.balance == 500
    
def test_negative_withdraw() -> None:
    account = Account(initial_balance=200)
    with pytest.raises(ValueError):
        account.withdraw(amount=500)    

def test__create_identifier_length_of_identifier(account) -> None:
    assert len(account.identifier) == 25


def test__create_identifier_is_alnum(account):
    assert account.identifier.isalnum() is True
