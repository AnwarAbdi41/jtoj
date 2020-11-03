from django.conf.urls import url
from django.urls import path
from companions import views

app_name = 'companions'

urlpatterns = [
    url('register', views.register_view, name='register'),
    url('user_login', views.login_view, name='user_login'),
    url('top10companions', views.companions, name='top10companions'),
    url('jannatulFirdous', views.jannatulFirdous, name="jannatulFirdous"),
    url('first_companion', views.first_companion, name="first_companion"),
    url('second_companion', views.second_companion, name="second_companion"),
    url('third_companion', views.third_companion, name="third_companion"),
    url('fourth_companion', views.fourth_companion, name="fourth_companion"),
    url('fifth_companion', views.fifth_companion, name="fifth_companion"),
    url('sixth_companion', views.sixth_companion, name="sixth_companion"),
    url('seventh_companion', views.seventh_companion, name="seventh_companion"),
    url('eighth_companion', views.eighth_companion, name="eighth_companion"),
    url('ninth_companion', views.ninth_companion, name="ninth_companion"),
    url('tenth_companion', views.tenth_companion, name="tenth_companion"),
]