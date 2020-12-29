import json
import imaplib
import email

# json has to contain "mail":"examplEmail@yourMailProvider.smth" and "password":"yourPassword"
with open("data.json") as jsonFile:
    credentials = json.load(jsonFile)
    jsonFile.close()

try:
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(credentials["mail"], credentials["password"])
    mail.select("inbox")
    data = mail.search(None, "ALL")
    mailIds = data[1]
    idList = mailIds[0].split()
    latestEmailId = int(idList[-1])

    for i in range(latestEmailId, latestEmailId - 10, -1):
        data = mail.fetch(str(i), "(RFC822)")
        for responsePart in data:
            arr = responsePart[0]
            if isinstance(arr, tuple):
                msg = email.message_from_string(str(arr[1], "utf-8"))
                print("From: " + str(msg["from"] + "\n" +
                                     "Subject: " + str(msg["subject"] + "\n\n")))


except Exception as e:
    print(str(e))
