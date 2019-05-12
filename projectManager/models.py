from django.db import models

# Model for issueProjects
class IssueProject(models.Model):

    projectName = models.CharField(max_length=30)

    def __str__(self):
        return "{}".format(self.projectName)
