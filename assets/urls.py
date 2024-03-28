
from django.urls import path
from . import views


urlpatterns = [

    path("",views.index,name="index"),
    path('dashboard',views.dashboard,name='dashboard'),
    path('senddata',views.senddata,name='senddata'),
    path('saveitems',views.saveitems,name='saveitems'),
    path('getroomdata/<str:data>',views.getroomdata,name='getroomdata'),
    path('roomrequests/<str:datas>',views.roomrequests,name='roomrequests'),
    path('deleteroom/<str:uuids>',views.deleteroom,name='deleteroom'),
    path('deleteclient/<str:uuids>',views.deleteclient,name='deleteclient'),
    path('getclients',views.getclients,name='getclients'),
    path('instadata',views.instadatas,name='instadatas'),
    path('contacting',views.contacting,name='contacting'),
    path('joiningclass',views.joiningclass,name='joiningclass'),
    path('ssc_getdata',views.ssc_getdata,name='ssc_getdata'),
    path('deletecontact/<str:uuids>',views.deletecontact,name='deletecontact'),
    path('deletejoin/<str:uuids>',views.deletejoin,name='deletejoin'),
    path('saveassignment',views.saveassignment,name='saveassignment'),
    path('getassignment',views.getassignment,name='getassignment'),
    path('assignment',views.assignment,name='assignment'),
    path('assignmentreq',views.assignmentreq,name='assignmentreq'),
   



]