from django.conf.urls import url
from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenRefreshView

from . import views

urlpatterns = [
    path('sign_up/', views.SignUpView.as_view(), name='sign_up'),
    path('log_in/', views.LogInView.as_view(), name='log_in'),
    path('token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('posts/', views.PostListView.as_view()),
    path('post/<int:pk>/', views.PostDetailView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)