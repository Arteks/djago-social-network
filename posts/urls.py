from django.conf.urls import url

from .views import (
    PostList,
    PostDetail,
    PostCreation,
    PostUpdate,
    PostDelete
)

urlpatterns = [

    url(r'^$', PostList.as_view(), name='list'),
    url(r'^(?P<pk>\d+)$', PostDetail.as_view(), name='detail'),
    url(r'^new$', PostCreation.as_view(), name='new'),
    url(r'^edit/(?P<pk>\d+)$', PostUpdate.as_view(), name='edit'),
    url(r'^delete/(?P<pk>\d+)$', PostDelete.as_view(), name='delete'),

]