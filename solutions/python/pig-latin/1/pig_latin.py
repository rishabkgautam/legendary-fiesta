"""Function to translate a text to Pig Latin (children's language)

    Rules:
    
    1. If a word begins with a vowel, or starts with "xr" or "yt", add an "ay" sound to the end of the word.

    2. If a word begins with one or more consonants, first move those consonants to the end of the word and then add an "ay" sound to the end of the word.

    3. If a word starts with zero or more consonants followed by "qu", first move those consonants (if any) and the "qu" part to the end of the word, and then add an "ay" sound to the end of the word.

    4. If a word starts with one or more consonants followed by "y", first move the consonants preceding the "y"to the end of the word, and then add an "ay" sound to the end of the word.

"""

def translate(words):
    """ Manipulate the text based on 4 rules

    Args:
        text (str) : A string-type word

    Returns:
        str : The corresponding translated word.
    """
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = []

    for word in words.split():
        # Rule 1: Starts with a vowel, 'xr', or 'yt'
        if word[0] in vowels or word.startswith(('xr', 'yt')):
            result.append(word + 'ay')
            continue

        # Rule 3: Zero or more consonants followed by 'qu'
        qu_index = word.find('qu')
        if qu_index != -1 and all(char not in vowels for char in word[:qu_index]):
            split_idx = qu_index + 2
            result.append(word[split_idx:] + word[:split_idx] + 'ay')
            continue

        # Rules 2 & 4: Consonant(s) followed by a vowel or 'y' acting as a vowel (index > 0)
        for index, char in enumerate(word):
            if char in vowels or (char == 'y' and index > 0):
                result.append(word[index:] + word[:index] + 'ay')
                break

    return ' '.join(result)