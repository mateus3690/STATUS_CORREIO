import smtplib
from email.mime.text import MIMEText


class ProcessaSMTP:
    
    def __init__(self, configuraDeEnvio, codigo, msg):
        self.configuraDeEnvio = configuraDeEnvio
        self.codigo = codigo
        self.msg = msg
    
        self._boot()
        
    def _boot(self):
        
        mensagem = MIMEText(self.msg)
        mensagem['From'] = self.configuraDeEnvio['mail_from_adress']
        mensagem['To'] = self.configuraDeEnvio['destinatario_email']
        mensagem['Subject'] = f"STATUS CORREIO: {self.codigo}"

        try:
            with smtplib.SMTP(self.configuraDeEnvio['mail_host'], self.configuraDeEnvio['mail_port']) as server:
                server.starttls()
                server.login(self.configuraDeEnvio['mail_username'], self.configuraDeEnvio['mail_password'])
                server.sendmail(self.configuraDeEnvio['mail_from_adress'], self.configuraDeEnvio['destinatario_email'], mensagem.as_string())
            print('E-mail enviado com sucesso!')
        except Exception as e:
            print('Erro ao enviar o e-mail:', e)
   