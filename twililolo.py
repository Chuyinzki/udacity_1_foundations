from twilio import TwilioRestException
from twilio.rest import TwilioRestClient

account_sid = "AC27707d6a12a9355aa168753087c5ea45"  # Your Account SID from www.twilio.com/console
auth_token = "52a4e1d4eb35cbb79fd488e7281e9ea1"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

try:
    message = client.messages.create(body="You'se a bitch",
                                     to="+17609601612",    # Replace with your phone number
                                     from_="+17605920206") # Replace with your Twilio number
except TwilioRestException as e:
    print(e)
