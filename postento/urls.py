# postento/urls.py                                                                                                                                
from django.conf.urls import url
from postento import views
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    # path('admin/', admin.site.urls),         
    path("login/", views.login, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    path("", views.home, name="home"),
    # path('', views.HomePageView.as_view(), name='homepage'),
    # path('about/', views.AboutPageView.as_view(), name='about')
    # url(r'^$', views.HomePageView.as_view()),
    # url(r'^about/$', views.AboutPageView.as_view()),
]
