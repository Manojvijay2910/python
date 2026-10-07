from email.mime.text import MIMEText
import smtplib

body = "This is a test email. How are you?"

msg = MIMEText(body)
msg['From'] = 'abcd@gmail.com'
msg['To'] = 'abcd@gmail.com'
msg['Subject'] = 'test email'

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login('abcd@gmail.com', 'abcdefghijklmnop')
server.send_message(msg)

print("Email sent!")
server.quit()