import smtplib
from email.mime.text import MIMEText


def sendMail(content, to, from1, subject):
    msg = MIMEText(content, 'html')
    msg['To'] = to
    msg['Subject'] = subject
    msg['From'] = from1

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(from1, "8435057182")
    server.send_message(msg)
    server.close()


rEmail = input("Enter receiver mail : ")
sEmail = input("Enter sender mail : ")
subject = input("Enter the subject : ")
content = input("Enter the content : ")

sendMail(content, rEmail, sEmail, subject)
