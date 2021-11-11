from django.db import models

class wuser_info(models.Model):
    opend_id = models.CharField(max_length=30, primary_key=True, null=False)  # 不能为空,添加数据的时候，主键可以不添加的？？
    res_time = models.DateField()  # 默认非空 '2020-9-18'
    wsex = models.CharField(max_length=2, null=True)  # 可为空
    name = models.CharField(max_length=6,null=True)
    role = models.CharField(null=False, default='0',max_length=1)  # 如果是学生就1老师是2游客是0

class stu(models.Model):
    stu_id = models.CharField(primary_key=True,max_length=30)

    wsex=models.CharField(null=True,max_length=1)

class tea(models.Model):
    tea_id=models.CharField(max_length=1,primary_key=True)

    wsex=models.CharField(null=True,max_length=1)


class course(models.Model):
    course_id = models.AutoField(primary_key=True) # 11位整数
    cou_info = models.CharField(max_length=250)
    cou_type = models.CharField(max_length=1)

class courese_selected(models.Model):
    cou_se_id=models.AutoField(primary_key=True)   # 11位整数
    cou_id = models.CharField(max_length=30)
    stu_id=models.CharField(max_length=30,null=True)
    tea_id=models.CharField(max_length=30,null=True)
    ai_scoure_one=models.IntegerField()
    scoure_one=models.CharField(max_length=30)



