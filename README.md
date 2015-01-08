# str2bool

Python library to convert a string to boolean(True, False), by guessing the approximate meaning of the input string. 

The string can range from ('y' / 'n') to ('yes', 'no') in most regular human languages. Ideally, someday it will be able to detect boolean-lity of large sentences. But, now it can sense only basic words in many languages.

## Current supported languages:
 * English
 * Bengali
 * Dutch
 * Polish
 * Arabic
 * Chinese
 * And, many more ...
 * 
 
## Example usage

    >>> import str2bool as s2b
    >>> s2b('True')
        True
    >>> s2b('0')
        False
    >>> s2b('Tak')  # polish
        True
    >>> s2b('না')   # bengali
        False
