import os
import requests
import json
import datetime

appID = os.environ.get("APP_ID")
appSecret = os.environ.get("APP_SECRET")
openId = os.environ.get("OPEN_ID")
template_id = os.environ.get("MESSAGE_ID")

def get_access_token():
    url = f'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appID.strip()}&secret={appSecret.strip()}'
    response = requests.get(url).json()
    print("获取token响应:", response)
    return response.get('access_token')

def send_sign_success(access_token):
    now = datetime.datetime.now()
    time_str = now.strftime("%Y年%m月%d日 %H:%M:%S")
    
    # 检查变量
    print(f"OPEN_ID: {openId}")
    print(f"TEMPLATE_ID: {template_id}")
    
    body = {
        "touser": openId.strip(),
        "template_id": template_id.strip(),
        "url": "https://weixin.qq.com",
        "data": {
            "time": {"value": time_str},
            "status": {"value": "签到成功"},
            "remark": {"value": "祝您今天工作愉快！"}
        }
    }
    
    # 打印请求
    print("\n请求数据:")
    print(json.dumps(body, ensure_ascii=False, indent=2))
    
    url = f'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={access_token}'
    response = requests.post(url, json.dumps(body))
    
    print("\n响应数据:")
    print(response.text)

if __name__ == '__main__':
    access_token = get_access_token()
    if access_token:
        send_sign_success(access_token)
    else:
        print("获取access_token失败")