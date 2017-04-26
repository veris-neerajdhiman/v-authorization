#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- micro_services.authorization.views
~~~~~~~~~~~~~~

- This file contains authorization service actions like creating new permissions , validating access.
"""

# future
from __future__ import unicode_literals

# 3rd party

# rest-framework
from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

# Django
from django.shortcuts import get_object_or_404


# local

# own app
from authorization import serializers, models


class AuthorizationPolicyViewSet(viewsets.ModelViewSet):
    """Authorization Viewset, every authorization http request handles by this class

    """
    model = models.AuthPolicy
    queryset = model.objects.all()
    serializer_class = serializers.AuthorizationPolicySerializer
    # TODO : remove AllowAny permission with proper permission class
    permission_classes = (permissions.AllowAny, )

    def update_permission_set(self, request, source_pk, perm_pk):
        """Policy Permission set will be updated here

        :param request:
        :param source_pk: policy pk
        :param perm_pk: policy permission pk
        :return: permission set
        """
        object = get_object_or_404(models.AuthPolicyPermissions,
                                   pk=perm_pk,
                                   source=source_pk
                                   )
        serializer = serializers.AuthorizationPolicyUpdateSerializer(instance=object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def destroy_permission_set(self, request, source_pk, perm_pk):
        """Policy Permission set will be deleted here

           :param request:
           :param source_pk: policy pk
           :param perm_pk: policy permission pk
           :return: permission set
        """
        models.AuthPolicyPermissions.objects\
            .filter(pk=perm_pk,
                    source=source_pk
                    )\
            .delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

    def validate_policy_permission(self, request):
        """check authorization w.r.t target

        """
        serializer = serializers.PolicyValidateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        object = get_object_or_404(models.AuthPolicyPermissions,
                                   target=serializer.data.get('resource'),
                                   source__source=serializer.data.get('source')
                                   )

        response = serializer.check_perm(object, serializer.data.get('action'))

        return Response({'allowed': response}, status=status.HTTP_200_OK)




