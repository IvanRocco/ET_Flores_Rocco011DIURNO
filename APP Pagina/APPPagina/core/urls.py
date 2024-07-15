from django.urls import path
from .views import home, form_beat, eliminar, modificar, ventana_inicio, ventana_info, listado_beats
from core import views
from django.contrib.auth import views as auth_views
from appNero.settings import EMAIL_HOST_PASSWORD
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('', ventana_inicio, name='home'),        # Ruta raíz para ventana_inicio
    path('form_beat/', form_beat, name='form_beat'),
    path('home/', home, name='tracklist'),        # Ruta para la antigua home
    path('eliminar/<int:id>/', eliminar, name='eliminar'),
    path('modificar/<int:id>/', modificar, name='modificar'),
    path('ventana_info/', ventana_info, name='ventana_info'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('buscar/', views.listado_beats, name='listado_beats'),     
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    ]
