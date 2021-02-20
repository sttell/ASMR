import json as js
from include import SETTINGS_PATH, DEFAULT_SETTINGS_PATH, LINK_FILE_PATH

"""
Module for working with JSON file format and uploading / uploading settings
"""


def load(file):
    """

    """
    with open(file, 'r') as read_file:
        container = js.load(read_file)
    return container


def write(file, data):
    with open(file, 'w') as write_file:
        js.dump(data, write_file)


def load_default_settings():
    with open(DEFAULT_SETTINGS_PATH, 'r') as read_file:
        container = js.load(read_file)
    return container


def load_settings():
    with open(SETTINGS_PATH, 'r') as read_file:
        container = js.load(read_file)
    return container


def save_settings(data):
    with open(SETTINGS_PATH, 'w') as write_file:
        js.dump(data, write_file)


def load_links():
    with open(LINK_FILE_PATH, 'r') as read_file:
        container = js.load(read_file)
    return container


def update_links(data):
    with open(LINK_FILE_PATH, 'w') as write_file:
        js.dump(data, write_file)
