from django.urls import path , include
from . import views


app_name= 'home'
urlpatterns=[
    path('',views.logs,name='logs'),
    path('home',views.home,name='home'),
    path('regs',views.regs,name='regs'),
    path('prof',views.prof,name='prof'),
    path('logsout',views.logsout,name='logsout'),
    path('logged',views.logged,name='logged'),



   ]


