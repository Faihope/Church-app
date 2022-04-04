import imp
from django.urls import path
from Blog import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.Home,name='Home'),
    path('blog/',views.Blog,name='Blog'),
    path('about/',views.About,name='About'),
    path('posts/',views.Posts,name='Posts'),
    path('registeruser/',views.registeruser,name='registeruser'),
    path('login/', views.loginpage, name="login"),
    path('post/<int:pk>/add_comment', views.add_comment, name='add-comment'),
    path('view-comment/(\d+)/', views.comment_view, name="comment_view"),
    path(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post-detail'),



] 
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
