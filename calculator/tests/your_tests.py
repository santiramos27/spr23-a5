#!/usr/bin/env python3
from calculator_adapter import run

# Checks that the program outputs "2" for an input of "3 - 1"
assert run("3 - 1").output == "2"
# Checks that the program outputs "3" for an input of "6 / 2"
assert run("6 / 2").output == "3"
# Checks that the program fails (correctly errors) for input "5 $ 5"
assert run("5 $ 5").exit_status != 0
  
print("All tests passed!")
