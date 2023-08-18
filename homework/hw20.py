# Реализовать проверку фразы на "анаграмму".
def is_anagram1(word1, word2):
    word1 = "".join(word1).lower().replace(",","")
    word2 = "".join(word2).lower().replace(",","")
    return "Фразы являются анаграммами" if sorted(list(filter(lambda x: x.isalpha(),word1)))==\
    sorted(list(filter(lambda x: x.isalpha(),word2))) else "Фразы не являются анаграммами"


print(is_anagram1(input("Введите первую фразу: "), input("Введите вторую фразу: ")))


