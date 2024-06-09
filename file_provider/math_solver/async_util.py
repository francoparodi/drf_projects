import time
from django.db import transaction
from .models import UploadedFile, ProcessLog

def async_run_solution():
    while True:
        time.sleep(10)
        try:
            with transaction.atomic():
                pass
                # Retrieve older record with status = "CREATED"
                # Change its value to "VALIDATING"
                # Execute validations:
                # If validations NOT PASS:
                #  1) insert record to ProcessLog with status "FAIL"
                #  2) change UploadedFile status to "PROCESSED"
                # If validations PASS:
                #  1) run solver process and wait for it to end
                #     Run solver:
                #       a) insert record to Solution table with status "RUNNING" 
                #       b) at the end, update record Solution table with status "COMPLETED"      
                #     If run Solver fail, 
                #       b) insert record to Solution table with status ""   
                #  2) change UploadedFile status to "PROCESSED"
                
                # uploaded_file = UploadedFile.objects.first()
                # if uploaded_file:
                #     # Copia il record nella tabella Validation
                #     ProcessLog.objects.create(
                #         file_name=uploaded_file.file_name,
                #         file_content=uploaded_file.file_content
                #     )
                #     # Elimina il record dalla tabella UploadedFile
                #     uploaded_file.delete()
        except Exception as e:
            print(f"Errore durante la copia del file: {e}")