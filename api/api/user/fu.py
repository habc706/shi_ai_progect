from database.models import wuser_info
from database.models import course
from database.models import courese_selected
from rest_framework.views import APIView
from rest_framework.response import Response
import requests


'''
接收的参数，，openid,role,此接口用于数据刷新，由于创建时姓名取错，为了减少可能的错误不再改名
请在前端设置好游客用户（未填写邀请码）不能调用该接口的操作
'''
class renew(APIView):
    def post(self,request,*args,**kwargs):
        open_id = request.data.get('openid')
        role = request.data.get('role')
        if role == '1':  #学生刷新
            course_id_list = []
            course_type_list = []
            se_course_id_list = []
            list2 = courese_selected.objects.filter(stu_id=open_id)  # 所有学生选过的课程

            for var in list2:
                se_course_id_list.append(var.cou_se_id)
                course_id_list.append(var.cou_id)
                course_type_list.append(course.objects.all().filter(course_id=var.cou_id).first().cou_type)
            #  ai_score_list.append(var.ai_scoure_one)
            return Response({
                #'role': '1',
                'course_id_list': course_id_list,
                'se_course_id_list': se_course_id_list, #
                'course_type_list': course_type_list,  # ai成绩和课程id，课程类型，选课信息表有顺序的一一对应关系
            })

        else:  #老师刷新
            course_id = courese_selected.objects.filter(tea_id=open_id).first().cou_id
            stud_list = []
            stud_name_list = []

            all_fix = courese_selected.objects.filter(cou_id=course_id)

            for var in all_fix:
                if var.stu_id != None:
                    stud_list.append(var.stu_id)  # 所有选了这个课的学生的id
                    stud_name_list.append(wuser_info.objects.filter(opend_id=var.stu_id).first().name)

            return Response({

                #'role': '2',
                'course_id': course_id,
                'stud_id_list': stud_list,
                'stud_name_list': stud_name_list
            })






