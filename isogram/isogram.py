def is_isogram(string):
    speecial_chars = "!?/-_@#$%^&*():;',.[]=+- "
    lower_string = string.lower()

    for word in lower_string:
        if word.lower() in speecial_chars:
            continue
        else:
            if lower_string.count(word) > 1:
                return False

    return True