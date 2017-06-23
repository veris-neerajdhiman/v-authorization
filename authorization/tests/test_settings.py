#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
- authorization.tests.test_settings
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- This file includes test-cases of settings which are required for Authorization micro-service

"""

# future
from __future__ import unicode_literals

# third party
import os

# Django
from django.conf import settings
from django.test import TestCase


class SettingsTestCase(TestCase):
    """Settings Test Case

    """

    def setUp(self):
        """

        """
        self.settings = ('SOURCE_RGX', 'RESOURCE_RGX', )

    def test_environment_variables(self):
        """makes sure settings which are necessary for running Authorization micro-service are defined in settings.

        """

        for key in self.settings:
            if not getattr(settings, key,):
                self.assertFalse('{0} environment settings is not defined.'.format(key))

        self.assertTrue('Environment settings test passed.')


class EnvironmentVariableTestCase(TestCase):
    """Environment Variables Test case

    """
    def setUp(self):
        """

        """
        self.env_variables = (
            'DATABASE_NAME_AUTH',
            'DATABASE_USER',
            'DATABASE_PASSWORD',
            'DATABASE_HOST',
            'DATABASE_PORT',
            'SECRET_KEY',
        )

    def test_env_variables(self):
        """Makes sure necessary env variables are declared.

        """
        for key in self.env_variables:
            try:
                return os.environ[key]
            except KeyError:
                self.assertFalse('{0} environment variable is not defined.'.format(key))
