#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Cibee'
SITENAME = u'Latchi'
SITEURL = ''

PATH = 'content'
PLUGIN_PATHS = ['plugins','pelican-plugins']
PLUGINS = ['yuicompressor']

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

DATE_FORMATS = {
    'fr': '%d %b %Y'
}

STATIC_PATHS = ['static']

THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

# code blocks with line numbers
PYGMENTS_RST_OPTIONS = {'linenos': 'table'}

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
