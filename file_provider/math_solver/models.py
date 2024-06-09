from django.db import models

# Create your models here.

class Solution(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	# STARTED, COMPLETED
	status = models.CharField(max_length = 64, blank=True)
	input = models.TextField(blank=True)
	output = models.TextField(blank=True)


class ProcessLog(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	# Status: FAILED | PASSED
	status = models.CharField(max_length = 64, default='FAILED', blank=True)
	# Action: IMPORT | SOLVE
	action = models.CharField(max_length = 64, blank=True)
	content = models.JSONField()
	errors = models.JSONField()


class UploadedFile(models.Model):
    content = models.JSONField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
	# Status: CREATED -> VALIDATING -> PROCESSED
    status = models.CharField(max_length = 64, default='CREATED', blank=True)
