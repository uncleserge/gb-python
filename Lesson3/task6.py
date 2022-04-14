# Task 6
#
# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.


def int_func(word):
    return str.title(word)


input_word = input("Введите слово:")
print(int_func(input_word))
