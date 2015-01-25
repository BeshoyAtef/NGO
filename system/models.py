from django.db import models

class application(models.Model):
	applicantName=models.CharField(max_length=140)
	caseType=models.ForeignKey('caseType')
 	description=models.TextField()
 	status=models.ForeignKey('caseStatus')
 	photoShootingDate=models.DateField()

 	
 	def __unicode__(self):
 		return self.applicantName


class caseType(models.Model):
	caseType=models.CharField(max_length=140)
	def __unicode__(self):
		return self.caseType

class caseStatus(models.Model):
	status=models.CharField(max_length=140)
	def __unicode__(self):
		return self.status

