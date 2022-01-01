import json
import os
import yagmail
import inspect
import time
os.chdir("C:/Users/abhi_/Automate_things")
with open('other_Files/important_Info.json', 'r') as f:
        cred = json.load(f)
sender_id = cred['sender_email']
sender_password = cred['app_password']
receiver_id = cred['sender_email']        # for simplicity using same address as sender and receiver
subject = "First email by automation"
content = """Hi how are you"""
### creating SMTP object to send the email
yag = yagmail.SMTP(user=sender_id,password=sender_password,smtp_ssl=False)
while True:
    try:
        yag.send(to=receiver_id,subject=subject,contents=content)
        print("Email send")
        time.sleep(60)
    except Exception as e:
        print("following exception occured")
        print(e)
