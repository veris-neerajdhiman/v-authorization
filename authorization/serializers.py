# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
- micro_services.authorization.serializers
~~~~~~~~~~~~~~

- This file contains the Authorization Serializers.
 """

# future
from __future__ import unicode_literals

# 3rd party

# DRF
from rest_framework import serializers

# Django
from django.db import IntegrityError

# local

# own app
from authorization import models


class AuthorizationPolicyPermSerializer(serializers.ModelSerializer):
    """

    """
    create = serializers.BooleanField(required=True)
    update = serializers.BooleanField(required=True)
    read = serializers.BooleanField(required=True)
    delete = serializers.BooleanField(required=True)

    class Meta:
        model = models.AuthPolicyPermissions
        exclude = ('source', 'created_at', 'modified_at',)


class AuthorizationPolicySerializer(serializers.ModelSerializer):
    """Serializer used for adding Policy

    """
    source = serializers.CharField(required=True)
    source_permission_set = AuthorizationPolicyPermSerializer(many=True)

    class Meta:
        model = models.AuthPolicy
        fields = ('id', 'source', 'source_permission_set',)

    def create(self, validated_data):
        """

        :param validated_data: Serializer valid data
        :return: policy instance
        """
        permissions = validated_data.pop('source_permission_set')
        policy, created = models.AuthPolicy.objects.get_or_create(**validated_data)

        for permission in permissions:
            try:
                models.AuthPolicyPermissions.objects.create(source=policy, **permission)
            except IntegrityError:
                pass

        return policy


class AuthorizationPolicyUpdateSerializer(serializers.ModelSerializer):
    """Only permission are allowed to update.

    """

    class Meta:
        model = models.AuthPolicyPermissions
        fields = ('create', 'update', 'delete', 'read',)


class PolicyValidateSerializer(serializers.Serializer):
    """Serializer for checking Access of source over target

    """
    ACCESS_TYPES = ('create', 'update', 'read', 'delete', )

    source = serializers.CharField(required=True)
    resource = serializers.CharField(required=True)
    action = serializers.ChoiceField(choices=ACCESS_TYPES)

    def check_perm(self, instance, access_type):
        """

        :param instance: Authorization instance
        :param access_type: permission type
        :return: True/False
        """
        return getattr(instance, access_type, False)
