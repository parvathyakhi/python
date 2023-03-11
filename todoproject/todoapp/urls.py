from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from todoapp import views

urlpatterns = [
    path('',views.todo,name='todo'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cgv/',views.tasklistview.as_view(),name='cgv'),
    path('cbvdetail/<int:pk>/',views.taskdetailview.as_view(),name='cbvdetail'),
    path('cgvup/<int:pk>/',views.taskupdate.as_view(),name='cgvup'),
    path('cbvdelete/<int:pk>/',views.taskdeleteview.as_view(),name='cbvdelete'),
]

