from django.urls import path, include
from accounts.views import CreateUserView, VerifyApiView
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('signup/', CreateUserView.as_view(), name='sign_up'),
    path('verify/', VerifyApiView.as_view(), name='verify'),
    path('blog-list/', blogList, name='blogList'),
    path('blog-details/<str:pk>', blogDetail, name='blogDetail'),
    path('blog-create/', blogCreate, name='blogCreate'),
    path('blog-update/', blogUpdate, name='blogUpdate'),
    path('blog-delete/<str:pk>', blogDelete, name='blogDelete'),
]
