import smtplib
from email.message import EmailMessage
email = EmailMessage()
email['from'] = 'gowtham'
email['to'] = 'gowthamtadikamalla123@gmail.com'
email['subject'] = 'this mail is from python code'
email.set_content('i am a python coder')
with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('krishnaguna445@gmail.com','Krishna@11')
    smtp.send_message(email)
    print('email send')