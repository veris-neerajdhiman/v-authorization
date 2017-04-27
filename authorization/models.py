#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- authorization.models
~~~~~~~~~~~~~~

- This file holds the necessary models for authorization micro-service
"""

# future
from __future__ import unicode_literals

# 3rd party
import uuid

# Django
from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.core.validators import RegexValidator
# local


# own app


SOURCE_RGX = getattr(settings, 'SOURCE_RGX')
SAMPLE_SOURCE = getattr(settings, 'SAMPLE_RGX_MATCHED_SOURCE')
RESOURCE_RGX = getattr(settings, 'RESOURCE_RGX')
RESOURCE_RGX_MATCHED_RESOURCE = getattr(settings, 'RESOURCE_RGX_MATCHED_RESOURCE')


class AuthPolicy(models.Model):
    """Authorization Policy Model

        Who can access what with how much extent (CURD) ?
    """

    # Attributes
    source = models.TextField(
            _('Source (Who ?)'),
            unique=True,
            validators=[
                RegexValidator(r'{0}'.format(SOURCE_RGX),
                               _('Enter a valid Source. This value may contain only match with Regular'
                                 ' Expression {source_regular_expression} , Sample Source {sample_source}'
                                 .format(source_regular_expression=SOURCE_RGX, sample_source=SAMPLE_SOURCE))
                               ),
            ],
            help_text=_('Who wants to access something ? Source must match with Regular'
                        ' Expression {source_regular_expression} , Sample Source {sample_source}'
                        .format(source_regular_expression=SOURCE_RGX, sample_source=SAMPLE_SOURCE)),
    )
    created_at = models.DateTimeField(
                 _('created at'),
                 auto_now_add=True,
                 db_index=True,
    )
    modified_at = models.DateTimeField(
                 _('modified at'),
                 auto_now=True,
                 db_index=True,
    )

    # Meta
    class Meta:
        verbose_name = _("Authorization Policy")
        verbose_name_plural = _("Authorization Policies")

    # Functions
    def __str__(self):
        return str(self.source)


class AuthPolicyPermissions(models.Model):
    """Authorization Policy Permissions Model

        Who can access what with how much extent (CURD) ?
    """

    # Relations
    source = models.ForeignKey(
        AuthPolicy,
        related_name='source_permission_set',
        on_delete=models.CASCADE,
        help_text=_('Policy Source')

    )

    # Attributes
    target = models.TextField(
            _('Target (What ?)'),
            unique=True,
            validators=[
                RegexValidator(r'{0}'.format(RESOURCE_RGX),
                               _('Enter a valid Resource. This value may contain only match with Regular'
                                 ' Expression {resource_regular_expression} , Sample Source {sample_resource}'
                                 .format(resource_regular_expression=RESOURCE_RGX, sample_resource=RESOURCE_RGX_MATCHED_RESOURCE))
                               ),
            ],
            help_text=_('What can be accessed ? Resource must match with Regular'
                        ' Expression {resource_regular_expression} , Sample Resource {sample_resource}'
                        .format(
                resource_regular_expression=RESOURCE_RGX,
                sample_resource=RESOURCE_RGX_MATCHED_RESOURCE
            )),
    )
    create = models.BooleanField(
            _('can create'),
            default=False,
    )
    update = models.BooleanField(
            _('can update'),
            default=False,
    )
    read = models.BooleanField(
            _('can read'),
            default=False,
    )
    delete = models.BooleanField(
            _('can delete'),
            default=False,
    )
    created_at = models.DateTimeField(
                 _('created at'),
                 auto_now_add=True,
                 db_index=True,
    )
    modified_at = models.DateTimeField(
                 _('modified at'),
                 auto_now=True,
                 db_index=True,
    )

    # Meta
    class Meta:
        verbose_name = _("Authorization Policy Permission")
        verbose_name_plural = _("Authorization Policy Permissions")
        unique_together = ('source', 'target', )

    # Functions
    def __str__(self):
        return str(self.target)
