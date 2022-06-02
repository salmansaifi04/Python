# define is_palindrome function that take one word in string as a input
# and return True if it is palindrome else return False


def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))
print(is_palindrome("salman"))