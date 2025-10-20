def greet():
    """Return a small message used by CI to verify the build."""
    return "Hello CI"

if __name__ == "__main__":
    print(greet())
# minor note: CI check should pass quickly
