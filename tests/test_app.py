from app import greet

def test_greet_message():
    assert greet() == "Hello CI"
