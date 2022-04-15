def printCorrespondingWords(multiples, words):
    sentence = ""
    for key in multiples:
        sentence += words[key]
    print(sentence)

def FizzBuzzBonus(words):
    for i in range(1,101):
        multiples = []
        for key in words.keys():
            if (i % int(key) == 0):
                multiples.append(key)
        if (len(multiples) > 0):
            printCorrespondingWords(multiples, words)
        else:    
            print(i)



# Tests :
# -------

'''
words = {
    '3' : 'Fizz',
    '5' : 'Buzz'
}

FizzBuzzBonus(words)
'''

words = {
    '3' : 'Fizz',
    '5' : 'Buzz',
    '12': 'Lazz'
}

FizzBuzzBonus(words)