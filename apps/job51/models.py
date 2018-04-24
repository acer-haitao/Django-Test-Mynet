from django.db import models

# Create your models here.
class job51(models.Model):
    job = models.CharField(max_length=256)
    company = models.CharField(max_length=512)
    address = models.CharField(max_length=512)
    wages = models.CharField(max_length=256)
    date = models.CharField(max_length=256)
    jobname = models.CharField(max_length=256)
    joburl = models.CharField(max_length=512)
    jobtxt = models.CharField(max_length=512,blank = True)
    jobaddress = models.CharField(max_length=256,blank = True)

    def __str__(self):
        tp = '<job51:[job:{job},company:{company},address:{address},wages:{wages},date:{date},jobname:{jobname},joburl:{joburl},jobtxt:{jobtxt}]>'
        return tp.format(job = self.job,company = self.company,address =self.address,wages = self.wages,date = self.date,jobname = self.jobname,joburl = self.joburl,jobtxt = self.jobtxt )