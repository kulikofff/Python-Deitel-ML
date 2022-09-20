import pandas as pd

#Series (одномерная) и DataFrames (двумерная).
zips = pd.Series({'Boston': '02215', 'Miami': '3310'})
print(zips)
print(zips.str.match(r'\d{5}'))

cities = pd.Series(['Boston, MA 02215', 'Miami, FL 33101'])
print(cities.str.contains(r' [A-Z]{2} '))
print(cities.str.match(r' [A-Z]{2} '))

contacts = [['Mike Green', 'demo1@deitel.com', '5555555555'],
           ['Sue Brown', 'demo2@deitel.com', '5555551234']]

contactsdf = pd.DataFrame(contacts, 
                          columns=['Name', 'Email', 'Phone'])
#Преобразование формата номера
import re

def get_formatted_phone(value):
    result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', value)
    return '-'.join(result.groups()) if result else value

formatted_phone = contactsdf['Phone'].map(get_formatted_phone)
print(formatted_phone)

contactsdf['Phone'] = formatted_phone
print(contactsdf)