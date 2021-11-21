from database.models import wuser_info

from rest_framework.views import APIView
from rest_framework.response import Response

class real_name(APIView):
    def post(self, request, *args, **kwargs):
        openid = request.get('openid')
        real_name = request.get('real_name')
        wuser_info.objects.filter(opend_id=openid).update(name=real_name)
        return Response({
            'errmsg':'ok'
        })