from django.db import models

class EmpInfo(models.Model): 
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.EmailField()
    mobileNumber = models.IntegerField()
    salary = models.IntegerField()
    
    
    def __str__(self):
        return self.firstName

    