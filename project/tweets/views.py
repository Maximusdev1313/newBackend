
from urllib import request
from .models import Student
from .serializers import StudentSerializer
from rest_framework.viewsets import ModelViewSet
from .pusher import pusher_client
from rest_framework.response import Response

class StudentsViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    def post(self, request):
        pusher_client.trigger('TweetMax-development', 'massage', {
            'name': request.data['name'],
            'massage': request.data['massage'],
        })
        return Response([])

