from django.urls import path
from .views import *
urlpatterns = [
    path('', home, name='home'),
    path('blog-list/', blogList, name='blogList'),
    path('blog-details/<str:pk>', blogDetail, name='blogDetail'),
    path('blog-create/', blogCreate, name='blogCreate'),
    path('blog-update/', blogUpdate, name='blogUpdate'),
    path('blog-delete/<str:pk>', blogDelete, name='blogDelete'),
]

