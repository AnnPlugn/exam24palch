morse_alphabet = {
    ". -": "A", "- . . .": "B", "- . - .": "C", "- . .": "D", ".": "E",
    ". . - .": "F", "- - .": "G", ". . . .": "H", ". .": "I", ". - - -": "J",
    "- . -": "K", ". - . .": "L", "- -": "M", "- .": "N", "- - -": "O",
    ". - - .": "P", "- - . -": "Q", ". - .": "R", ". . .": "S", "-": "T",
    ". . -": "U", ". . . -": "V", ". - -": "W", "- . . -": "X", "- . - -": "Y",
    "- - . .": "Z", ". - - - -": "1", ". . - - -": "2", ". . . - -": "3", ". . . . -": "4",
    ". . . . .": "5", "- . . . .": "6", "- - . . .": "7", "- - - . .": "8", "- - - - .": "9",
    "- - - - -": "0"
}

def decode_morse_code(morse_code):
    words = [[str(i) for i in j.split("   ")] for j in morse_code.split('     ')]  # Длинная пауза
    print(words)
    result = ""
    for word in words:
        for letter in word:
            result += morse_alphabet.get(letter, "")
        result += " "
    return result.strip()

# Пример использования
morse_code = ". - - -   .   . . .   . . .     . .     . - . .   - - -   . . . -   .     - . - -   - - -   . . -"
decoded_word = decode_morse_code(morse_code)
print(decoded_word)  # Вывод: JESS I LOVE YOU
# к исходной задаче добавила возможность отправить целое слово дополнителным условием о том что пауза между словами это 5 пробелов