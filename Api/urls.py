from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.UserList.as_view(), name='UserList'),
    path('<str:name>', views.UserDetail.as_view(), name='UserDetail')
]