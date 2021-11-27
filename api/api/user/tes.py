import os
import re
from rest_framework.views import APIView
from rest_framework.response import Response
from builtins import Exception, str, bytes
import websocket
import datetime
import hashlib
import base64
import hmac
import json
from urllib.parse import urlencode
import time
import ssl
from wsgiref.handlers import format_date_time
from datetime import datetime
from time import mktime
import _thread as thread
from database.models import ai_score_storage

#  BusinessArgs参数常量
SUB = "ise"
ENT = "cn_vip"
#中文题型：read_syllable（单字朗读，汉语专有）read_word（词语朗读）read_sentence（句子朗读）read_chapter(篇章朗读)
#英文题型：read_word（词语朗读）read_sentence（句子朗读）read_chapter(篇章朗读)simple_expression（英文情景反应）read_choice（英文选择题）topic（英文自由题）retell（英文复述题）picture_talk（英文看图说话）oral_translation（英文口头翻译）
CATEGORY = "read_chapter"
STATUS_FIRST_FRAME = 0  # 第一帧的标识
STATUS_CONTINUE_FRAME = 1  # 中间帧标识
STATUS_LAST_FRAME = 2  # 最后一帧的标识
def get_time(couse_id):
    return 'C:\\Users\\Lenovo\\Desktop\\01\\'+couse_id+'\\'

class tes(APIView):
    def post(self,request,*args,**kwargs):  # 由于调用ai接口的一些特殊写法，需要把许多类和方法再写进这个post函数里面
        class Ws_Param(object):
            # 初始化
            def __init__(self, APPID, APIKey, APISecret, AudioFile, Text):
                self.APPID = APPID
                self.APIKey = APIKey
                self.APISecret = APISecret
                self.AudioFile = AudioFile
                self.Text = Text
                # 公共参数(common)
                self.CommonArgs = {"app_id": self.APPID}
                # 业务参数(business)，更多个性化参数可在官网查看
                self.BusinessArgs = {"category": CATEGORY, "sub": SUB, "ent": ENT, "cmd": "ssb",
                                     "auf": "audio/L16;rate=16000",
                                     "aue": "lame", "text": self.Text, "ttp_skip": True, "aus": 1}
                self.final_data = ''


            def create_url(self):
                # wws请求对Python版本有要求，py3.7可以正常访问，如果py版本请求wss不通，可以换成ws请求，或者更换py版本
                url = 'ws://ise-api.xfyun.cn/v2/open-ise'
                # 生成RFC1123格式的时间戳
                now = datetime.now()
                date = format_date_time(mktime(now.timetuple()))
                # 拼接字符串
                signature_origin = "host: " + "ise-api.xfyun.cn" + "\n"
                signature_origin += "date: " + date + "\n"
                signature_origin += "GET " + "/v2/open-ise " + "HTTP/1.1"
                # 进行hmac-sha256进行加密
                signature_sha = hmac.new(self.APISecret.encode('utf-8'), signature_origin.encode('utf-8'),
                                         digestmod=hashlib.sha256).digest()
                signature_sha = base64.b64encode(signature_sha).decode(encoding='utf-8')
                authorization_origin = "api_key=\"%s\", algorithm=\"%s\", headers=\"%s\", signature=\"%s\"" % (
                    self.APIKey, "hmac-sha256", "host date request-line", signature_sha)
                authorization = base64.b64encode(authorization_origin.encode('utf-8')).decode(encoding='utf-8')
                # 将请求的鉴权参数组合为字典
                v = {
                    "authorization": authorization,
                    "date": date,
                    "host": "ise-api.xfyun.cn"
                }
                # 拼接鉴权参数，生成url
                url = url + '?' + urlencode(v)
                # 此处打印出建立连接时候的url,参考本demo的时候，比对相同参数时生成的url与自己代码生成的url是否一致
                # print("date: ", date)
                # print("v: ", v)
                # print('websocket url :', url)
                return url

         # 收到websocket消息的处理
        def on_message(ws, message):  # ws是该类本身,message是从服务器接收到的数据
            try:
                code = json.loads(message)["code"]
                sid = json.loads(message)["sid"]
                if code != 0:
                    errMsg = json.loads(message)["message"]
                    print("sid:%s call error:%s code is:%s" % (sid, errMsg, code))

                else:
                    data = json.loads(message)["data"]
                    status = data["status"]
                    result = data["data"]
                    if (status == 2):
                        xml = base64.b64decode(result)
                        # python在windows上默认用gbk编码，print时需要做编码转换，mac等其他系统自行调整编码

                        final_data = xml.decode("gbk")

                        wsParam.final_data = final_data




            except Exception as e:
                print("receive msg,but parse exception:", e)

        # 收到websocket错误的处理
        def on_error(ws, error):
            pass

        # 收到websocket关闭的处理
        def on_close(ws):
            pass
        def on_data(ws, str, data_type, continue_type):  # data是从服务器接收到的字符串
            pass
            print(str)
            print(data)

            print(data_type)
            print(continue_type)
        # 收到websocket连接建立的处理
        def on_open(ws):
            def run(*args):
                frameSize = 1280  # 每一帧的音频大小
                intervel = 0.04  # 发送音频间隔(单位:s)
                status = STATUS_FIRST_FRAME  # 音频的状态信息，标识音频是第一帧，还是中间帧、最后一帧

                with open(wsParam.AudioFile, "rb") as fp:
                    while True:
                        buf = fp.read(frameSize)
                        # 文件结束
                        if not buf:
                            status = STATUS_LAST_FRAME
                        # 第一帧处理
                        # 发送第一帧音频，带business 参数
                        # appid 必须带上，只需第一帧发送
                        if status == STATUS_FIRST_FRAME:
                            d = {"common": wsParam.CommonArgs,
                                 "business": wsParam.BusinessArgs,
                                 "data": {"status": 0}}
                            d = json.dumps(d)
                            ws.send(d)
                            status = STATUS_CONTINUE_FRAME
                        # 中间帧处理
                        elif status == STATUS_CONTINUE_FRAME:
                            d = {"business": {"cmd": "auw", "aus": 2, "aue": "lame"},
                                 "data": {"status": 1, "data": str(base64.b64encode(buf).decode())}}
                            ws.send(json.dumps(d))
                        # 最后一帧处理
                        elif status == STATUS_LAST_FRAME:
                            d = {"business": {"cmd": "auw", "aus": 4, "aue": "lame"},
                                 "data": {"status": 2, "data": str(base64.b64encode(buf).decode())}}
                            ws.send(json.dumps(d))
                            time.sleep(1)
                            break
                        # 模拟音频采样间隔
                        time.sleep(intervel)
                ws.close()

            thread.start_new_thread(run, ())

        cou_id = request.data.get('cou_id')
        test_text = request.data.get('text')
        files = request.FILES
        errmesg = ''
        content = files.get('luyingfile').read()  #  这个就是上传mp3的二进制内容
        path = get_time(cou_id)
        wenjian = path  + str(time.mktime(time.localtime())) + '.mp3'
        data = {}
        try:
            if not os.path.exists(path):
                os.makedirs(path)
            with open(wenjian, 'wb') as e:
                e.write(content)

            errmesg = errmesg + 'file store successfully '
        except Exception:
            errmesg= errmesg+'file store error happen '
        finally:
            try:
                audio_file_path = wenjian

                str0 = test_text
                # 待评测文本 utf8 编码，需要加utf8bom 头
                TEXT = '\uFEFF' + str0
                # 直接从文件读取的方式
                TEXT = '\uFEFF'+ open("cn/read_sentence_cn.txt","r",encoding='utf-8').read()
                # APPID、APISecret、APIKey信息在控制台——语音评测了（流式版）——服务接口认证信息处即可获取
                wsParam = Ws_Param(APPID='42989e8d', APISecret='Yzg4NjMxMTRlOTdhZTYyMTM4MTEyMzJi',
                                   APIKey='2a8365fffbb5d0775c452ad0c41a2cd1',
                                   AudioFile=audio_file_path, Text=TEXT)
                websocket.enableTrace(False)
                wsUrl = wsParam.create_url()
                ws = websocket.WebSocketApp(wsUrl, on_message=on_message, on_error=on_error, on_close=on_close,
                                            on_data=on_data)
                ws.on_open = on_open
                ws.run_forever(sslopt={"cert_reqs": ssl.CERT_NONE})

                str1 = r'<read_chapter(.*?)>'
                real_result = re.findall(str1, wsParam.final_data)
                judge = r'"(.*?)"'
                judge2 = r'(.*?)='
                b = real_result[1].split(' ')[1:]

                for var in b:

                    mid = re.findall(judge2, var)[0]
                    data[mid] = re.findall(judge, var)[0]
                try:
                    ai_score_storage.objects.create(lujing=wenjian, fluency_score=data['fluency_score'],
                                                    phone_score=data['phone_score'], total_score=data['total_score']
                                                    , integrity_score=data['integrity_score'],
                                                    tone_score=data['tone_score'],
                                                    content=data['content'], is_rejected=data['is_rejected'].capitalize()
                                                    )  # 返回的是false python 要的是False!!!!!!!!!!!
                    errmesg+='database ok '
                except Exception as e:  # integrity_score
                    print(e)
                    errmesg+='database error '

                errmesg+=' get ai score successfully '
            except Exception:
                errmesg +=' get ai score error '

            finally:

                return Response({
                    'errmesg': errmesg,
                    'data': data,

                })