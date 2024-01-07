def word_statistics(input_file, output_file):
    word_count = {}
    with open(input_file, 'r', encoding = 'utf-8') as file:
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

    sorted_word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

    with open(output_file, 'w') as file:
        for word, count in sorted_word_count:
            file.write(f"{word}: {count}\n")

word_statistics('revisor.txt', 'word_statistics.txt')