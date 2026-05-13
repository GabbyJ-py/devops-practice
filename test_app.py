from app import add_numbers

def test_add():
  assert add_numbers(-1, 1) == 0
  assert add_numbers(2, 3) == 5
