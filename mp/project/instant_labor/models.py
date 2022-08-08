from django.db import models

class Credentials(models.Model):
    user = models.CharField(max_length=200)
    passw =models.CharField(max_length=16)
    def _str_(self):
        return self.user
class Worker(models.Model):
    fname      = models.CharField(max_length=200)
    lname      = models.CharField(max_length=200)
    skills     = models.CharField(max_length=200)
    contact_no = models.IntegerField()
    email      = models.EmailField(max_length=200)
    addr       = models.CharField(max_length=200)
    def _str_(self):
        return self.fname
class Owner(models.Model):
    fname      = models.CharField(max_length=200)
    lname      = models.CharField(max_length=200)
    skills_req     = models.CharField(max_length=200)
    contact_no = models.IntegerField()
    email      = models.EmailField(max_length=200)
    addr       = models.CharField(max_length=200)
    def _str_(self):
        return self.fname
class Feedback(models.Model):
    from_per_mail     = models.EmailField(max_length=200)
    to_per_mail      = models.EmailField(max_length=200)
    rating = models.IntegerField()
    feed      = models.CharField(max_length=200)
    def _str_(self):
        return self.to_per_mail
