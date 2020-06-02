import smtplib 
import socket 

def send(server='smtp-mail.outlook', port='587', msg):
    # contain following in try-except in case of momentary network errors 
    try:
        #initialise connection to emain server , the default is outlook 
        smtp = smtplib.SMTP(server, port)
        # this is the 'Extended Hello' command, essentially greeting our SMTP or ESMTP server 
        smtp.ehlo()
        # this is the 'Start Transport Layer Security' command, tells the server we will 
        #be communicating with TLS encryption 
        smtp.starttls()

        #read email and password from file 
        with open('../data/email.txt', 'r') as fp:
            email = fp.read()
        with open('../data/password.txt', 'r') as fp:
            pwd = fp.read()

        # login to outlook server 
        smtp.login(email, pwd)
        #send notification to self 
        smtp.sendmail(email, destination_address, msg.as_string())
        #disconnect from the server 
        smtp.quit()
    except socket.gaierror:
        print("Network connection error, email not sent. ")