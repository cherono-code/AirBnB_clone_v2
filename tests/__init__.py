#!/usr/bin/python3
"""Tests for the AirBnb clone modules.
"""
import os
from typing import TextIO
from models.engine.file_storage import FileStorage


def clear_stream(stream: TextIO):
    """Clears the contents of a given stream

    Args:
        stream (TextIO): stream to be cleared.
    """
    if stream.seekable():
        stream.seek(0)
        stream.truncate(0)


def delete_file(file_path: str):
    """Removes a file if it exists.
    Args:
        file_path (str): name of the file to be removed.
    """
    if os.path.isfile(file_path):
        os.unlink(file_path)


def reset_store(store: FileStorage, file_path='file.json'):
    """Resets items in given store.
    Args:
        store (FileStorage): FileStorage to be reset.
        file_path (str): path to store's file.
    """
    with open(file_path, mode='w') as file:
        file.write('{}')
        if store is not None:
            store.reload()


def read_text_file(file_name):
    """Reads contents of a given file.

    Args:
        file_name (str): name of the file to read.

    Returns:
        str: contents of the file if it exists.
    """
    lines = []
    if os.path.isfile(file_name):
        with open(file_name, mode='r') as file:
            for line in file.readlines():
                lines.append(line)
    return ''.join(lines)


def write_text_file(file_name, text):
    """Writes a text to a specific file.

    Args:
        file_name (str): The name of the file to write to.
        text (str): contents of the file.
    """
    with open(file_name, mode='w') as file:
        file.write(text)
