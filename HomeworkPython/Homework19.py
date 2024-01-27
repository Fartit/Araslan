
import re


text_user = input("Введите текст для того чтобы найти адрес электронной почты: ")
e_mail = re.findall(r'[.\-\w]+@[.\w]+', text_user)
print(e_mail)
