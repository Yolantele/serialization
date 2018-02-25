from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from .views.views import SnippetList, SnippetDetail
from .views.views import UserList, UserDetail
from django.conf.urls import include

urlpatterns = [
    url(r'^snippets/$', SnippetList.as_view()),
    url(r'^snippets/(?P<pk>[0-9]+)/$', SnippetDetail.as_view()),
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)$', UserDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^$', views.api_root),
    url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)