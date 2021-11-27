from rest_framework.views import APIView
from rest_framework.response import Response
from database.models import course_score

class enter_score(APIView):
    def post(self,request,*args,**kwargs):
        stud_id = request.data.get('stud_id')
        total_score = request.get('total_score')
        number = request.get('number')
        cou_id = request.get('cou_id')
        evaluate = request.get('evaluate')

        try:
            course_score.objects.create(real_score=total_score, number=number, stud_id=stud_id, cou_id=cou_id,
                                        evaluate=evaluate)
            return Response({
                'errmsg': 'ok'
            })
        except:
            return Response({
                'errmsg': 'fail'
            })
