
from Service.views.home import views_home
from Service.views.auth import views_auth
from django.urls import path, re_path

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views_auth.LoginPage, name='login'),
    path('home', views_home.index, name='index'),
    path('validate', views_auth.validate_login, name='validate_login'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += (
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) +
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        )