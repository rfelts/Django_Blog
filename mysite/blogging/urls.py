from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from blogging import views
from blogging.feeds import LatestEntriesFeed

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)
router.register(r'categories', views.CateoryViewSet)

urlpatterns = [
    path('', views.list_view, name="blog_index"),
    path('posts/<int:post_id>/', views.detail_view, name="blog_detail"),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('latest/feed/', LatestEntriesFeed(), name='feeds'),
]
