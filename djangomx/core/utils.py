# coding: utf-8
import os
from datetime import datetime

from django.utils.text import slugify


def get_filename(ext):
    """
    Returns a unique file name based on its extension parameter
    """
    ts = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    return '%s%s' % (ts, ext)


def get_upload_to(instance, filename):
    """
    Returns a file name, extension and directory.
    """
    name, ext = os.path.splitext(filename)
    return '{}'.format(get_filename(ext))


def generate_filepath(directory=''):
    """
    Returns the timestampped file name, extension and directory specified in the args.
    """
    try:
        return '{}/{}'.format(directory, get_upload_to)
    except TypeError:
        return get_upload_to


def truncated_slugify(string, max_length=75):
    """
    Returns a slug, excludes keywords and truncates it to a default of 75 characters.
    """
    if len(string) > max_length:
        truncated_string = ''
        for word in string.split(' '):
            if len(word) < 1:
                next_len = len(truncated_string) + len(word)
                if next_len < max_length:
                    truncated_string += '{0}{1}'.format(word, ' ')
                elif next_len == max_length:
                    truncated_string += '{0}'.format(word)
                    break

        string = truncated_string.strip(' ')

    return slugify(string)
