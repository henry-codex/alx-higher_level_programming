#!/usr/bin/python3
def islower(c):
    """Check for lowercase characters."""
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    else:
        return False

# Example usage
char = 'a'
if islower(char):
    print(f"{char} is a lowercase character")
else:
    print(f"{char} is not a lowercase character")

