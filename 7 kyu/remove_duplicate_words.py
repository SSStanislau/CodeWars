'''
Your task is to remove all duplicate words from a string, leaving only single (first) words entries.

Example:

Input:

'alpha beta beta gamma gamma gamma delta alpha beta beta gamma gamma gamma delta'

Output:

'alpha beta gamma delta'

'''


def remove_duplicate_words(s):
    present = []
    for word in s.split(" "):
        if word not in present: present.append(word)
    return " ".join(present)