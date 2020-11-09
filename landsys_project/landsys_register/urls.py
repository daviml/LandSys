from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.landsys_formv,name='landsys_insertv'),
    path('<int:id>/',views.landsys_formv,name='landsys_updatev'),
    path('delete/<int:id>/',views.landsys_deletev,name='landsys_deletev'),
    path('listv/',views.landsys_listv,name='landsys_listv'),

    
    path('formc',views.landsys_formc,name='landsys_insertc'),
    path('<int:id>/',views.landsys_formc,name='landsys_updatec'),
    path('delete/<int:id>/',views.landsys_deletec,name='landsys_deletec'),
    path('listc/',views.landsys_listc,name='landsys_listc'),
]