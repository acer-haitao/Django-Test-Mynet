from django.db import models

# Create your models here.
class comment(models.Model):
    txt = models.TextField()#评论内容
    footer=models.CharField(max_length=256)#评论脚本
    def __str__(self):
        tp = '<comment:[txt:{txt},footer:{footer}]>'
        return tp.format(txt=self.txt,footer=self.footer)
