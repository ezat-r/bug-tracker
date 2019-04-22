from django.db import models

class Issue(models.Model):
    
    projectName = models.CharField(max_length=30)
    issueType = models.CharField(max_length=30)
    issuePriority = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    affectsVersion = models.CharField(max_length=30)
    foundInBuild = models.CharField(max_length=30)
    description = models.TextField()
    status = models.CharField(max_length=30)
    reporter = models.CharField(max_length=30)
    
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{}-{}".format(self.projectName, self.id)
    
