# 此文件用于用户登录，会从数据表中检查有没有符合的id
import time
from database.models import wuser_info
from database.models import course
from database.models import courese_selected
from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class login(APIView):
    def post(self,request,*args,**kwargs):
        wx_code = request.data.get('code')
        username = request.data.get('username')
        info={
            "appid" : 'wx09236611cba1fa77',
            "secret" : '0431676f306f490f7e74447f429c0ba4',
            "js_code":wx_code,
            "grant_type":'authorization_code'
        }
        result = requests.get(url='https://api.weixin.qq.com/sns/jscode2session',params=info)
        id = result.json()['openid']
        #id = 'guo'
        #session_key =result.json()['session_key']
        course_id_list = []
        course_type_list = []
        #se_course_id_list = []

        if wuser_info.objects.filter(opend_id=id).exists(): #如果用户存在

            if wuser_info.objects.filter(opend_id=id).first().role == '1':   # 如果是学生
                name = wuser_info.objects.filter(opend_id=id).first().name
                list2 = courese_selected.objects.filter(stu_id=id)  # 所有学生选过的课程
                # ai_score_list=[]
                for var in list2:
                    #se_course_id_list.append(var.cou_se_id)
                    course_id_list.append(var.cou_id)
                    course_type_list.append(course.objects.all().filter(course_id=var.cou_id).first().cou_type)
                  #  ai_score_list.append(var.ai_scoure_one)
                return Response({
                    'open_id': id,
                    'name':name,
                    #'session_key':session_key,
                    'role': '1',
                    'course_id_list': course_id_list,
                   # 'se_course_id_list': se_course_id_list,
                    'course_type_list': course_type_list,  # ai成绩和课程id，课程类型，选课信息表有顺序的关系
                })
            elif wuser_info.objects.filter(opend_id=id).first().role == '2':  # 如果是老师,老师可能开多个班级？ x
                course_id = courese_selected.objects.filter(tea_id=id).first().cou_id
                stud_list = []
                stud_name_list = []
                name = wuser_info.objects.filter(opend_id=id).first().name
                all_fix = courese_selected.objects.filter(cou_id=course_id)

                for var in all_fix:
                    if var.stu_id != None:
                        stud_list.append(var.stu_id)  # 所有选了这个课的学生的id
                        stud_name_list.append(wuser_info.objects.filter(opend_id=var.stu_id).first().name)

                return Response({
                    'open_id': id,
                    'name': name,
                    #'session_key': session_key,
                    'role': '2',
                    'course_id':course_id,
                    'stud_id_list': stud_list,  # 这两个list是一一对应的
                    'stud_name_list': stud_name_list
                })

            else:   # 依旧是普通游客
                name = wuser_info.objects.filter(opend_id=id).first().name
                return Response({
                    'name':name,
                    'open_id': id,
                    #'session_key': session_key,
                    'role': '0'
                })
                pass

        else:  #  如果是新用户
            nowtime = time.localtime()
            realtime = ""
            realtime += str(nowtime.tm_year) + "-" + str(nowtime.tm_mon) + "-" + str(nowtime.tm_mday)
            wuser_info.objects.create(opend_id=id, res_time=realtime, role = '0', name = username)
            return Response({
            # 'course_id_list': course_id_list,  # 返回空的值?
                'name': username,
                'open_id': id,
                'role': '0'
            })

