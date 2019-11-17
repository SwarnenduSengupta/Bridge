import smtplib
from email.mime.text import MIMEText

smtp_ssl_host = 'smtp.gmail.com'
smtp_ssl_port = 465
username = 'myhousedankuni2019@gmail.com'
password = 'Delight@2995@'
sender = 'myhousedankuni@gmail.com'
targets = ['swarnendu.sengupta@yahoo.com']

msg = MIMEText('Hi, how are you today?')
msg['Subject'] = 'Hello'
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()

##https://www.geeksforgeeks.org/send-mail-attachment-gmail-account-using-python/
