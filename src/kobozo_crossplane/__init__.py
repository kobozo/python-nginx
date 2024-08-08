from kobozo_crossplane.common.formatter import format
from kobozo_crossplane.ext.lua import LuaBlockPlugin
from kobozo_crossplane.helpers.lexer import lex
from kobozo_crossplane.nginx_dumper import build
from kobozo_crossplane.nginx_parser import parse

__all__ = ['parse', 'lex', 'build', 'format']

__title__ = 'kobozo-crossplane'
__summary__ = 'Reliable and fast NGINX configuration file parser.'
__url__ = 'https://github.com/kobozo/crossplane'

__version__ = '0.1.0'

__author__ = 'Yannick De Backer'
__email__ = 'ydb@trustbuilder.com'

__license__ = 'Apache 2.0'
__copyright__ = 'Copyright 2018 NGINX, Inc.'

default_enabled_extensions = [LuaBlockPlugin()]
for extension in default_enabled_extensions:
    extension.register_extension()
