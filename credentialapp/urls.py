from django.urls import path
from . import views

urlpatterns = [
    path('cred',views.credfun,name='credfun'),
    path('login',views.loginfun,name='loginfun'),
    path('logout',views.logoutfun,name='logoutfun')
    #path('about',views.abt,name='about')
]