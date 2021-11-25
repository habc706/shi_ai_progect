'''
此文件用于编写其他接口时进行测试
'''

import os
from rest_framework.views import APIView
from rest_framework.response import Response
import asyncio
import websockets
import time

def get_time(couse_id):
    return 'C:\\Users\\Lenovo\\Desktop\\01\\'+couse_id+'\\'

url = 'ws://ise-api.xfyun.cn'
result = {

}

# async def get_ai_score(content,text):





class tes(APIView):
    def post(self,request,*args,**kwargs):
        #file = request.data.get('')
        cou_id = request.data.get('cou_id')
        files = request.FILES
        text = request.data.get('Text')
        content = files.get('luyingfile').read()  #  这个就是上传mp3的二进制内容
        path = get_time(cou_id)

        appid = 'wx09236611cba1fa77'
        appscret = '0431676f306f490f7e74447f429c0ba4'
        with websockets.connect(url) as websocket:
            while True:
                websocket.send(
                    {'AudioFile': content, 'Text': text, 'APPID': appid, 'APISecret': '', 'APISecret0': ''})

                result2 =  websocket.recv()
                print(result2.data.data)
                print(result2)

        # loop = asyncio.get_event_loop()
        # task = [get_ai_score(content,text)]
        # loop.run_until_complete(asyncio.wait(task))
        return Response({
            'errmesg':'ok'
        })
        loop.close()
        # try:
        #     get_ai_score(content,text)
        #     try:
        #         if not os.path.exists(path):
        #             os.makedirs(path)
        #         with open(path + str(time.mktime(time.localtime())) + '.mp3', 'wb') as e:
        #             e.write(content)
        #         return Response({
        #             'messg': 'ok',
        #             'data': result.data
        #         })
        #
        #     except:
        #         return Response({
        #             'messg': 'score ok but storage error happen',
        #             'data': result.data
        #         })
        #
        #
        # except:  # 获取分数失败
        #
        #     try:
        #         if not os.path.exists(path):
        #             os.makedirs(path)
        #         with open(path + str(time.mktime(time.localtime())) + '.mp3', 'wb') as e:
        #             e.write(content)
        #         return Response({
        #             'messg': 'storage ok but score error happen',
        #             'data': result.data
        #         })
        #
        #     except:
        #         return Response({
        #             'messg': 'storage error happen and score error happen',
        #             'data': result.data
        #         })







