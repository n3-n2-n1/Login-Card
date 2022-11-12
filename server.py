from email.mime.nonmultipart import MIMENonMultipart
from flask import Flask, render_template, request, make_response
from werkzeug.datastructures import ImmutableDict

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


app = Flask(__name__)

HOST_NAME = "localhost"
HOST_PORT = 80
MAIL_FROM = "sys@site.com"
MAIL_TO = "admin@site.com"
MAIL_SUBJECT = "Booking Request"

@app.route("/")

def index():
    return render_template("form.html")

@app.route("/thank")

def thank():
    return render_template("thank.html")



@app.route("/book", methods=["POST"])

def book():

    mail = MIMENonMultipart("alternative")
    mail["Subjetct"] = MAIL_SUBJECT
    mail["From"] = MAIL_FROM
    mail["To"] = MAIL_TO
    
    data = dict(request.form)
    msg = "<html><head></head><body>"
    
    for key, value in data.items():
        msg += key + ":" + value + "<br>"
        msg += "</body><html>"
        mail.attach(MIMEText(msg, "html"))


        mailer = smtplib.SMTP("localhost")
        mailer.sendmail(MAIL_FROM, MAIL_TO, mail.as_string())
        mailer.quit()

        res = make_response("OK", 200)
        return res


if __name__ == "__main__":
  app.run(HOST_NAME, HOST_PORT)