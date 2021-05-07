from django.shortcuts import render,redirect
from django.http import response, HttpResponse
from rest_framework.views import APIView
from .models import Task
from .serializer import TaskSerializer

class TodoView(APIView):

    def getTask(self, request):
        modifId= request.POST.get("id")
        return Task.objects.get(id= modifId)

    def get(self, request):
        query_set_todo= Task.objects.filter(isItDone=False)
        query_set_done= Task.objects.filter(isItDone=True)
        return render(request, 'tdTemp.html', 
            {"tasks_todo":query_set_todo, "tasks_done":query_set_done}
        )

    def post(self, request):
            modifMethod= request.POST.get("_method")
            if modifMethod == "add":
                serialized = TaskSerializer(data=request.data)  
                if serialized.is_valid():
                    serialized.save()
                    return redirect('/', status=200)
    
            elif modifMethod == "done":
                wantedTask= self.getTask(request)
                wantedTask.isItDone= True
                wantedTask.save()
                return redirect('/', status=200)

            elif modifMethod == "delete":
                wantedTask= self.getTask(request)
                wantedTask.delete()
                return redirect('/', status=200)
            
            return HttpResponse( status=400)
    
