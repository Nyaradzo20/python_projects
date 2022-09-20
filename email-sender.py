from email.message import EmailMessage
import smtplib
import ssl
email_sender ='nchinyati@gmail.com'
email_pswd = 'acfossrrayzmedcz'
email_receiver = 'nyaradzochinyati3@gmail.com'

subject = "hewllo world"
body  ="python is fun"

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content = (body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender,email_pswd)
    smtp.sendmail(email_sender, email_receiver, em.as_string)
