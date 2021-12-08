from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register("users", views.UserViewSet, 'user')

urlpatterns = [
    # path('', include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('oauth2-info/', views.AuthInfo.as_view()),
    path('users/', views.UserViewSet.as_view(), name='users'),
    path('verify-email/', views.VerifyEmail.as_view(), name='verify-email'),
]
