import argparse

def get_word_count(contents):
    return len(contents.split())

def get_character_count(contents):
    letters = {}
    for letter in contents.lower():
        if letter not in letters:
            letters[letter] = 0

        letters[letter] += 1

    return letters

def format_report(file_name, word_count, character_count):
    report = f"--- Begin report of {file_name} ---\n"
    report += f"{word_count} words found in the document\n\n"

    character_list = sorted(character_count.items(), key=lambda character: character[1], reverse=True)

    for char, count in character_list:
        if not char.isalpha():
            continue
        report += f"The '{char}' character was found {count} times\n"

    report += "--- End report ---"

    return report

def generate_report(file_name):
    with open(file_name) as f:
        file_contents = f.read()

        word_count = get_word_count(file_contents)
        character_count = get_character_count(file_contents)

        print(format_report(file_name, word_count, character_count))

def main():
    parser = argparse.ArgumentParser("generate_report")
    parser.add_argument("--file", dest="file", help="The path to the text file you want to generate a report for", type=str)
    args = parser.parse_args()

    generate_report(args.file)

if __name__ == "__main__":
    main()    

