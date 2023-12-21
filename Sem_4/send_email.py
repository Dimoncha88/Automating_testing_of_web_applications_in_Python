'''
Иметь почту на сайте mail.ru (если ее нет – создать).
В настройках безопасности почтового ящика задать
пароль для внешних приложений.

Написать скрипт, который отправляет по email
отчет о тестах, сформированный pytest.
'''

import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

fromaddr = "dimonch_rus@mail.ru"
toaddr = "dimonch_rus@mail.ru"
mypass = "hPVPniZ7Z6iaMgMA1XwF"
reportname = "report.xml"

msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Привет от питона"

with open(reportname, "rb") as f:
    part = MIMEApplication(f.read(), Name=basename(reportname))
    part['Content - Desposition'] = 'attachment; filename = "%s"' % basename(reportname)
    msg.attach(part)

body = "Это пробное сообщение"
msg.attach(MIMEText(body, 'plain'))

server = smtplib.SMTP_SSL('smpt.mail.ru', 465)
server.login(fromaddr, mypass)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
