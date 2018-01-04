#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'admin'
SITENAME = u'Valkyrie Studios'
SITEURL = ''
THEME = "themes/my_notmyidea"
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

MENUITEMS = (
    ('首页', '/'),
    ('家长监护', '/parents.html'),
    ('产品中心', '/products.html'),
    ('服务项目', '/services.html'),
    ('充值中心', '/pay.html'),
    ('加入我们', '/careers.html'),
    ('联系我们', '/contactUs.html'),
)

# Blogroll
LINKS = ()
# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['plugins']
PLUGINS = ['photos']

CUR_DIR = os.path.dirname(__file__)
PHOTO_LIBRARY = "./content/images"