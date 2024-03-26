import json
import requests

admin_user=[]
global languages,colors,inline_keyboard
inline_keyboard=[[],[],[]]
colors=['#00ff8c','#00ff8c','#003cff','#72fdff']
t_colors=['#ffe4e4','#FFFFFF']
languages=['确定','取消','{\"width\":null,\"height\":null,\"data\":\"{\\\"tag\\\":\\\"column\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"12,7\\\",\\\"gradient\\\":{\\\"colors\\\":[\\\"'+colors[0]+'\\\",\\\"'+colors[1]+'\\\"]},\\\"child\\\":{\\\"tag\\\":\\\"text\\\",\\\"data\\\":\\\"管理员设置成功\\\",\\\"style\\\":{\\\"color\\\":\\\"'+t_colors[1]+'\\\",\\\"fontSize\\\":16,\\\"fontWeight\\\":\\\"medium\\\"}},\\\"backgroundColor\\\":\\\"ddeeff\\\"},{\\\"tag\\\":\\\"container\\\",\\\"child\\\":{\\\"tag\\\":\\\"column\\\",\\\"padding\\\":\\\"12\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"0,0,0,4\\\",\\\"alignment\\\":\\\"-1,0\\\",\\\"child\\\":{\\\"tag\\\":\\\"markdown\\\",\\\"data\\\":\\\"你现在可以控制该机器人了！\\\"}}]},\\\"backgroundColor\\\":\\\"ffffff\\\"}],\\\"crossAxisAlignment\\\":\\\"stretch\\\"}\",\"notification\":null,\"come_from_icon\":null,\"come_from_name\":null,\"template\":null,\"no_seat_toast\":null,\"type\":\"messageCard\"}','{\"width\":null,\"height\":null,\"data\":\"{\\\"tag\\\":\\\"column\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"12,7\\\",\\\"gradient\\\":{\\\"colors\\\":[\\\"'+colors[2]+'\\\",\\\"'+colors[3]+'\\\"]},\\\"child\\\":{\\\"tag\\\":\\\"text\\\",\\\"data\\\":\\\"你已经是管理员了\\\",\\\"style\\\":{\\\"color\\\":\\\"'+t_colors[1]+'\\\",\\\"fontSize\\\":16,\\\"fontWeight\\\":\\\"medium\\\"}},\\\"backgroundColor\\\":\\\"ddeeff\\\"},{\\\"tag\\\":\\\"container\\\",\\\"child\\\":{\\\"tag\\\":\\\"column\\\",\\\"padding\\\":\\\"12\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"0,0,0,4\\\",\\\"alignment\\\":\\\"-1,0\\\",\\\"child\\\":{\\\"tag\\\":\\\"markdown\\\",\\\"data\\\":\\\"你已经是管理员了，直接使用即可\\\"}}]},\\\"backgroundColor\\\":\\\"ffffff\\\"}],\\\"crossAxisAlignment\\\":\\\"stretch\\\"}\",\"notification\":null,\"come_from_icon\":null,\"come_from_name\":null,\"template\":null,\"no_seat_toast\":null,\"type\":\"messageCard\"}','{\"width\":null,\"height\":null,\"data\":\"{\\\"tag\\\":\\\"column\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"12,7\\\",\\\"gradient\\\":{\\\"colors\\\":[\\\"'+colors[2]+'\\\",\\\"'+colors[3]+'\\\"]},\\\"child\\\":{\\\"tag\\\":\\\"text\\\",\\\"data\\\":\\\"帮助信息\\\",\\\"style\\\":{\\\"color\\\":\\\"'+t_colors[1]+'\\\",\\\"fontSize\\\":16,\\\"fontWeight\\\":\\\"medium\\\"}},\\\"backgroundColor\\\":\\\"ddeeff\\\"},{\\\"tag\\\":\\\"container\\\",\\\"child\\\":{\\\"tag\\\":\\\"column\\\",\\\"padding\\\":\\\"12\\\",\\\"children\\\":[{\\\"tag\\\":\\\"container\\\",\\\"padding\\\":\\\"0,0,0,4\\\",\\\"alignment\\\":\\\"-1,0\\\",\\\"child\\\":{\\\"tag\\\":\\\"markdown\\\",\\\"data\\\":\\\">发送控制权限密码获取控制权限  \\\\n**基本指令：**  \\\\n- 添加拓展：add_expand id-拓展id(可选) url-拓展zipurl(可选)  \\\\n- 删除拓展：del_expand 拓展id(可选)  \\\\n- 查看当前拓展：get_expand  \\\\n- 还原配色方案、命令及语言：restore  \\\\n>提示：添加个性化指令拓展后请按照拓展文档使用\\\"}}]},\\\"backgroundColor\\\":\\\"ffffff\\\"}],\\\"crossAxisAlignment\\\":\\\"stretch\\\"}\",\"notification\":null,\"come_from_icon\":null,\"come_from_name\":null,\"template\":null,\"no_seat_toast\":null,\"type\":\"messageCard\"}']
global command
command=['add_expand','del_expand','help','get_expand','restore']

def processing(message={},content=""):
    global admin_user
    if content['text']==password and message['data']["resource_type"]=='friend_chat_stranger':
        if not message['data']['user_id'] in admin_user:
            admin_user.append(message['data']['user_id'])
            url = f"https://a1.fanbook.mobi/api/bot/{token}/sendMessage"
            payload = json.dumps({
            "chat_id": int(message['data']['channel_id']),
            "text": languages[2],
            #"parse_mode": "Fanbook",
            "reply_markup": {
                "inline_keyboard": inline_keyboard[0]
            }
            })
            headers = {
            'Content-Type': 'application/json'
            }
            print('\n[info] POST',url,headers,payload,'\n')
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
        else:
            url = f"https://a1.fanbook.mobi/api/bot/{token}/sendMessage"
            payload = json.dumps({
            "chat_id": int(message['data']['channel_id']),
            "text": languages[3],
            #"parse_mode": "Fanbook",
            "reply_markup": {
                "inline_keyboard": inline_keyboard[1]
            }
            })
            headers = {
            'Content-Type': 'application/json'
            }
            print('\n[info] POST',url,headers,payload,'\n')
            response = requests.request("POST", url, headers=headers, data=payload)
            print(response.text)
    if content['text'] == command[2]:
        url = f"https://a1.fanbook.mobi/api/bot/{token}/sendMessage"
        payload = json.dumps({
        "chat_id": int(message['data']['channel_id']),
        "text": languages[4],
        #"parse_mode": "Fanbook",
        "reply_markup": {
            "inline_keyboard": inline_keyboard[2]
        }
        })
        headers = {
        'Content-Type': 'application/json'
        }
        print('\n[info] POST',url,headers,payload,'\n')
        response = requests.request("POST", url, headers=headers, data=payload)
        print(response.text)
    if content['text'] == command[0]:
        t=content['text']
        t=t.split(' ')
        if len(t)==2:
            if t[1].split('-')[0]=='id':
                
global token
def initialize(token1=''):
    global password,token
    token=token1
    #读取init.json为字典
    with open('init.json', 'r', encoding='utf-8') as f:
        init_dict = json.load(f)
        password=init_dict['password']
    return password