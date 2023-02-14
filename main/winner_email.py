import smtplib, ssl
import os


def send_winner_email(winner_email):
    print("sending email to "+winner_email)
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    sender_email = os.getenv("EMAIL_ADDRESS")
    cc = [os.getenv("ADMIN_EMAIL")]
    receiver_email = [winner_email]
    password = os.getenv("EMAIL_PASSWORD")

    message = """
    Personal Data Powerball Winner

    Congratulations on winning the personal data powerball.

    Please respond all to this email with your full name and further instructions to acsess your data will be sent.
    """

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        toaddrs = [receiver_email] + cc
        server.login(sender_email, password)
        server.sendmail(sender_email, toaddrs, message)