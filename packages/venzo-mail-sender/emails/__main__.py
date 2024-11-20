from http import HTTPStatus
import os
from mailersend import emails


def main(args):
    """
    The function sends an email using the MailerSend API key and provided email details.

    :param args: Dictionary containing the required email details:
                 - from_email: Sender's email address
                 - from_name: Sender's name
                 - to_email: Recipient's email address
                 - subject: Email subject
                 - content: Email content (HTML format)
    :return: Dictionary containing "statusCode" and "body" indicating the result.
    """
    key = os.environ.get("MAILER_SEND_API_KEY")
    if not key:
        return {
            "statusCode": HTTPStatus.INTERNAL_SERVER_ERROR,
            "body": "API key is missing",
        }

    from_email = args.get("from_email")
    from_name = args.get("from_name", "")
    to_email = args.get("to_email")
    user_subject = args.get("subject")
    content = args.get("content")

    # Validate required parameters
    if not from_email:
        return {
            "statusCode": HTTPStatus.BAD_REQUEST,
            "body": "Sender email is required",
        }
    if not to_email:
        return {
            "statusCode": HTTPStatus.BAD_REQUEST,
            "body": "Recipient email is required",
        }
    if not user_subject:
        return {
            "statusCode": HTTPStatus.BAD_REQUEST,
            "body": "Email subject is required",
        }
    if not content:
        return {
            "statusCode": HTTPStatus.BAD_REQUEST,
            "body": "Email content is required",
        }

    try:
        # Initialize the MailerSend client
        mailer = emails.NewEmail(key)

        # Construct the email message
        message_body = {}
        mail_from = {"name": from_name, "email": from_email}
        recipients = [{"name": "Recipient", "email": to_email}]

        mailer.set_mail_from(mail_from, message_body)
        mailer.set_mail_to(recipients, message_body)
        mailer.set_subject(user_subject, message_body)
        mailer.set_html_content(content, message_body)

        # Send the email
        mailer.send(message_body)

        return {"statusCode": HTTPStatus.ACCEPTED, "body": "Email sent successfully"}
    except Exception as e:
        return {"statusCode": HTTPStatus.INTERNAL_SERVER_ERROR, "body": str(e)}
