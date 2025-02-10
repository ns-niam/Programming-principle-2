#Eleventh exercise: write a Python function that checks whether a word or phrase is palindrome or not. Note: A palindrome is word,
#phrase, or sequence that reads the same backward as forward, e.g., madam

def palindrome(word):
    if word == word[::-1]: #With word[::-1] operation we can read the text on the contrary.
        print("Palindrome")
    else:
        print("Not palindrome")
        
palindrome_check = input("Enter a word or phrase: ")
palindrome(palindrome_check)
