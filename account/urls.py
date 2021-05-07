from django.urls import path
from. import views

app_name= 'account'

urlpatterns=[
    path('login/', views.loginView.as_view(), name='login'),
    path('signup/', views.signupView.as_view(), name='signup'),
    path('logout/', views.logoutView.as_view(), name='logout'),
]