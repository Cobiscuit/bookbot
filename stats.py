def count_words(text):
    # split() with no argument handles spaces/newlines correctly
    return len(text.split())


def count_unique_chars(text):
    char_counts = {}
    for char in text.lower():
        if char.isalpha():  # only count letters
            char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts


def sort_on(dict_item):
    return dict_item["num"]


def sort_characters(char_counts):
    char_list = []

    for char, count in char_counts.items():
        char_list.append({"char": char, "num": count})

    # sort in-place, greatest to least
    char_list.sort(key=sort_on, reverse=True)
    return char_list
