#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- authorization.tests.test_views
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- This file includes Test cases for Views .

"""

# future
from __future__ import unicode_literals

# 3rd party
import json

# Django
from django.test import TestCase
from django.core.urlresolvers import reverse

# local
from authorization.models import AuthPolicy, AuthPolicyPermissions


class AuthTestCase(TestCase):
    """Handles Auth Views Test Cases

    """

    def setUp(self):
        """

        """
        source = 'user:2db95648-b5ea-458a-9f07-a9ef51bbca21:'
        target = 'vrn:resource:organization:'
        self.policy = AuthPolicy.objects.create(source=source)
        self.policy_perm = AuthPolicyPermissions.objects.create(
            source=self.policy,
            target=target,
            create=True,
            update=True,
            read=True,
            delete=False
        )

    def test_policy_add(self):
        """Test Policy Add & then Validate (Authorized + UnAuthorized)

        """
        url = reverse('auth-urls:authorization-policy-create')

        data = json.dumps({
            'source': 'organization:2db95648-b5ea-458a-9f07-a9ef51bbca21:',
            'source_permission_set': [
                {
                    'target': 'vrn:resource:member:',
                    'create': True,
                    'read': True,
                    'update': True,
                    'delete': True
                }]
        })

        create_response = self.client.post(url, content_type='application/json', data=data)

        if create_response.status_code == 201:
            url = reverse('auth-urls:authorization-policy-validate')
            # Validate Authorized Access
            v_data = {
                "resource": "vrn:resource:member:",
                "source": "organization:2db95648-b5ea-458a-9f07-a9ef51bbca21:",
                "action": "create"
            }

            verify_response = self.client.post(url, data=v_data)

            self.assertEqual(verify_response.status_code, 200)

            # Validate Un-Authorized Access
            v_data = {
                "resource": "vrn:resource:member:",
                "source": "organization:b0b66cee-1375-43f7-a75e-01d229336f13:",
                "action": "create"
            }

            verify_response = self.client.post(url, data=v_data)

            self.assertEqual(verify_response.status_code, 404)

        self.assertEqual(create_response.status_code, 201)

    def test_policy_detail(self):
        """Test Policy fetch (single)

        """
        url = reverse('auth-urls:authorization-policy-detail', args=(self.policy.pk, ))

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_policy_list(self):
        """Test Source Policy list (multiple policies)

        """
        url = reverse('auth-urls:authorization-policy-list')

        response = self.client.get(url, data={'source': self.policy.source})

        self.assertEqual(response.status_code, 200)

    def test_policy_delete(self):
        """Test Policy delete

        """
        url = reverse('auth-urls:authorization-policy-detail', args=(self.policy.pk, ))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)

    def test_policy_permission_update(self):
        """Test Policy Permission set update

        """
        url = reverse('auth-urls:authorization-policy-update-delete', args=(self.policy_perm.source.pk,
                                                                            self.policy_perm.pk, ))

        data = json.dumps({
            'create': True,
            'read': True,
            'update': True,
            'delete': True
        })

        response = self.client.patch(url, content_type='application/json', data=data)

        self.assertEqual(response.status_code, 204)

    def test_policy_permission_delete(self):
        """Test Policy Permission set Delete

        """
        url = reverse('auth-urls:authorization-policy-update-delete', args=(self.policy_perm.source.pk, self.policy_perm.pk, ))

        response = self.client.delete(url)

        self.assertEqual(response.status_code, 204)
