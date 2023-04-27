from flask import Flask, render_template
import smtplib, ssl

emplacement = "data.txt"

app = Flask(__name__)

@app.route('/')
def alarme():
    f = open(emplacement, "r")
    file = f.readlines()
    
    return render_template('page.html', file=file)
    


# port = 465  # For SSL
# password = "AlerteCoursPython69!"
# context = ssl.create_default_context()

# with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
#     server.login("AlerteCoursPython@gmail.com", password)
#     server.sendmail("AlerteCoursPython@gmail.com", "oquintal33@gmail.com", "penis ")



port = 465  # Port SSL pour Gmail
smtp_server = "smtp.gmail.com"
sender_email = "AlerteCoursPython@gmail.com"  # Adresse e-mail de l'expéditeur
receiver_email = "oquintal33@gmail.com"  # Adresse e-mail du destinataire
password = "nfyrcqapbiwsuwms" # Mot de passe pour se connecter au compte Gmail

message = """Mouvement detecte """

context = ssl.create_default_context() # Crée un contexte SSL sécurisé

with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password) # Se connecter au compte Gmail
    server.sendmail(sender_email, receiver_email, message) # Envoyer l'email
    print("L'e-mail a été envoyé avec succès!")

if __name__ == '__main__':
    app.run()
