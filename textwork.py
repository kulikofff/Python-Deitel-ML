'''
print(f'{17.489:.2f}')
# Тип представления d форматирует целочисленные значения как строки:
print(f'{10:d}')
# Тип представления c форматирует целочисленный код символа в виде соответствующего символа
print(f'{65:c} {97:c}')
print(f'{"hello":s} {7}')

from decimal import Decimal

print(f'{Decimal("10000000000000000000000000.0"):.3f}')
print(f'{Decimal("10000000000000000000000000.0"):.3e}')
print(f'[{27:10d}]')
print(f'[{3.5:10f}]')
print(f'[{"hello":10}]')
print(f'[{27:<15d}]')
print(f'[{3.5:<15f}]')
print(f'[{"hello":>15}]')
#Центр поля
print(f'[{27:^7d}]')
print(f'[{3.5:^7.1f}]')
print(f'[{"hello":^7}]')
print(f'[{27:+10d}]')
print(f'[{27:+010d}]')
print(f'{27:d}\n{27: d}\n{-27: d}')
print(f'{12345678:,d}')
print(f'{123456.78:,.2f}')
print('{:.2f}'.format(17.489))
print('{} {}'.format('Amanda', 'Cyan'))
print('{0} {0} {1}'.format('Happy', 'Birthday'))
print('{last} {first}'.format(first='Amanda', last='Gray'))
s1 = 'happy'
s2 = 'birthday'
s1 += ' ' + s2
print(s1)
sentence = '\t \n This is a test string. \t\t \n'
print(sentence.strip(), sentence.lstrip(), sentence.rstrip(), 'happy birthday'.capitalize(), 'strings: a deeper look'.title(), (f'A: {ord("A")}; a: {ord("a")}'))
sentence = 'to be or not to be that is the question'
print(sentence.count('to'), sentence.count('to', 12), sentence.count('that', 12, 25), sentence.index('be'), sentence.rindex('be'), ('that' in sentence), sentence.startswith('to'), sentence.endswith('question'))
values = '1\t2\t3\t4\t5'
print(values.replace('\t', ','))
#Разбиение строк
letters = 'A, B, C, D'
print(letters.split(', '))
print(letters.split(', ', 2))
letters_list = ['A', 'B', 'C', 'D']
print(','.join(letters_list))
print(','.join([str(i) for i in range(10)]))
print('Amanda: 89, 97, 92'.partition(': '))
url = 'http://www.deitel.com/books/PyCDS/table_of_contents.html'
rest_of_url, separator, document = url.rpartition('/')
print(rest_of_url, separator, document)
print('-27'.isdigit())
print('123 Main Street'.isalnum())
#Необработанные строки - например, для пути каталогов Windows
file_path = r'C:\MyFolder\MySubFolder\MyFile.txt'
print(file_path)
'''
#Регулярные выражения
import re
pattern = '02215'
print('Match' if re.fullmatch(pattern, '022215') else 'No match')
print('Valid' if re.fullmatch(r'\d{5}', '022215') else 'Invalid')
print('Valid' if re.fullmatch('[A-Z][a-z]*', 'Wally') else 'Invalid')
print('Match' if re.fullmatch('[^a-z]', 'a') else 'No match')
print('Match' if re.fullmatch('[*+$]', '!') else 'No match')
print('Valid' if re.fullmatch('[A-Z][a-z]+', 'E') else 'Invalid')
print('Match' if re.fullmatch('labell?ed', 'labellled') else 'No match')
print('Match' if re.fullmatch(r'\d{3,}', '12') else 'No match')
print('Match' if re.fullmatch(r'\d{3,6}', '1234567') else 'No match')
print(re.sub(r'\t', ', ', '1\t2\t3\t4'))
print(re.sub(r'\t', ', ', '1\t2\t3\t4', count=2))
print(re.split(r',\s*', '1, 2, 3,4, 5,6,7,8'))
print(re.split(r',\s*', '1, 2, 3,4, 5,6,7,8', maxsplit=3))
result = re.search('Python', 'Python is fun')
print(result.group() if result else 'not found')
#Без учета регистра
result3 = re.search('Sam', 'SAM WHITE', flags=re.IGNORECASE)
print(result3.group() if result3 else 'not found')
result4 = re.search('^Python', 'Python is fun')
print(result.group() if result else 'not found')
result5 = re.search('Python$', 'Python is fun')
print(result.group() if result else 'not found')

contact = 'Wally White, Home: 555-555-1234, Work: 555-555-4321'
print(re.findall(r'\d{3}-\d{3}-\d{4}', contact))

for phone in re.finditer(r'\d{3}-\d{3}-\d{4}', contact):
    print(phone.group())

text = 'Charlie Cyan, e-mail: demo1@deitel.com'
pattern = r'([A-Z][a-z]+ [A-Z][a-z]+), e-mail: (\w+@\w+\.\w{3})'
result = re.search(pattern, text)
print(result)
print(result.groups())
print(result.group())
print(result.group(1))