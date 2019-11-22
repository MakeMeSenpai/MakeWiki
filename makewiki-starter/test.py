import unittest

from django.test import TestCase
from django.contrib.auth.models import User
from wiki.models import Page

# Create your tests here.
class WikiTestCase(TestCase):
    def test_true_is_true(self):
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        """ Tests the slug generated when ssaving a Page. """
        # Create a user for this test.
        user = User()
        user.save()

        # Create and save Page to database
        page = Page(title="My Test Page", content="test")
        page.save()

        self.assertEqual(page.slug, 'my-test-page')

    def test_multiple_pages(self):
        # Create a user for this test.
        user = User()
        pass
