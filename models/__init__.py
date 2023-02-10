#!/usr/bin/env python3
"""importing file storage
creating a variable storage which is an instance of filestorage
call reload() method on the variable storage
"""

from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
