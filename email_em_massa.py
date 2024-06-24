import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, body, recipients):
    smtp_server = 'smtp.office365.com'
    smtp_port = 587
    email_username = 'rafael_hss_studio@hotmail.com'
    email_password = '@fpf2024'  # Use sua senha do Outlook

    # Configuração do servidor SMTP
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Iniciar TLS para segurança

    try:
        server.login(email_username, email_password)
        print("Login bem-sucedido")

        for recipient in recipients:
            # Criação do e-mail
            msg = MIMEMultipart()
            msg['From'] = email_username
            msg['To'] = recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Envio do e-mail
            server.sendmail(email_username, recipient, msg.as_string())
            print(f'E-mail enviado para: {recipient}')

    except smtplib.SMTPAuthenticationError as e:
        print(f'Erro de autenticação: {e}')

    except Exception as e:
        print(f'Ocorreu um erro: {e}')

    finally:
        server.quit()


# Definição dos destinatários, assunto e corpo do e-mail
recipients = [
    'panquecariadorafa@gmail.com',
    'andremerli74@gmail.com',
    'zxhbpg@jmurip.com',
    'pmlxew@veracg.com',
    'cgbvud@lxvhhq.com',
    'carmed@usp.br',
    'caueameni@gmail.com',
    'claudiomsi@hotmail.com',
    'daisyess@gmail.com',
    'daniel.abr@hotmail.com',
    'deuzimarcorreiadesantana@gmail.com',
    'dfqjjd@fettiv.com',
    'diego.gregb@hotmail.com',
    'ucmnyo@afyyrn.com',
    'Edu.itaperuna@gmail.com',
    'edw_drum@hotmail.com',
    'etechy@tre-pr.jus.br',
    'fabiosilvarodolpho@gmail.com',
    'feliperepresentante@yahoo.com.br',
    'fernando.financeiro@Yahoo.com.br',
    'fernandopontes@outlook.com',
    'dlima99@bol.com.br',
    'esvhne@jsnpxh.com',
    'prof.janderfisica@gmail.com',
    'joaomoura.com@gmail.com',
    'jonathan.cassian@gmail.com',
    'jornalismo@jornalmontesclaros.com.br',
    'larissareis@FOLHA.COM.BR',
    'larissahbaldoino@gmail.com',
    'leo_rosato@hotmail.com',
    'lucianolf@hotmail.com',
    'luciano.santos@uol.com.br',
    'lffcosta2@yahoo.com.br',
    'marcio@usp.br',
    'maripitanga@yahoo.com.br',
    'mark357177@hotmail.com',
    'mark3qf527@hotmail.com',
    'mateus@mobilizebrasil.com',
    'derby451@hotmail.com',
    'agvhfb@ulswuo.com',
    'miguel.longman@agu.gov.br',
    'rosazmirian@gmail.com',
    'xsxkvw@tasphd.com',
    'D.souza0609@yahoo.com.br',
    'azzyyj@hhnlqu.com',
    'gwagmp@fsqcjc.com',
    'rede@visaofuturo.org.br',
    'facine.patricia@yahoo.com.br',
    'pramais@yahoo.com.br',
    'paulovalerio@msn.com',
    'uucevh@xsnyvl.com',
    'xgkoto@xmwrjd.com',
    'tzoiow@gflnwi.com',
    'recabarrach@globo.com',
    'renan.flumian@gmail.com',
    'ric.takeda@gmail.com',
    'robertocanavezzi@yahoo.com.br',
    'robertopaivaf@hotmail.com',
    'rogerio.araujo@sindagua.com.br',
    'ronangoncalves@gmail.com',
    'sandro.meireles@gmail.com',
    'ijflmo@nmsvpp.com',
    'thiagoullmann@hotmail.com',
    'tiagojesus@mpf.mp.br',
    'vagnelso@hotmail.com',
    'varibeiro@folha.com.br',
    'gmvaltercps@yahoo.com.br',
    'vgp@vigilantesdagestao.org.br',
    'williamspedro@oi.com.br',
    'ohcbcj@wmbowy.com',
    'caevrb@davueg.com',
    'rmtfjw@hypssv.com',
    'pfgwqp@lcmnlv.com',
    # Adicione mais endereços de e-mail conforme necessário
]

subject = 'Assunto do E-mail em Massa'
body = """
Olá,

"Desvende o segredo para o sucesso em apenas um clique! 💫 Clique aqui para começar sua jornada rumo à transformação pessoal e profissional."

https://fir3.net/qjIN

Atenciosamente,
Seu Nome
"""

# Envio dos e-mails
send_email(subject, body, recipients)
