from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]
# url =>  vue, izay miseo amin n ecran
#  base url = 127.0.01:8000
# ex1
#  127.0.01:8000/admin
#                   io : admin.py 
# 127.0.01:8000
#            si  juste base url: view.postlite
# faceboook = base url
# facebook/profiletiana = url hafa