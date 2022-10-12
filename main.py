import re
from pprint import pprint


# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)
x = contacts_list[1]
z = str(x)
pprint(z)
print(type(z))
# reg
reg_ex4 = r'^\W+(\b[а-яА-Я\w]+\b)\W*(\b[а-яА-Я\w]+\b)\W*(\b[а-яА-Я\w]+\b)*\''
reg_posish = r"(?P<q>[\s])'(\b[а-яА-Я\w]+\b)\s?(\b[а-яА-Я\w]+\b)\s+.+?\s*(\b[а-яА-Я\w]+\b)\s*?(\b[а-яА-Я\w]+\b)\s*?'(" \
             r"?P<k>[\S]) "
reg_fone = r'^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$'
reg_organ = r'ФНС|Минфин'


i = 1
while i != len(contacts_list):
    print(re.findall(,reg_ex4 str(contacts_list[i])))
    print(re.findall(reg_organ, str(contacts_list[i])))
    print(re.findall(reg_posish, str(contacts_list[i])))
    print(re.findall(reg_fone, str(contacts_list[i])))
    i += 1











# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     # Вместо contacts_list подставьте свой список
#     datawriter.writerows(contacts_list)
