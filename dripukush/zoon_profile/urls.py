from django.urls import path
from . import views

app_name='zoon_profile'

urlpatterns = [
    #zone page
    path('zoon1/', views.Dhaka, name='dhaka_page'),
    path('zoon2/', views.Chittagong, name='chittagong_page'),
    path('zoon3/', views.Cumilla, name='cumilla_page'),
    path('zoon4/', views.Syllet, name='syllet_page'),
    path('zoon5/', views.Moymonshing, name='maymonshing_page'),
    path('zoon6/', views.Power_Plant, name='Power_Plant_page'),

    #member list
    path('dhaka-member/', views.DhakaMember, name='DhakaMember'),
    path('ctg-member/', views.ChittagongMember, name='ChittagongMember'),
    path('com-member/', views.ComillaMember, name='ComillaMember'),
    path('syllet-member/', views.SylletMember, name='SylletMember'),
    path('moy-member/', views.MoymonshinMember, name='MoymonshinMember'),
    path('pp-member/', views.Power_plantMember, name='Power_plantMember'),
    
    #comittee info personal 
    path('all_comite/', views.AllComite, name='AllComite'),
    path('info/', views.CommitteDetails, name='CommitteDetails'),

]
