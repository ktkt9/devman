import os
import smtplib
from dotenv import load_dotenv
mail = '''Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.'''


load_dotenv()

my_mail = os.getenv("Login")
password=os.getenv("Password")
site='https://dvmn.org/profession-ref-program/yakirussshha/OtXag/'
my_name='Кирилл'
recipient_name='Артём'
mail=mail.replace('%website%',site)
mail=mail.replace('%friend_name%',recipient_name)
mail=mail.replace('%my_name%',my_name)
recipient_mail = 'kirilltimoffev@gmail.com'
letter = \
 '''From: {}
To: {}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";
{}'''.format(my_mail,recipient_mail,mail)
letter = letter.encode("UTF-8")
server = smtplib.SMTP_SSL('smtp.yandex.ru', 465) 
server.login(my_mail,password)
server.sendmail(my_mail, my_mail, letter)
server.quit()
