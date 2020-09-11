import os
from twilio.rest import Client

account_sid = 'AC81d02d97609670a76e77016ea477f7ff'
auth_token = 'b9fb20b0ccb287245339ba09a7ad67fd'

client = Client(account_sid, auth_token)

from_whatsapp_number = 'whatsapp:+14155238886'
to_whatsapp_number = 'whatsapp:' + os.environ['MY_PHONE_NUMBER']

message = client.messages.create(
    body='How you doin!',
    from_=from_whatsapp_number,
    to=to_whatsapp_number
)

print(message.sid)
