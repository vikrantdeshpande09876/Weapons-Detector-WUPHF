import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders



def send_email(sender_email, sender_password, receiver_email, body, attachment_filename=None, SMTP_SERVER='smtp.office365.com', SMTP_PORT=587):
    """Sends an automated email to the desired receiver from my personal email address.
    Also supports sending across an attachment if I manage to include the image as part of the Kafka-topic message body.

    Args:
        sender_email (str): Email address of the sender account.
        sender_password (str): Password of the sender account.
        receiver_email (str): Authorities/Admins to be notified.
        body (str): Message body that indicates the weapons detected in current situation.
        attachment_filename (str, optional): Maybe even include a screenshot in the message body. Defaults to None.
        SMTP_SERVER (str, optional): Defaults to 'smtp.office365.com' for Outlook.
        SMTP_PORT (int, optional): Defaults to 587 for Outlook.
    """
    curr_timestamp = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
    subject = f'REPORT UPDATE: {curr_timestamp}'
    body = f'''
    ALERT! Weapons Detected:
    {body}.

    I intend to include a feature in this email, to enable contacting the police department at the click of a button.

    Peace,
    Vikrant Deshpande.
    '''

    mime_message = MIMEMultipart()
    mime_message['From'] = sender_email
    mime_message['To'] = receiver_email
    mime_message['Subject'] = subject
    mime_message.attach(MIMEText(body, 'plain'))
    if attachment_filename:
        attachment = open(attachment_filename, 'rb')
        part = MIMEBase('application', "octet-stream")
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "attachment; filename= %s" % attachment_filename)
        mime_message.attach(part)

    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(sender_email, sender_password)
    server.send_message(mime_message)
    server.quit()
    print(f'Sent an email successfully!')