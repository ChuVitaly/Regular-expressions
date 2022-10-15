import re
from pprint import pprint


# читаем адресную книгу в формате CSV в список contacts_list
import csv

contacts_list = []

header_list = ['lastname', 'firstname', 'surname', 'organization']

reg_ex4 = r'^([А-я]\w+),\s?([А-я]\w+),\s?([А-я]\w+|)|(ФНС|Минфин)|'

with open("phonebook_raw.csv") as f:
    # rows = csv.DictReader(f, delimiter=" ")
    rows = csv.reader(f, delimiter=" ")


    for row in rows:
        x = ','.join(row)
        fio = re.findall(reg_ex4, x)
        fio = re.findall(r'(\w+)', str(fio))
        contacts_list.append(fio)




    with open('new_phonebook.csv', 'w', encoding='utf-8') as f:
        i = 1
        writer = csv.writer(f, delimiter=",")
        writer.writerow(header_list)
        while i != len(contacts_list):
            writer.writerow(contacts_list[i])
            i += 1



# reg_ex4 = r'^\S\'(\b[Аа-я\w]+\b)\'?\s?\S?\s\S?(\b[Аа-я\w]+\b)\s?\S*?\W*?(\b[А-я\w]+\b)'
# reg_fone = r'(\+\d|\d)\s*(\(|)(\d{3})[\s\)-]*(\d{3})\-*(\d{2})\-*(\d{2})'
# reg_fone1 = r'(\+\d|\d)\s*(\(|)(\d{3})[\s\)-]*(\d{3})\-*(\d{2})\-*(\d{2})\W*?.(доб.\s\d{4})'
# reg_fone2 = r'[,](\+7|8),?((495)|\(495\))(-|,)?([0-9]{3})?-?([0-9]{2}?)-?([0-9]{2})'





# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     # Вместо contacts_list подставьте свой список
#     datawriter.writerows(contacts_list)
