from django.shortcuts import render
from rest_framework.views import APIView

class TodoView(APIView):

    def get(self, request):
        return render(request, 'tdTemp.html')