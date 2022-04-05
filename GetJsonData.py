import json

#>> 파일명 얻기
filename = "slack_token.json"
    
# >> 파일읽기
with open(filename, "r") as fp:
    token = json.load(fp)
        
# >> auth key return
print(token['myToken'])
