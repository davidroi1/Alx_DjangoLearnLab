from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import BookList
from .views import BookViewSet


router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')


urlpatterns = [
    path('api/', include(router.urls)),
    path('books/', BookList.as_view(), name='book_list'),
    path('api-token-auth/', obtain_auth_token),
]