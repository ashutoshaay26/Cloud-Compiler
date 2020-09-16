import smtplib

from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'cloudcompiler@hotmail.com'
PASSWORD = 'lab@@cc2'

def mail(to,message,subject):
    # set up the SMTP server
    s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email:
    #msg = MIMEMultipart()       # create a message

    # message = "Click on the following link to activate your account..! \n"
    # link = "http://localhost:8080/" + category + "?email=" + to + "&id=" + id
    # message = message + link
    msg = MIMEText(message, 'plain')
    # Prints out the message body for our sake
    print(message)

    # setup the parameters of the message
    msg['From'] = MY_ADDRESS
    msg['To'] = to
    msg['Subject'] = subject
    #subject = "Activate Your Account"

    # add in the message body
    #msg.attach(MIMEText(message, 'plain'))
        
    # send the message via the server set up earlier.
    s.sendmail(MY_ADDRESS,to,msg.as_string())
        
    # Terminate the SMTP session and close the connection
    s.quit()