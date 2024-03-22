import smtplib

def send_email(to_address, message_body):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)  # Use a secure password storage mechanism
    server.sendmail("sender_email", to_address, message_body)
    server.close()

# Example usage:
to = "recipient@example.com"  # Replace with the actual recipient email address
message = "This is the message to be sent."
send_email(to, message)
