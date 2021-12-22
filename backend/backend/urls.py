from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .views import UserViewSet, CustomAuthToken
from core.views import ItemViewSet, ListViewSet, RegisterView



router = routers.DefaultRouter()
router.register(r'users', UserViewSet,basename='users')
router.register(r'list', ListViewSet, basename='list')
router.register(r'item', ItemViewSet, basename='item')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-token-auth/', CustomAuthToken.as_view()),
    path('createuser/',  RegisterView.as_view(), name='createuser')
]
