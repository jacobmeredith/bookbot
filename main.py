file_name = './books/frankenstein.txt'

def get_word_count(contents):
    return len(file_contents.split())

with open(file_name) as f:
    file_contents = f.read()
    print(f"Word count: {get_word_count(file_contents)}")
