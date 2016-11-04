"""Dependency injector injections unit tests."""

import unittest2 as unittest

from dependency_injector import providers


class PositionalInjectionTests(unittest.TestCase):

    def test_isinstance(self):
        injection = providers.PositionalInjection(1)
        self.assertIsInstance(injection, providers.Injection)

    def test_get_value_with_not_provider(self):
        injection = providers.PositionalInjection(123)
        self.assertEquals(injection.get_value(), 123)

    def test_get_value_with_factory(self):
        injection = providers.PositionalInjection(providers.Factory(object))

        obj1 = injection.get_value()
        obj2 = injection.get_value()

        self.assertIs(type(obj1), object)
        self.assertIs(type(obj2), object)
        self.assertIsNot(obj1, obj2)


class NamedInjectionTests(unittest.TestCase):

    def test_isinstance(self):
        injection = providers.NamedInjection('name', 1)
        self.assertIsInstance(injection, providers.Injection)

    def test_get_name(self):
        injection = providers.NamedInjection('name', 123)
        self.assertEquals(injection.get_name(), 'name')

    def test_get_value_with_not_provider(self):
        injection = providers.NamedInjection('name', 123)
        self.assertEquals(injection.get_value(), 123)

    def test_get_value_with_factory(self):
        injection = providers.NamedInjection('name',
                                             providers.Factory(object))

        obj1 = injection.get_value()
        obj2 = injection.get_value()

        self.assertIs(type(obj1), object)
        self.assertIs(type(obj2), object)
        self.assertIsNot(obj1, obj2)