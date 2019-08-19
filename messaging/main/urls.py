from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path
from . import views


urlpatterns = [
  path('auth-token/', obtain_auth_token, name='auth_token'),

  path('message/', views.MessagePageView.as_view(), name='list'),
  path('message/create/<int:receiver_pk>', views.MessagePageView.as_view(), name='create'),
  path('message/<int:pk>/', views.MessagePageView.as_view(), name='read'),
  path('message/delete/<int:pk>', views.MessagePageView.as_view(), name='delete')
]