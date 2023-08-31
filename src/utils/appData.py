from dotenv import load_dotenv
import os

load_dotenv()

def appData():
    return {
        "loginSentry" : {
            'login': os.getenv("LOGIN_SENTRY"), 
            'password': os.getenv("PASSWORD_SENTRY")
        },
        "url": os.getenv("URL"),
        "smtp": {
            "mail_host":  os.getenv("MAIL_HOST"),
            "mail_port": 587,
            "mail_username":  os.getenv("MAIL_USERNAME"),
            "mail_password":  os.getenv("MAIL_PASSWORD"),
            "mail_from_adress":  os.getenv("MAIL_FROM_ADDRESS"),
            "destinatario_email": os.getenv("DESTINATARIO_EMAIL")
        }
    }
