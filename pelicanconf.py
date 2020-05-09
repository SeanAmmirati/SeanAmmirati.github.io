#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sean Ammirati'
SITENAME = 'Stats Works'
SITESUBTITLE = 'Making Statistics Work for You'
SITEURL = 'https://seanammirati.github.io'
FEED_DOMAIN = SITEURL
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
             ('About', '/pages/about'),
             ]

DEFAULT_METADATA = {
    'status': 'draft',
}

PATH = 'content'

CATEGORY_URL = "category/{slug}"
CATEGORY_SAVE_AS = "category/{slug}/index.html"
PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'
ARTICLE_URL = 'category/{category}/{slug}.html'
ARTICLE_SAVE_AS = 'category/{category}/{slug}.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tags/'
TAGS_SAVE_AS = 'tags/index.html'

# Favicon
STATIC_PATHS = ['images', 'extra/favicon.ico', 'figure']
EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'}
}
# Category options
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True

MARKUP = ('md', 'rmd', 'ipynb')
from pelican_jupyter import markup as nb_markup
PLUGIN_PATHS = ['./plugins', './pelican-plugins']
PLUGINS = [nb_markup, 'render_math',
           'better_codeblock_line_numbering',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'rmd_reader', 'neighbors', 'tipue_search']

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    }
}
# Jupyter Notebook
IGNORE_FILES = ['.ipynb_checkpoints']

# R-Markdown compatibility
RMD_READER_RENAME_PLOT = 'directory'
RMD_READER_KNITR_OPTS_CHUNK = {'fig.path': 'figure/'}

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'English'

THEME = 'pelican-themes/elegant'


#Elegant Toggles
LANDING_PAGE_ABOUT = {
        'title': 'A website for statistics, machine learning and programming',
        'details': 'Sean Ammirati, the creator of Stats Works is a Data Scientist from NYC. He enjoys musing over statistical problems and analytical puzzles.'
        }
USE_SHORTCUT_ICONS = True
AUTHORS = {
    u'Sean Ammirati': {
        u'blurb': """ creator of Stats Works. He can be reached on Github, LinkedIn and email.""",
        u'url': 'https://seanammirati.github.io/pages/about'
    },
    }

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
SOCIAL = (
          ('GitHub', 'https://github.com/SeanAmmirati'),
          ('LinkedIn', 'https://www.linkedin.com/in/sean-ammirati-4795a4ba/'),
          ('Email', SIDEBAR_EMAIL)
          )

DEFAULT_PAGINATION = 10

# Disqus for Comments
DISQUS_SITENAME = "statsworks"

DEFAULT_PAGINATION = False
RELATIVE_URLS = True
