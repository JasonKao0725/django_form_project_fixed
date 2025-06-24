from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),  # ✅ 加上 name='index'
    path('post/', views.post, name='post'),
    path('post1/', views.post1, name='post1'),
    path('post2/', views.post2, name='post2'),
    path('postform/', views.postform, name='postform'),
    path('delete/<int:id>/', views.delete, name='delete'),
]