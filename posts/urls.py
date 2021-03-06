from django.urls import include, path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register('', views.PostViewSet)

urlpatterns = [
    # comments crud operations
    # path('<int:pk>/comments/', views.CommentList.as_view(), name='comment_list'),
    # path('<int:pk>/comments/<int:comment_pk>/', views.CommentDetail.as_view(), name='comment_detail'),
]

urlpatterns += router.urls

'''

# if we define urls manually we could do something like this

post_list = views.PostViewSet.as_view({
    'get': 'list',
    'post': 'create',
    })

post_detail = views.PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
    })

post_comments = views.PostViewSet.as_view({
    'get': 'comments',
    })


urlpatterns = [
    path('', post_list, name='post-list'),
    path('<int:pk>/', post_detail, name='post-detail'),
    path('<int:pk>/comments', post_comments, name='post-comments'),
]

# urlpatterns = format_suffix_patterns(urlpatterns)

'''
