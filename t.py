
import os
import time
import json
import re

judge= r'"(.*?)"'
judge2 = r'(.*?)='
data = {}
a = [' lan="cn" type="study" version="7,0,0,1024"', ' accuracy_score="0.000000" beg_pos="0" content="今天的天气很好啊。" emotion_score="0.000000" end_pos="2983\
" except_info="28689" fluency_score="52.444565" integrity_score="62.500000" is_rejected="false" phone_score="25.000000" time_len="2983" tone_score="87.5000\
00" total_score="48.867748"']



print(a[1].split(' ')[1:])
# # print(type(a[0].split(' '))) # list ,第0个为空
#
# aa = ai_score_storage.objects.all().first()
# print(aa.lujing)
# print(aa.total_score)
# b = a[0].split(' ')[1:] # list
# # c=json.loads(a)
# print(b)
#
# for var in b:
#     mid = re.findall(judge2,var)[0]
#     data[mid] = re.findall(judge,var)[0]
#  # 由于处理之后的东西仍然是一个列表，，要加[0]
#
# print(data)
# print(data['content'])


# print(a[0].split(' ')[2])
# print(type(a[0].split(' ')[2])) # str
#print(c)


# path = 'C:\\Users\\Lenovo\\Desktop\\01\\103'
# wenjian = path +'\\' +str(time.mktime(time.localtime())) + '.mp3'
#
# if not os.path.exists(path):
#     os.makedirs(path)
# with open('C:\\Users\\Lenovo\\Desktop\\01\\1024\\1637728149.0.mp3','rb') as e:
#     content = e.read()
#
#
# with open(wenjian,'wb') as e:
#
#     e.write(content)

# try:
#     get_ai_score(content,text)
#     try:
#         if not os.path.exists(path):
#             os.makedirs(path)
#         with open(path  + '.mp3', 'wb') as e:
#             e.write(content)
#         return Response({
#             'messg': 'ok',
#             'data': result.data
#         })
#
#     except:
#         return Response({
#             'messg': 'score ok but storage error happen',
#             'data': result.data
#         })
#
#
# except:  # 获取分数失败
#
#     try:
#         if not os.path.exists(path):
#             os.makedirs(path)
#         with open(path + str(time.mktime(time.localtime())) + '.mp3', 'wb') as e:
#             e.write(content)
#         return Response({
#             'messg': 'storage ok but score error happen',
#             'data': result.data
#         })
#
#     except:
#         return Response({
#             'messg': 'storage error happen and score error happen',
#             'data': result.data
#         })
