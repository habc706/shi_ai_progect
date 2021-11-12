from rest_framework.views import APIView
from rest_framework.response import Response
import requests
class tes(APIView):
    def post(self,request,*args,**kwargs):
        wx_code = request.data.get('code')
        info = {
            "appid": 'wx09236611cba1fa77',
            "secret": '0431676f306f490f7e74447f429c0ba4',
            "js_code": wx_code,
            "grant_type": 'authorization_code'
        }
        result = requests.get(url='https://api.weixin.qq.com/sns/jscode2session', params=info)
        print(result.json())
        return Response({
            'test':'ok'
        })