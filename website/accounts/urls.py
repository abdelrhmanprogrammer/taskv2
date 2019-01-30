from django.urls import path , include
from django.contrib.auth import views as auth_views

urlpatterns=[
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='registration/passresetview.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/passresetdone.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/passresetconfirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/passcomplete.html'), name='password_reset_complete')]
