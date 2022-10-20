import requests

def lambda_handler(event, context):
   TOKEN = 'トークン'
   CHANNEL = 'チャンネル名'
   
   url = "https://slack.com/api/chat.postMessage"
   headers = {"Authorization": "Bearer "+TOKEN}
   data  = {
      'channel': CHANNEL,
      'text': 'もくもく会は本日19時~21時で実施されます'
   }
   r = requests.post(url, headers=headers, data=data)
   print("return ", r.json())
   return True
