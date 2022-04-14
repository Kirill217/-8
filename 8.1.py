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
dict_username_domain = {}

def correct_email(email):
    pattern = r'^[a-z,A-Z,0-9,\.,\_,\-]+@[a-z]+\.[a-z]+$'
    # pattern_2 = r'^[a-z,A-Z,0-9,\.,\_,\-]+$'
    # pattern_3 = r'^@+[a-z,A-Z,0-9,\.,\_,\-]+$'
    name_email = re.compile(pattern)
    # username = re.compile(pattern_2)
    # domsin = re.compile(pattern_3)
    if name_email.match(email) is None:
        # raise ValueError
        msg = f'wrong email {email}'
        raise ValueError(msg)
        # print(f'ValueError: wrong email: {email}')
        # raise ValueError(msg)
        # msg = f'Error {email}'
    else:
        username = email.partition('@')[0]
        # print(username)
        domain = email[email.find("@") + 1:]
        # print(domain)
        dict_username_domain['username'] = username
        dict_username_domain['domain'] = domain
        print(dict_username_domain)
        # username.match(email)
        # domsin.match(email)
        # print(email)

        # print('Ваш email:', email)

    return


correct_email('kirill217sulimov@gmail.com')
correct_email('kirill-sulimov@gmail.com')
correct_email('_irill.sulimov@gmail.com')
# correct_email('kirill217sulimov@gma!l.com')
# correct_email('kiril1sulimov@gmail.com')
# correct_email('kirill217sulimov@gmailcom')
correct_email('kirill217sulimov@gmail.c0m')
# correct_email('kirill-sulimov@gmail.com')
