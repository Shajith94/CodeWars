 #Write a function that checks if a given string (case insensitive) is a palindrome.   
def is_palindrome(s):
    return  s.lower()[::-1] == s.lower() 
#[::- 1] will do it in reverse 