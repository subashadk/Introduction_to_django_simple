from . import views
from django.urls import path, re_path


urlpatterns = [
   
    path('blog/', views.home, name='home'),
    path('blog/about/', views.about, name='about'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('user/<str:username>/', views.user_profile, name='user_profile'),
    path('article/<int:year>/<int:month>/', views.article_detail, name='article_archive'),

    # re_path(r'^article/(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/$', views.article_archive, name='article_archive'),
]