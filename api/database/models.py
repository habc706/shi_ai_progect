from django.db import models

class wuser_info(models.Model):
    opend_id = models.CharField(max_length=30, primary_key=True, null=False)  # 不能为空,添加数据的时候，主键可以不添加的？？
    res_time = models.DateField()  # 默认非空
    wsex = models.CharField(max_length=2, null=True)  # 可为空
    name = models.CharField(max_length=6,null=True)
    role = models.CharField(null=False, default='0',max_length=1)  # 学生就1 老师是2 游客是0


class course(models.Model):
    course_id = models.CharField(primary_key=True,max_length=30)
    cou_info = models.CharField(max_length=300)
    cou_type = models.CharField(max_length=1)



class course_score(models.Model):
    score_id = models.AutoField(primary_key= True, default='1')  # 注意这里不能是直接的数字
    cou_id = models.CharField(max_length=30)  # 课程id
    stud_id = models.CharField(max_length=30)  # 学生id
    number = models.IntegerField()  # 第几次的
    real_score = models.IntegerField()  # 实际分数


# 该表的主要作用是记录学生选了什么课，老师开了什么课
class courese_selected(models.Model):
    cou_se_id=models.CharField(primary_key=True,max_length=50)
    cou_id = models.CharField(max_length=30)
    stu_id=models.CharField(max_length=30,null=True)
    tea_id=models.CharField(max_length=30,null=True)
    #ai_scoure_one=models.IntegerField(default=0)  最终的分数是由course_score记录，无需在此记录
   # scoure_one=models.CharField(max_length=30,default='')



