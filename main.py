def main():

    sentence = input("Ввведите слова через пробел: ")
    words_list = sentence.split()

    longest_word = max(words_list, key=len)

    print(f"Самое длинное слово: {longest_word}. его длинна {len(longest_word)}")


if __name__ == "__main__":
    main()
