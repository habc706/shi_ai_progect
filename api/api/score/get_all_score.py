from rest_framework.views import APIView
from rest_framework.response import Response
from database.models import course
from database.models import course_score

'''
此接口接受post请求，请求参数位openid，course_id,请求的对象是学生,返回的是，按照次序排列号的分数数组
感觉那个页面的下拉刷新可以采取一样的接口,
'''

class get_all_score(APIView):
    def post(self,request,*args,**kwargs):
        openid = request.data.get('openid')
        course_id = request.data.get('course_id')
        score_list = []
        my_this_score = course_score.objects.filter(stud_id=openid,cou_id = course_id)
        my_order_score = my_this_score.order_by('number')  # 按照number拍好次序
        for var in my_order_score:
            score_list.append(var.real_score)

        return Response({
            'score_list':score_list
        })