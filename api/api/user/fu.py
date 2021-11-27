from database.models import wuser_info
from database.models import courese_selected
from rest_framework.views import APIView
from rest_framework.response import Response
'''
接收的参数，，openid,role,此接口用于数据刷新，由于创建时姓名取错，为了减少可能的错误不再改名
请在前端设置好游客用户（未填写邀请码）不能调用该接口的操作
学生刷新应该是刷新分数列表，不用返回课程信息，因为在登录时已经返回，，认证之后也有
'''
class renew(APIView):
    def post(self,request,*args,**kwargs):
        open_id = request.data.get('openid')
        role = request.data.get('role')
        if role== '2':  #老师刷新
            course_id = courese_selected.objects.filter(tea_id=open_id).first().cou_id
            stud_list = []
            stud_name_list = []
            all_fix = courese_selected.objects.filter(cou_id=course_id)
            for var in all_fix:
                if var.stu_id != None:
                    stud_list.append(var.stu_id)  # 所有选了这个课的学生的id
                    stud_name_list.append(wuser_info.objects.filter(opend_id=var.stu_id).first().name)
            return Response({
                'errsmg': 'ok',
                'course_id': course_id,
                'stud_id_list': stud_list,
                'stud_name_list': stud_name_list
            })
        else:
            return Response({
                'errsmg':'role error!'
            })





