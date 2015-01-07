# -*- coding: utf-8 -*-

__title__ = 'String to Boolean'
__version__ = '0.2'
__author__ = 'khaled monsoor'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015-2015 khaled monsoor'
__date_of_birth__ = '2015.01.07'


# list of supported languages in ISO_639-1_code
supported_languages = ['EN', 'BN', 'AR', 'NL', 'ES', 'KO', 'JA', 'ZH', 'TL', 'VI', ]


def string_to_boolean(string):
    return string.lower() in ['yes', 'yeah', 'y', '1', 'ja', 'tak', 'yep', 'true', 'right', 'si', 'sí', 'da',
                              'jes', 'হ্যা', 'জি', 'Да', 'हाँ', 'ya', 'já', 'hai', 'éé', 'eh', 'cha', 'baht',
                              'نعم', 'aye', 'bai', 'হাঁ', 'affirmative', 'positive', '+ve', '+', '是的', 'oo',
                              'はい', '예', '네']
