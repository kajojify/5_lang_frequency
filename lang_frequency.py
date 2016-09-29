import re
import chardet
from collections import Counter


def load_data(filepath):
    """Производит загрузку содержимого текстового файла filepath.
    Для корректной загрузки определена кодировка содержимого.
    Возвращает содержимое текстового файла"""

    rawdata = open(filepath, "rb").read()
    file_encoding = chardet.detect(rawdata)['encoding']
    return open(filepath, encoding=file_encoding).read()


def get_most_frequent_words(text):
    """Подсчитывает частоту употребления каждого слова в text.
    Выделяет 10 самых частовстречаемых слов. Возвращает список,
    элементами которого являются кортежи, состоящие из двух
    элементов: слово и частота его употребления."""

    words = re.findall(r'\w+', text.lower())
    most_frequent_words = Counter(words).most_common(10)
    return most_frequent_words


if __name__ == '__main__':
    filepath = input("Введите путь к текстовому файлу --- ")
    try:
        text = load_data(filepath)
    except FileNotFoundError:
        print("Нет такого файла или директории! Завершение программы.")
        exit()
    most_frequent_words = get_most_frequent_words(text)
    print("{:>10}{:>10}".format("Слово", "Частота"))
    for word, frequency in most_frequent_words:
        print("{:>10}{:>10}".format(word, frequency))

