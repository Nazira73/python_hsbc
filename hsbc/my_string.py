alphabets = "abcdefghijklmnopqrstuvwxyz"
alphabets_upper = alphabets.upper() 

def reverse_a_string(s):
    """
    This function takes a string as input and returns the string reversed.
    
    :param s: The string to be reversed
    :return: The reversed string
    """
    return s[::-1]

def is_pallidrome(s):
    """
    This function checks if a given string is a palindrome.
    
    :param s: The string to check
    :return: True if the string is a palindrome, False otherwise
    """
    reversed_s = reverse_a_string(s)
    return s == reversed_s