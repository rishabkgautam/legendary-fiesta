def is_isogram(phrase):
    phrase = ''.join([letter for letter in phrase if letter.isalpha()]).lower()
    return len(phrase) == len(set(phrase))
