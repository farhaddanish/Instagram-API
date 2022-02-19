from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/posts/', views.AllPostGV .as_view(), name="post"),
    path('createpost/', views.CreatePostGV.as_view(), name="creatpost"),
    path('<int:pk>/posts/<int:pk2>/',
         views.SinglePostGV.as_view(), name="singlepost"),

]
