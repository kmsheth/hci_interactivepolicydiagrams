from django.db import models

# Create your models here.

class Issue(models.Model):
    code = models.CharField(max_length=30, primary_key=True)
    title = models.CharField(max_length=30)
    #link_address

    def __str__(self):
        return "%s" %(self.title)

class actor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    code = models.CharField(max_length=30, primary_key=True)
    #img address
    #link_address

    def __str__(self):
        return "%s %s" %(self.first_name, self.last_name)

class result(models.Model):
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE)
    actor = models.ForeignKey(actor, on_delete=models.CASCADE)

    def get_code(self):
        return "%s:%s" % (self.actor.code, self.issue.code)

    def __str__(self):
        return "%s on %s" % (self.actor.__str__(), self.issue.__str__())

