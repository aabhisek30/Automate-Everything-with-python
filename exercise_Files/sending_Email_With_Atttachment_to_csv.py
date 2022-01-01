import json
import os
import pandas as pd
import yagmail
import inspect
import time

### setting working directory, loading and initializing important variables
os.chdir("C:/Users/abhi_/Automate_things")
with open('other_Files/important_Info.json', 'r') as f:
        cred = json.load(f)
sender_id = cred['sender_email']
sender_password = cred['app_password']
subject = "Bill for your purchase"
attachment_dir = os.path.join(os.getcwd(),"other_Files")


def generate_attachment(file_name,amount):
    """
    A function to generate attachment to attach to E-mail while sending
    """
    file_path = os.path.join(attachment_dir,file_name)
    with open(file_path,"w") as file:
        file.write(f'you have to pay {amount}')
    return file_path

### creating SMTP object to send the email
yag = yagmail.SMTP(user=sender_id,password=sender_password,smtp_ssl=False)

### reading pandas file for contact info

contact_Info = pd.read_csv("other_Files/contact_info.csv")

## iterating through contact dataframe to send mail with requirement attachment

for index,row in contact_Info.iterrows():
    try:
        receiver_id = row['emailID']
        amount = str(row['amount'])
        name = row['name']
        file_name = f'{receiver_id}.txt'
        file_path = generate_attachment(file_name,amount)
        content = [f'Hi {name} you bill is attached. please check it out',file_path,]
        yag.send(to=receiver_id,subject=subject,contents=content)
        print("Email send")
    except Exception as e:
        print("following exception occured")
        print(e)
