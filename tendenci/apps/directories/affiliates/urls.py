from django.conf.urls import url
from tendenci.apps.site_settings.utils import get_setting
from . import views

urlpatterns = [
    url(r'^request/(?P<to_directory_id>\d+)/$',
        views.request_associate, name="affiliates.request_associate"),
    url(r'^approve/(?P<affiliate_request_id>\d+)/$',
        views.approve, name="affiliates.request_approve"),
    url(r'^reject/(?P<affiliate_request_id>\d+)/$',
        views.reject, name="affiliates.request_reject"),
    url(r'^requests-list/(?P<directory_id>\d+)/$',
        views.requests_list, name="affiliates.requests_list"),
]