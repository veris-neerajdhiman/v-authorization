#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- authorization.admin
~~~~~~~~~~~~~~~~~~~~~

- This file contains admin models of authorization micro service
"""

# future
from __future__ import unicode_literals

# 3rd party


# Django
from django.contrib import admin


# local


# own app
from authorization import models


class AuthorizationPolicyAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('id', 'source', 'created_at', 'modified_at', )
    list_display_links = ('source',)
    search_fields = ('id', 'source', )
    list_per_page = 20
    ordering = ('-id',)


class AuthorizationPolicyPermAdmin(admin.ModelAdmin):
    """
    """
    list_display = ('id', 'source', 'target', 'create', 'update', 'read', 'delete', 'created_at', 'modified_at', )
    list_display_links = ('source', 'target',)
    list_filter = ('create', 'update', 'read', 'delete', )
    search_fields = ('id', 'source__source', 'target', )
    list_per_page = 20
    ordering = ('-id',)


admin.site.register(models.AuthPolicy, AuthorizationPolicyAdmin)
admin.site.register(models.AuthPolicyPermissions, AuthorizationPolicyPermAdmin)


