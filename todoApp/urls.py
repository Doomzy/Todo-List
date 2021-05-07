from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required

app_name= "to_do_app"

urlpatterns = [
    path('', login_required(views.TodoView.as_view()), name="app"),
]
