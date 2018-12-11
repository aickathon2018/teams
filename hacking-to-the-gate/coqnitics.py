import requests 
import json
import os

def requestAPI(id):
  file = '{}{}{}'.format('tmp/train', id,'.jpg')
  url = "https://fashion.recoqnitics.com/analyze"
  accessKey = "e3bedbcee735461c8e99"
  secretKey = "d5c151a04d1de54941aad8a9ad11721b96b06c3d"

  # access_key and secret_key
  data = {'access_key': accessKey,
    'secret_key': secretKey}

  filename = {'filename': open(file,'rb')}
  r = requests.post(url, files = filename, data=data)
  content = json.loads(r.content)
  return content