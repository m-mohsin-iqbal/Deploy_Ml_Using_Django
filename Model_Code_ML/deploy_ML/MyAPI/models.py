from django.db import models

# Create your models here.
class approvals(models.Model):
    GENDER_CHOICES=(('Male','Male'),('Female','Female'))
    MARRIED_CHOICES = (('Yes', 'Yes'), ('No', 'No'))
    GRADUATED_CHOICES=(('Graduate', 'Graduate'), ('Not_Graduate', 'Not_Graduate'))
    SELF_EMPLOYED = (('Yes', 'Yes'), ('No', 'No'))
    PROPERTY_CHOICES = (('Rural', 'Rural'), ('Semiurban', 'Semiurban'),('Urban','Urban'))
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Depandants=models.IntegerField()
    Applicationincome=models.IntegerField()
    Coapplicationincome=models.IntegerField()
    Loanamt=models.IntegerField()
    Loanterm=models.IntegerField()
    Credithistory=models.IntegerField()
    Gender=models.CharField(max_length=15,choices=GENDER_CHOICES)
    Married=models.CharField(max_length=15,choices=MARRIED_CHOICES)
    Graduatededucation=models.CharField(max_length=15,choices=GRADUATED_CHOICES)
    Selfemployed=models.CharField(max_length=15,choices=SELF_EMPLOYED)
    Area=models.CharField(max_length=15,choices=PROPERTY_CHOICES)

    def __str__(self):
        return self.Firstname

