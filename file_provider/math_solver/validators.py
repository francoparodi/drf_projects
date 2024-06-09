import json
import time
from django.db import transaction
from .models import UploadedFile, ProcessLog

def validate_import_data(data_to_validate) -> bool:
    error = False
    data = json.load(data_to_validate)
 
    # if some error into data_to_validate,
    # write record to ProcessLog:
    # status = 'FAILED'
    # action = 'IMPORT
    # content = data_to_validate
    # error = json errors
    #
    # return True
    return error
