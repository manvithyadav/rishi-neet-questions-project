import smtplib
import pandas as pd
import random
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

df = pd.read_csv('neet_pg_qns_2023.csv')

question_num = random.randint(0, len(df) - 1)

with open("neet_answer.txt", "w") as file:
    file.write("correct answer - " + str(df.loc[question_num]['answer']))


sender_email = "supser.respus@gmail.com"
receiver_email = "manvith.dyadav@gmail.com"
password = "lijx hewe noru oppg"

# create the message as multipart if attachments are to be sent
message = MIMEMultipart()

message['Subject'] = f'Test - NEET 2023 Question - {question_num}'
message['From'] = sender_email
message['To'] = receiver_email


# MIMEMultipart doesn't have set_content methof as EmailMessage. We need to create a body and attach it
body = f'''
<!DOCTYPE html>
<html>
    <body>
        <p>
            <b>Q.</b> {df.loc[question_num]['question']}
        </p>
        <ol>
            <li>{df.loc[question_num]['option_1']}</li>
            <li>{df.loc[question_num]['option_2']}</li>
            <li>{df.loc[question_num]['option_3']}</li>
            <li>{df.loc[question_num]['option_4']}</li>
        </ol>

        <hr>

        <p>
            send a reply in the below form<br>
            <b>correct answer: [your option]</b><br>
            <b>explanation: [your explanation]</b>
        </p>

        <hr>
    </body>
</html>
'''

message.attach(MIMEText(body, 'html')) 


# filename = "neet_answer.txt"
# attachment = open("./neet_answer.txt", "rb")

# attachment_instance = MIMEBase('application', 'octet-stream') 
# attachment_instance.set_payload((attachment).read())
# encoders.encode_base64(attachment_instance)
# attachment_instance.add_header('Content-Disposition', "attachment; filename= %s" % filename)
# message.attach(attachment_instance)


s = smtplib.SMTP('smtp.gmail.com', 587)
print(f'created SMTP session')
s.starttls()
print(f'started TLS for security')
s.login(sender_email, "lijx hewe noru oppg")
print(f'authenticated')
s.sendmail(sender_email, receiver_email, message.as_string())
print(f'mail sent')
s.quit()
print(f'terminated the session')