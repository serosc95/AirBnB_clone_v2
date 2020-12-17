#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

database = os.getenv('HBNB_TYPE_STORAGE')
if database == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
