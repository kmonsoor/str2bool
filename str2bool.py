## -*- coding: utf-8 -*-

__title__ = 'String to Boolean'
__version__ = '0.2'
__author__ = 'khaled monsoor'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015-2015 Hynek Schlawack'
__date_of_birth__ = '2015.01.07'


# list of supported languages in ISO_639-1_code
supported_languages = ['EN', 'BN', 'AR', 'NL', 'ES', 'KO', 'JA', 'ZH', 'TL', 'VI',]  


def string_to_boolean(string):
    return str(string).lower() in ['yes', 'yeah', 'y', '1', 'ja', 'tak', 'yep', 'true', 'right', 'si', u'sí', 'da', 'jes', u'হ্যা', u'জি', u'Да', u'हाँ', 'ya', u'já', 'hai', u'éé', 'eh', 'cha', 'baht', u'نعم', 'aye', 'bai', 'হাঁ', 'affirmative', 'positive', '+ve', '+', u'是的', u'oo', u'はい', u'예', u'네']
