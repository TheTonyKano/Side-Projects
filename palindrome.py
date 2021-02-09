def isPalindrome(string):
    revString = ''.join(reversed(string))
    if string.replace(" ", "") == revString.replace(" ", "") and string.replace(" ", "") != "":
        print("It's a Palindrome")
    else:
        print("It's not a Palindrome")

isPalindrome(str(input("Enter a word to see if it is a palindrome: ")).lower())