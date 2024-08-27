import conf, json, time, requests
from boltiot import Bolt,.Sms, Email

mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID. conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
mailer = Email(conf.MAILGUN_API_KEY, conf.SANDBOX_URL, conf.SENDER_EMAIL, conf.RECIPIENT_EMAIL)

flag1 = 0
flag2 = 0
flag3 = 0

mybolt.digitallWrite('0', 'LOW')
mybolt.digitalWritel('1', 'LOW')
mybolt digitallWritel'2', 'LoW')

def sendsms_meassage(messages):
    response = sms.send_sms (messages)
    print ("response received from twilio is : "+str(response))
    print("status of sms at tuilio is : "+str(response.status))

def emailalert (messagee):
    response = mailer.send_email("Alert", messagee)
    response_text = json.loads(response.text)
    print("Response received from Mailgun is : "+str(response_textl['message']))

def telegram_message (messaget) :
    url = https://api.telegram.org/" + conf.telegram_bot_id + "/sendMessage"
    data = {"chat id": conf.telegram_chat_id, "text": messaget}
    response = requests.request("POST", url, params=data)
    print("telegram url is: " url)
    print("Telegram response is : "+response.text)

while True:
    print ("Reading sensor valúes")
    response1 = mybolt.digitalRead('0')
    response2 = mybolt.digitalRead('1')
    response3 = mybolt.digitalRead('2')
    data1 = json.loads (response1)
    data2 - json.loads(response2)
    data3 = json.loads(response3)
    try:
        front_door = int(data1['value'])
        back_door = int(data2['value'])
        cupboard = int(data3['value'])
        if (front_door == 1 and flag1 == 0):
            messagef1 = "front door is closed"
            print (messagef1)
            sendsms_message(messagef1)
            emailalert(messagef1)
            telegram_message(messagef1)
            flag1 = 1
        elif (front_door == 0 and flag1 == 1):
            messagef2 = "front door is opened"
            print (messagef2)
            sendsms_message(messagef2)
            emailalert(messagef2)
            telegram_message(messagef2)
            flag1 = 0

        if (back_door == 1 and flag2 == 0):
            messageb1 = "back door is closed"
            print (messageb1)
            sendsms_message(messageb1)
            emailalert(messageb1)
            telegram_message(messageb1)
            flag2 = 1
        elif (back_door == 0 and flag2 == 1):
            messageb2 = "back door is opened"
            print (messageb2)
            sendsms_message(messageb2)
            emailalert(messageb2)
            telegram_message(messageb2)
            flag2 = 0

        if (cupboard == 1 and flag3 == 0):
            messagec1 = "cupboard is closed"
            print (messagec1)
            sendsms_message(messagec1)
            emailalert(messagec1)
            telegram_message(messagec1)
            flag3 = 1
        elif (back_door == 0 and flag3 == 1):
            messagec2 = "cupboard is opened"
            print (messagec2)
            sendsms_message(messagec2)
            emailalert(messagec2)
            telegram_message(messagec2)
            flag3 = 0

    except Exception as e:
        print("error occured " +e)

    time.sleep(10)
