import smtplib, ssl
from getpass import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


context = ssl.create_default_context()
sender_email = "thetonykano.do.not.reply@gmail.com"
password = getpass("Please enter your password: ")
smtp_server = "smtp.gmail.com"
receiver_email = 'prettyfosie@yahoo.com'
subject = "Hey Guys! Guess what happened?"

message = MIMEMultipart("alternative")
message["Subject"] = subject
message["From"] = sender_email
message["To"] = receiver_email
# Create the plain-text and HTML version of your message
text = """\
Hi,

How are you?

Sincerely,
TheTonyKano
Twitch: twitch.tv/TheTonyKano
"""

html = """\
<html>
    <body>
        <p>
            Hi,<br><br>
            How are you?<br><br>
            Sincerely,<br>
            TheTonyKano <br>
            Twitch <a href="twitch.tv/TheTonyKano" target="_blank">TheTonyKano</a>
        </p>
    </body>
</html>
"""

# Turn these into plain/html MIMEText objects
part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")




def sslBasedEmail(sender_email, receiver_email, message):
    #  Create a secure SSL context
    sslPort = 465 # for SSL connections
    # Try to log in to server and send email
    server = smtplib.SMTP(smtp_server,sslPort)
    try:
        server.ehlo() # Can be omitted
        server.starttls(context=context) # Secure the connection
        server.ehlo() # Can be omitted
        server.login(sender_email, password)
        # TODO: Send email here
        server.sendmail(sender_email, receiver_email, message)
    except Exception as e:
        # Print any error messages to stdout
        print(e)
    finally:
        server.quit() 


def tlsBasedEmail(sender_email, receiver_email, message):
    tlsPort = 587 # for TLS connections
    server = smtplib.SMTP(smtp_server, tlsPort)
    try:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        print("Email sent successfully.")
    except Exception as e:
        print(e)
        print("Email failed to send.")
    finally:
        server.close()

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
message.attach(part1)
message.attach(part2)

tlsBasedEmail(sender_email, receiver_email, message.as_string())