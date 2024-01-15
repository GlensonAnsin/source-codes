def is_palindrome(string):
    #base case
    if len(string) <= 1:
        return True
    else:
        #recursive case
        if string[0] == string[-1]:
            return is_palindrome(string[1:-1])
        else:
            return False
user_input = str(input("Enter string:"))
if (is_palindrome(user_input)==True):
    print("Yes! The string you entered is a palindrome.")
else:
    print("Unfortunately, the string you encoded is NOT a palindrome.")