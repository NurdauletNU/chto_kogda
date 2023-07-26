import re
from collections import Counter
from openpyxl import Workbook, load_workbook

# Напишите программу, в которой возвращаются домены из списка e-mail адресов.
def extract_domains(emails):
    domain_list = []
    for email in emails:
        match = re.search(r'@([\w.-]+)', email)
        if match:
            domain = match.group(1)
            domain_list.append(domain)
    return domain_list

email_list = ['example1@gmail.com', 'example2@yahoo.com', 'example3@hotmail.com']
domains = extract_domains(email_list)
print(domains)

# Напишите программу, в которой извлекаются слова, начинающиеся на гласную букву
def extract_vowel_words(text):
    # Используем регулярное выражение для извлечения слов, начинающихся с гласной буквы
    vowel_words = re.findall(r'\b[aeiouAEIOU]\w+', text)
    return vowel_words

input_text = "An apple a day keeps the doctor away"
vowel_words = extract_vowel_words(input_text)
print(vowel_words)

# Напишите программу, в которой разбивается строка по нескольким разделителям

def split_string(input_string, delimiters):
    delimiter_pattern = '|'.join(map(re.escape, delimiters))
    split_result = re.split(delimiter_pattern, input_string)
    return split_result

input_string = "Hello, World! How are you today?"
delimiters = [',', '!', '?']
result = split_string(input_string, delimiters)
print(result)

# Пользователю предоставляется список кандидатов, каждый из голосующих делает свой
# выбор. Выбранный кандидат добавляется в список. В итоге имеется неизменяемый список
# кандидатов.
# Определить победителя, в зависимости от количества встречаемости в списке кандидата.
# Определить количество голосов победителя.
# В случае, если будет двое победителей, сделать сортировку по длине слова между ними и
# выбрать победителя с минимальным количеством букв в имени.
# Кандидаты в выборы: Аскаров, Бекмуханов, Ернур, Пешая, Карим, Шаримазданов и т.д.
# Вы отдаете голос за:
# Победитель выборов: Ернур



candidates = ['Аскаров', 'Бекмуханов', 'Ернур', 'Пешая', 'Карим', 'Шаримазданов']

votes = []
for candidate in candidates:
    vote = input(f"Вы отдаете голос за {candidate}? (Да/Нет): ")
    if vote.lower() == 'да':
        votes.append(candidate)

vote_count = Counter(votes)

winner = max(vote_count, key=vote_count.get)


if list(vote_count.values()).count(vote_count[winner]) > 1:
    top_candidates = [c for c in vote_count if vote_count[c] == vote_count[winner]]
    winner = min(top_candidates, key=len)

print(f"Победитель выборов: {winner}")
print(f"Количество голосов победителя: {vote_count[winner]}")








