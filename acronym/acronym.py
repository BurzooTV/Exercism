def abbreviate(words: str):
    acronym = str()

    clean_words = words.replace('_', '').replace('-', ' ').replace('  ', '')
    list_words = clean_words.split(' ')

    for word in list_words:
        acronym += word[0]

    return acronym.upper()


