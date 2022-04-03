from django.urls import path
from . import views
app_name='payment_app'
urlpatterns = [

    path('step1/', views.PaymentSetp_1, name='PaymentSetp_1'),
    path('step2/', views.PaymentSetp_2, name='PaymentSetp_2'),
    path('step3/', views.PaymentSetp_3, name='PaymentSetp_3'),
    path('step4/', views.PaymentSetp_4, name='PaymentSetp_4'),
    
]