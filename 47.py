def cyclic_shift_words(in1, in2):
    s1 = in1.split(" ")
    s2 = in2.split(" ")
    res = []
    for i in range(len(s1)):
        res.append(s1[i])
        res.append(s2[i])
    res = ' '.join(res)
    return res


# Пример использования
input_sentence1 = "'один два три"
input_sentence2 = "альфа бетта гамма"
result = cyclic_shift_words(input_sentence1, input_sentence2)
print(result)
