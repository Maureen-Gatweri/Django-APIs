from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ClassroomSerializer
from rest_framework.response import Response

class ClassroomListView(APIView):
    def get(self,request):
        Classroom=Classroom.objects.all()
        serializer=ClassroomSerializer(Classroom, many=True)
        return Response(serializer.data)




