from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.UserList.as_view(), name='UserList'),
    path('<int:pk>', views.UserDetail.as_view(), name='UserDetail')
]