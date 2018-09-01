#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import bulrush

AUTHOR = 'Sean Ammirati'
SITENAME = 'Stats Works'
SITESUBTITLE = 'Making Statistics Work for You'
SITEURL = 'statsworks.github.io'
SIDEBAR_NAME = AUTHOR
SIDEBAR_EMAIL = 'ammirati.sean@gmail.com'
SIDEBAR_TAGS = ['Statistics',
                'Data Science',
                'Machine Learning',
                'Python',
                'R'
                ]
MENUITEMS = [('Home', '/'),
             ('Topics', '/pages/topics'),
             ('About', 'pages/about'),
             ]

DEFAULT_METADATA = {
    'status': 'draft',
}

PATH = 'content'

MARKUP = ('md', 'ipynb')
PLUGIN_PATHS = ['./plugins', './pelican-plugins']
PLUGINS = ['ipynb.markup', 'render_math', 'better_codeblock_line_numbering',
           'assets']
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5'
}

ARTICLE_URL = 'articles/{date:%Y}/{date:%b}/{date:%d}/{slug}/'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'English'

THEME = bulrush.PATH
JINJA_ENVIRONMENT = bulrush.ENVIRONMENT
JINJA_FILTERS = bulrush.FILTERS
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
