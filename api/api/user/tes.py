from database.models import wuser_info
from database.models import course
from database.models import courese_selected
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class tes(APIView):
    def post(self,request,*args,**kwargs):

        class qunima:
            def __init__(self,a):
                self.a=a

            def say(self):
                print(self.a)

        oj = qunima('okelael')
        oj.say()

        data={}
        data['oj']=oj.a
        data['ojbk'] = 'qnmd'
        return Response({
            'mess':'qnmdwqok',
            'data':data
        })