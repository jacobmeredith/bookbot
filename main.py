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

with open(file_name) as f:
    file_contents = f.read()
    
    print(f"Word count: {get_word_count(file_contents)}")
    print(f"Character count: {get_character_count(file_contents)}")

