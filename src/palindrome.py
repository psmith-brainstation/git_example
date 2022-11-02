

def is_palindrome(word):
    '''
    input == a string
    output == True if palimdrome, else False
    '''
    letters = list(word)
    letters.insert(0, 'x')

    for i in range(1, len(letters)):
        if letters[i] != letters[-1*i]:
            return(False)
        
    return(True)

print(is_palindrome("computer"))