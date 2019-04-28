from django.db import models
from django.contrib.auth.models import User

# Model for issues
class Issue(models.Model):
    
    projectName = models.CharField(max_length=30)
    issueType = models.CharField(max_length=30)
    issuePriority = models.CharField(max_length=50)
    title = models.CharField(max_length=100)
    affectsVersion = models.CharField(max_length=30)
    foundInBuild = models.CharField(max_length=30)
    description = models.TextField()
    resolution = models.CharField(max_length=30)
    status = models.CharField(max_length=30)
    reporter = models.ForeignKey(User, default=None)
    
    createdDate = models.DateTimeField(auto_now_add=True)
    updatedDate = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}".format(self.projectName, self.id)

# Model for issue comments - 1 - many relationship i.e. one issue can have multiple comments
class IssueComments(models.Model):

    issueId = models.ForeignKey(Issue, default=None, on_delete=models.CASCADE)

    user = models.ForeignKey(User, default=None)
    comment = models.TextField()
    commentDate = models.DateTimeField(auto_now_add=True)
