from django.contrib import admin
from django.urls import path
from companions.views import ( login_view, register_view, logout_view, home_view, special_view)
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from django.contrib.auth.views import LoginView, LogoutView, PasswordResetDoneView, PasswordResetView, PasswordResetConfirmView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', home_view, name='home'), 
    path('admin/', admin.site.urls),
    path('password-reset/', 
        auth_views.PasswordResetView.as_view(
            template_name="companions/password_reset.html"
            ), 
        name="password_reset"),
    path('password-reset/done/', 
        auth_views.PasswordResetDoneView.as_view(
            template_name="companions/password_reset_done.html"
        ), 
        name="password_reset_done"),
     path('password-reset-confirm/<uidb64>/<token>/', 
        auth_views.PasswordResetConfirmView.as_view(
            template_name="companions/password_reset_confirm.html"
        ), 
        name="password_reset_confirm"),
    path('password-reset-complete/', 
        auth_views.PasswordResetCompleteView.as_view(
            template_name="companions/password_reset_complete.html"
            ), 
        name="password_reset_complete"),
    path('companions/', include('companions.urls')),
    path('logout/', logout_view, name='logout'),
    path('special/', special_view, name='special')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
