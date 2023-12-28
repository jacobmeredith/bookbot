file_name = './books/frankenstein.txt'

def get_word_count(contents):
    return len(file_contents.split())

def get_character_count(contents):
    letters = {}
    for letter in contents.lower():
        if letter not in letters:
            letters[letter] = 0

        letters[letter] += 1

    return letters

def print_report(word_count, character_count):
    print(f"--- Begin report of {file_name} ---")
    print(f"{word_count} words found in the document\n")

    character_list = sorted(character_count.items(), key=lambda character: character[1], reverse=True)

    for char, count in character_list:
        if not char.isalpha():
            continue
        print(f"The '{char}' character was found {count} times")

    print("--- End report ---")

with open(file_name) as f:
    file_contents = f.read()
    
    word_count = get_word_count(file_contents)
    character_count = get_character_count(file_contents)

    print_report(word_count, character_count)

