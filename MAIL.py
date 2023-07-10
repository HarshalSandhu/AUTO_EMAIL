"""This python code is used to send mail from my email to different email address with proper subject,body and even a pdf attached to it."""
"""This email can be sent through command prompt without even opening the Gmail"""
"""All it require is an internet connection"""
"""importing the neccessay libraries"""
#-------------------------------------------------------#

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#-------------------------------------------------------#


# the following is the port and server details which aid in sending emails
smtp_port = 587
smtp_server = "smtp.gmail.com"

#The line bellow is used to accept the Subject from the user
subject = input("Please enter the subject: ")
email_from = "sandhuharshal1@gmail.com"

#the line below accepts the list of emails to whom the user widhes to send the email
email_to = list(map(str, input("Enter the receiver's email: ").split()))

#this is the passsword which is genrated randonly by the mail using app passwords which allows u to send email without logging in the credentials
pswd = "ivtrjizafeiqqcwe"


#the following function is used to send the mail. it accepts the list of recevers and then sends the mail one by one asking for the body/message in the email individually
def send_mails(email_to):
    #running loop to run through all the persons in the list
    for person in email_to:
        #this line accepts the input message fromt he user
        body = input(f"Enter the message for {person}: ")
        #This line creates an instance of the MIMEMultipart class, which represents a multipart email message.
        msg = MIMEMultipart()
        
        # This line sets the "From" field of the email message to the value stored in the variable email_from.
        msg["From"] = email_from
        
        #similarly this store the adrress to of the receiver
        msg["To"] = person
        
        #this line stores the Subject in the variable Subjet of instance of the MIMEMultipart class
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        #----------------------------------------------------------------------#
        #the following part is used to attach pdf to the mail
        with open("D:/DSA/PROJECT/hs.pdf", "rb") as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            "attachment; filename=hs.pdf"
        )
        msg.attach(part)
        text = msg.as_string()
        #----------------------------------------------------------------------#

        print("Connecting to server...")
        TIE_server = smtplib.SMTP(smtp_server, smtp_port)
        TIE_server.starttls()
        # Login to your email account
        TIE_server.login(email_from, pswd)
        print("Successfully connected to the server.")
        TIE_server.sendmail(email_from, person, text)
        print(f"Email sent successfully to {person}")
        print()
        print()
        TIE_server.quit()
        


# Run the function
send_mails(email_to)