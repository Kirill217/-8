import re
# pattern = r'^[a-z,A-Z,0-9,\.,\_]+@[a-z]+\.[a-z]+'

# RE_NAME = re.compile(pattern)
# email_name = input('Введите email:' )
# print(RE_NAME.match('Kirillkaya@mail.ru'))
# print(RE_NAME.match('Kirillkayamail.ru'))
# print(RE_NAME.match('Kirillkaya@mailru'))
# print(RE_NAME.match('Kirill217kaya@mail.ru'))
# print(RE_NAME.match(email_name))

# name_email = input('Введите email: ')

def correct_email(email):
    pattern = r'^[a-z,A-Z,0-9,\.,\_]+@[a-z]+\.[a-z]+$'
    RE_NAME = re.compile(pattern)
    if RE_NAME.match(email) is None:
        print('ValueError: wrong email:', email)
    else:
        print('Ваш email:', email)

    return

correct_email('kirill217sulimov@gmail.com')
correct_email('kirill/sulimov@gmail.com')
correct_email('кirill.sulimov@gmail.com')
correct_email('kirill217sulimov@gma!l.com')
correct_email('kiril1sulimov@gmail.com')
correct_email('kirill217sulimov@gmailcom')
correct_email('kirill217sulimov@gmail.c0m')
