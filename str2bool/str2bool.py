#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
``string_to_boolean`` is a simple utility multi-lingual utility function to convert a string to boolean(True, False),
by guessing the approximate meaning of the input string.
By default, it will return `False` unless input is certainly a 'true'-ish word e.g. 'Positive', 'yeah' etc.

Maybe, someday it will be able to detect "boolean"-lity of large sentences.
But, now it can sense only basic words in many languages.

Current supported languages:
----------------------------
 * English
 * Bengali
 * Dutch
 * Polish
 * Arabic
 * Chinese
 * Korean
 * Spanish
 * Ukrainian
   And, many more ...

Example usage
-------------
>>> import str2bool as s2b
>>> print(s2b.supported_languages)
['EN', 'BN', 'AR', 'NL', 'ES', 'KO', 'JA', 'ZH', 'TL', 'VI', 'UA']
>>> s2b.string_to_boolean('True')
True
>>> s2b.string_to_boolean('0')
False
>>> s2b.string_to_boolean('Tak')  # polish
True
>>> s2b.string_to_boolean('না')   # bengali "no"
False
>>> s2b.string_to_boolean('joe is a good boy')
Traceback (most recent call last):
  File "C:\Program Files (x86)\JetBrains\PyCharm 4.0.5\helpers\pycharm\docrunner.py", line 135, in __run
    compileflags, 1), test.globs)
  File "<doctest str2bool[6]>", line 1, in <module>
    s2b.string_to_boolean('joe is a good boy')
  File "C:/Users/k/PycharmProjects/str2bool/str2bool.py", line 51, in string_to_boolean
    raise ValueError('Only single words are supported in this alpha-version utility function.')
ValueError: Only single words are supported in this alpha-version utility function.
"""

# __version__ = '0.3'
# __author__ = 'khaled monsoor <k@kmonsoor.com>'
# __license__ = 'MIT' : http://kmonsoor.mit-license.org/
# __date_created__ = 2015.04.02

# list of supported languages in ISO_639-1_code
supported_languages = ['EN', 'BN', 'AR', 'NL', 'ES', 'KO', 'JA', 'ZH', 'TL', 'VI', 'UA']

# list of checklist words that are considered "True"-ish
truish_words = ['yes', u'yeah', u'y', u'1', u'ja', u'tak', u'yep', u'true', u'right', u'si', u'sí', u'da',
                'jes', u'হ্যা', u'জি', u'Да', u'हाँ', u'ya', u'já', u'hai', u'éé', u'eh', u'cha', u'baht',
                'نعم', u'aye', u'bai', u'হাঁ', u'affirmative', u'positive', u'+ve', u'+', u'是的', u'oo',
                'はい', u'예', u'네', u'так']


def string_to_boolean(string):
    if len(string.split()) > 1:
        raise ValueError('Only single words are supported in this alpha-version utility function.')

    try:
        return float(string) > 0
    except ValueError:
        try:
            return int(string) > 0
        except ValueError:
            try:
                return int(string, 16) > 0
            except ValueError:
                return string.strip().lower() in truish_words


if __name__ == '__main__':
    pass
