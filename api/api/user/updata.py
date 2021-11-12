from database.models import wuser_info
from database.models import course
from database.models import courese_selected
from rest_framework.views import APIView
from rest_framework.response import Response
import requests


'''
接收的参数，，openid,role
'''
class updata(APIView):
    def post(self,request,*args,**kwargs):

        open_id = request.data.get('openid')
        role = request.data.get('role')

        if role == '1':  #学生刷新

            pass
        else:  #老师刷新


            pass




