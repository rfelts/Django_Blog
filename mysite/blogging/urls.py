from django.urls import path, include
from blogging.views import list_view, detail_view
from rest_framework import routers
from blogging import views


router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'categories', views.CateoryViewSet)


urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>/', detail_view, name="blog_detail"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
