import unittest

from ok import Key


class KeyTest(unittest.TestCase):

    def test_key(self):
        class User(Key):
            pass

        self.assertEqual(User().key, 'User')

    def test_field_access(self):
        class User(Key):
            fields = ['timeline', 'followers', 'following']

        self.assertEqual(User('mixxorz').timeline, 'User:mixxorz:timeline')

    def test_class_key_access(self):
        class User(Key):
            pass

        self.assertEqual(User('mixxorz').key, 'User:mixxorz')

    def test_subkey_access(self):
        class City(Key):
            pass

        class Province(Key):
            subkeys = [City]

        class Country(Key):
            subkeys = [Province]

        self.assertEqual(Country('PH').Province('Metro Manila').City('Manila').key,  # noqa
                         'Country:PH:Province:Metro Manila:City:Manila')

    def test_string_subkey_access(self):
        self.assertEqual(Parent('foo').Refer('bar').key,
                         'Parent:foo:Refer:bar')

    def test_string_subkey_relative_access(self):
        self.assertEqual(ParentRelative('foo').ReferRelative('bar').key,
                         'ParentRelative:foo:ReferRelative:bar')

    def test_string_subkey_same_file_relative_access(self):
        self.assertEqual(ParentSame('foo').ReferSame('bar').key,
                         'ParentSame:foo:ReferSame:bar')

    def test_empty_id(self):
        class Twitter(Key):
            fields = ['tweets']

        self.assertEqual(Twitter().tweets, 'Twitter:tweets')

    def test_class_key(self):
        class Twitter(Key):
            class_key = 'twitter'

        self.assertEqual(Twitter().key, 'twitter')

    def test_should_accept_non_strings(self):
        class User(Key):
            fields = ['tweets']

        self.assertEqual(User(123).tweets, 'User:123:tweets')

    def test_class_str(self):
        class User(Key):
            pass

        self.assertEqual('%s' % User('mixxorz'), 'User:mixxorz')


class Parent(Key):
    subkeys = ['ok.tests.module_test.Refer']


class ParentRelative(Key):
    subkeys = ['..module_test.ReferRelative']


class ParentSame(Key):
    subkeys = ['.ReferSame']


class ReferSame(Key):
    pass
