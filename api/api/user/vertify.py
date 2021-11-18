from database.models import wuser_info
from database.models import course
from database.models import courese_selected
from rest_framework.views import APIView
from rest_framework.response import Response

# 返回的应该是这个所选的课程的id和类型，在选课信息表中特定的编号,并且在数据库中存进这个信息
# 如果已经有了相应的信息就返对应的信息
'''
如果用户填写的邀请码没有错,那返回的errmsg都是ok，如果邀请码填写错误是invitation fill in error!
如果是身份不对应(老师填了学生的，学生填了老师的),errmsg是role do not match
此外，确保openid是已经存在的，先登录才可以使用该接口

'''

class vertify(APIView):
    def post(self, request, *args, **kwargs):
        openid=request.data.get('openid')
        invitation=request.data.get('invitation')
        #openid='tresrasd'
        ### role  courseid 根据邀请码切片得到
        role =''
        courseid=''

        # 根据courseid和用户特色信息（openid）得到selected_course_id
        selected_course_id = ''
        '''防止邀请码填写错误'''
        if course.objects.filter(course_id=courseid).exists():  # 如果课程存在,即，没有填错信息

            if wuser_info.objects.filter(opend_id=openid).first().role == '0':  # 如果是游客
                wuser_info.objects.filter(opend_id=openid).update(role=role)  # 存入角色信息

            else:  # 如果不是游客填写邀请码
                if wuser_info.objects.filter(opend_id=openid).first().role != role: # 身份信息不配对，老师填写了学生的邀请码，学生填写了老师的邀请码
                    return Response({
                        'errmsg': 'role do not match'
                    })

            if courese_selected.objects.filter(cou_se_id=selected_course_id).exists():  # 如果选课信息码存在，即重复填写了邀请码
                return Response({
                    'errmsg':'already choose!',
                    'se_course_id': selected_course_id,
                })
            else:  # 如果是真的第一次选课,
                if role == '1':  # 如果是学生
                    courese_selected.objects.create(cou_se_id=selected_course_id, stu_id=openid, cou_id=courseid)
                    course_type = course.objects.all().filter(course_id=courseid).first().cou_type
                    return Response({
                        'errmsg':'ok',
                        'cou_id': courseid,
                        'se_course_id': selected_course_id,
                        'course_type': course_type
                    })

                elif role == '2':  # 如果是老师
                    courese_selected.objects.create(cou_se_id=selected_course_id, tea_id=openid, cou_id=courseid)
                    stud_id_list = []
                    stud_name_list = []
                    all_fix = courese_selected.objects.filter(cou_id=courseid)
                    for var in all_fix:
                        if var.stu_id != None:
                            stud_id_list.append(var.stu_id)  # 所有选了这个课的学生的id
                            stud_name_list.append(wuser_info.objects.filter(open_id=var.stu_id).first().name)
                    return Response({
                        'errmsg':'ok',
                        'cou_id': courseid,
                        'stud_id_list': stud_id_list,
                        'stud_name_list': stud_name_list
                    })
        else:       # 邀请码填写错误，课程不存在

            return  Response({
                'errmsg': 'invitation fill in error!'
            })






