import json
import smtplib
import imaplib

with open("data.json") as jsonFile:
    jsonObject = json.load(jsonFile)
    jsonFile.close()

try:
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(jsonObject["mail"], jsonObject["password"])
    mail.select("inbox")

    for i in range(1, 10):
        data = mail.fetch(str(i), "(RFC822)")
        print(str(data) + "\n")


except Exception as e:
    print(str(e))
