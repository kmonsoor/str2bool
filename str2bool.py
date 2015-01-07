## -*- coding: utf-8 -*-

__title__ = 'String to Boolean'
__version__ = '0.1'
__author__ = 'khaled monsoor'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015-2015 Hynek Schlawack'
__date_of_birth__ = '2015.01.07'


# list of supported languages in ISO_639-1_code
supported_languages = ['EN', 'BN', 'AR', 'NL']  


def string_to_boolean(string):
    return str(string).lower() in ['yes', 'yeah', 'y', '1', 'ja', 'tak', 'yep', 'true', 'right', ]
