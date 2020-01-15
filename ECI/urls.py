from django.urls import path
from django.conf.urls import url
from . import views
app_name='ECI'

urlpatterns= [
  
path('',views.index,name='index'),
path("login",views.login,name="login"),
path('register',views.register,name='register'),
path('eciuser',views.eciuser,name='eciuser'),
path('forgotpassword',views.forgotpassword,name='forgotpassword'),
path('validate_credentials',views.validate_credentials,name='validate_credentials'),
path('clientregister',views.clientregister,name='clientregister'),
path('quiz',views.quiz,name='quiz'),
path('service',views.service,name='service'),
path('team',views.team,name='team'),
path('about',views.about,name='about'),
path('log_cred',views.log_cred,name='log_cred')
]