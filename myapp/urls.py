from django.urls import path
from .views import *

urlpatterns = [
    path('users/', user_list_view),
    path('users/<int:pk>/', user_detail_view),
    path('profiles/', profile_list_view),
    path('profiles/<int:pk>/', profile_detail_view),
    path('posts/', post_list_view),
    path('posts/<int:pk>/', post_detail_view),
    path('likes/', like_list_view),
    path('likes/<int:pk>/', like_detail_view),
    path('favorites/', favorite_list_view),
    path('favorites/<int:pk>/', favorite_detail_view),
]
