def main():
   book_path = "books/frankenstein.txt"
   text = get_book_path(book_path)
   num_words = word_count(text)
   char_dict = character_count(text)
   sorted_char_dict = sorted_dict(char_dict)
   print(f"--For {book_path}--")
   print(f"--{num_words}--")
   for item in sorted_char_dict:
        if not item["char"].isalpha():
           continue
        print(f"The '{item['char']}' character was found {item['num']} times")
   

def sort_on(d):
    return d["num"]
def word_count(file_contents):
    words = file_contents.split()
    return len(words)

def get_book_path(path):
    with open(path) as f:
        return f.read()

def character_count(text):
    char_count = {}
    for c in text:
        lowered = c.lower()
        if lowered in char_count:
            char_count[lowered] += 1
        else:
            char_count[lowered] = 1
    return char_count


def sorted_dict(char_dict):
    sorted_list = []
    for ch in char_dict:
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
main()