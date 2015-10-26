[![Build Status](https://travis-ci.org/kmonsoor/str2bool.svg?branch=master)](https://travis-ci.org/kmonsoor/str2bool)
[![License](https://img.shields.io/github/license/mashape/apistatus.svg)](http://kmonsoor.mit-license.org/)

# str2bool  :  String to Boolean conversion

a simple multi-lingual utility function to convert a string to boolean i.e. True, False,
by guessing the approximate meaning of the input string.
By default, it will return `False`. Return ``True`` ONLY if input is certainly a 'true'-ish word e.g. 'Positive', 'yeah' etc.

Maybe, someday it will be able to detect "boolean"-lity of large sentences.
But, now it can sense only single AND basic words in many languages.


### Currently supported languages:
 * English
 * Bengali
 * Dutch
 * Polish
 * Arabic
 * Chinese
 * Korean
 * Spanish
 * Ukrainian
   And, some more ...

Please consider adding your language-specific "yes"|"True"-ish words. See **Contribution** section below.

## Installation
    pip install git+git://github.com/kmonsoor/str2bool.git
 
## Example usage
    >>> import str2bool as s2b
    >>> print(s2b.supported_languages)
    ['EN', 'BN', 'AR', 'NL', 'ES', 'KO', 'JA', 'ZH', 'TL', 'VI']
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

## Contribution

 * To word new list in the "True-ish" checklist, please:
 
   1. Append the "yes"|"True"-ish word(s) at the end of the ``truish_words`` list, 
   2. update ``supported_languages`` list, and 
   3. create a pull-request.
 
 * Please add your suggestion, feature-request, constructive criticism, bug as __issue__ on this GitHub repo
 * Even your generic observation, word-of-wisdom, inspiration, or just "Thanks, buddy" is highly welcome. Please send them to my email: k (at) kmonsoor (dot) com
 * Also, I would love to know any use-case where this tiny library is helping. :) 

## License
``str2bool`` is released as open-source software under the MIT License (MIT). for more information, please visit http://kmonsoor.mit-license.org/

Ciao !
