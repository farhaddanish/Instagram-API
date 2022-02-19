from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token
from followApp.views import MakeFollowGV,AllFollowers,AllFollowing,UnFollowGV

urlpatterns = [
    # editing your own profile
    path('account/register/<int:pk>/profile/',
         views.ProfileDetailGV.as_view(), name="registerGV"),
    # creating account
    path('account/register/', views.UserCreationGV.as_view(), name="signupGV"),
    # getting token
    path('account/login/', obtain_auth_token, name="login"),

    # All Profile Users
    path('profiles/', views.AllProfileGV.as_view(), name="allPrfoile"),
    # your own profile
    path('profiles/<int:pk>/', views.SingleProfileGV.as_view(), name="singlePrfoile"),

    # make follow
    path('profiles/<int:pk>/makefollow/',MakeFollowGV.as_view(),name="makefollow"),
    # seeing all followers of your profile
    path('profiles/<int:pk>/followers/',AllFollowers.as_view(),name="allfollowers"),
    # seeing all foolowing of your profile
    path('profiles/<int:pk>/following/',AllFollowing.as_view(),name="allfollowing"),

    # making unfollow
    path('profiles/<int:pk>/unfollow/',UnFollowGV.as_view(),name="unfollow"),




]
