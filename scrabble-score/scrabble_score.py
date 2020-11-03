def score(word):
    result = 0
    values = {1: ('A', 'E','I', 'O', 'U', 'L', 'N', 'R', 'S', 'T'),
              2: ('D', 'G'),
              3: ('B', 'C', 'M', 'P'),
              4: ('F', 'H', 'V', 'W', 'Y'),
              5: ('K'),
              8: ('J', 'X'),
              10:('Q', 'Z')}

    for letter in word.upper():
        for key, value in values.items():
            if letter in value:
                result += key

    return result