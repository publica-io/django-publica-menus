#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-publica-menus
------------

Tests for `django-publica-menus` models module.
"""

import os
import shutil
import unittest

from menus import models
from menus import factories


class TestLink(unittest.TestCase):

    def setUp(self):
        self.link = factories.LinkFactory(title='Title1', url='Url1')

    def test_title(self):
        self.assertEqual(self.link.title, 'Title1')

    def test_url(self):
        self.assertEqual(self.link.url, 'Url1')

    def tearDown(self):
        pass


class TestMenu(unittest.TestCase):

    def setUp(self):
        self.menu = factories.MenuFactory(title='Title1', slug='Slug1', enabled=True)

    def test_title(self):
        self.assertEqual(self.menu.title, 'Title1')

    def test_url(self):
        self.assertEqual(self.menu.slug, 'Slug1')

    def test_enabled(self):
        self.assertEqual(self.menu.enabled, True)

    def tearDown(self):
        pass


class MenuItem(unittest.TestCase):

    def setUp(self):
        self.link = factories.LinkFactory(title='Title1', url='Url1')
        self.menu = factories.MenuFactory(title='Title1', slug='Slug1', enabled=True)
        self.menu_item = factories.MenuItemFactory(menu=self.menu, link=self.link,
                                                   order=0, is_featured=True,
                                                   parent=None)

    def test_menu(self):
        self.assertEqual(self.menu, self.menu_item.menu)

    def test_link(self):
        self.assertEqual(self.link, self.menu_item.link)

    def test_order(self):
        self.assertEqual(self.menu_item.order, 0)

    def test_is_featured(self):
        self.assertEqual(self.menu_item.is_featured, True)

    def test_parent(self):
        self.assertEqual(self.menu_item.parent, None)

    def tearDown(self):
        pass