#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- micro_service.authorization.router
~~~~~~~~~~~~~~~~~

- This file contains Authorization service routers.
"""

# future
from __future__ import unicode_literals

# Django
from django.conf import settings
from django.conf.urls import url

# own app
from authorization import views

SOURCE_UUID_REGEX = getattr(settings, 'SOURCE_RGX')


policy_create = views.AuthorizationPolicyViewSet.as_view({
    'post': 'create',
})

policy_detail = views.AuthorizationPolicyViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy'
})

policy_list = views.AuthorizationPolicyViewSet.as_view({
    'get': 'list_source_policy',
})

policy_update = views.AuthorizationPolicyViewSet.as_view({
    'patch': 'update_permission_set',
    'delete': 'destroy_permission_set'
})

policy_validate = views.AuthorizationPolicyViewSet.as_view({
    'post': 'validate_policy_permission',
})


urlpatterns = [
        url(r'policy/$',
            policy_create,
            name='authorization-policy-create'),
        url(r'policy/(?P<pk>\d+)/$',
            policy_detail,
            name='authorization-policy-detail'),
        url(r'policy/list/$',
            policy_list,
            name='authorization-policy-list'),
        url(r'policy/(?P<source_pk>\d+)/(?P<perm_pk>\d+)/$',
            policy_update,
            name='authorization-policy-update-delete'),
        url(r'policy/validate/$',
            policy_validate,
            name='authorization-policy-validate'),
]
