from django.db import models

# Create your models here.
class URLDB(models.Model):
    Num = models.IntegerField()
    Name =models.CharField(max_length=100)
    URL =models.CharField(max_length=100)
    Time = models.CharField(max_length=100)
    #在数据库里能显示对应的字段
    def __str__(self):
        tpl = '<URLDB:[Num={Num},Name={Name},URL={URL},Time={Time}]>'
        return tpl.format(Num=self.Num,Name=self.Name,URL=self.URL,Time=self.Time)


class TabName(models.Model):
    Num = models.IntegerField()
    TabName = models.CharField(max_length=100)
    def __str__(self):
        tpl = '<TabName:[Num={Num},TabName={TabName}]>'
        return tpl.format(Num=self.Num,TabName=self.TabName)
    class Meta:
        verbose_name = u"TabName"
        verbose_name_plural = verbose_name