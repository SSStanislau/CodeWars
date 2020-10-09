'''
Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
'''


def pig_it(text):
    return ' '.join([el[1:len(el)]+el[0]+'ay' if el.isalpha() else el for el in text.split()])