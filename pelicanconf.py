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

CATEGORY_URL = "/category/{slug}"
CATEGORY_SAVE_AS = "/category/{slug}/index.html"
PAGE_URL = '/{slug}/'
PAGE_SAVE_AS = '/{slug}/index.html'
ARTICLE_URL = '/{category}/{slug}.html'
ARTICLE_SAVE_AS = '/{category}/{slug}.html'

# Category options 
USE_FOLDER_AS_CATEGORY = True
DISPLAY_CATEGORIES_ON_MENU = True 

MARKUP = ('md', 'rmd', 'ipynb')
PLUGIN_PATHS = ['./plugins', './pelican-plugins']
PLUGINS = ['ipynb.markup', 'render_math',
           'better_codeblock_line_numbering',
           'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube',
            'liquid_tags.vimeo',
           'liquid_tags.include_code', 'liquid_tags.notebook',
           'rmd_reader']
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5'
}
# Jupyter Notebook 
IGNORE_FILES = ['.ipynb_checkpoints']

# R-Markdown compatibility
STATIC_PATHS = ['figure']
RMD_READER_RENAME_PLOT = 'directory'
RMD_READER_KNITR_OPTS_CHUNK = {'fig.path': 'figure/'}

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'English'

THEME = 'html5-dopetrope'
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
          ('Kaggle', 'https://www.kaggle.com/seanammirati'),
          ('Email', SIDEBAR_EMAIL)
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
