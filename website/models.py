from django.db import models

# Create your models here.
class Record(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    Name = models.CharField(max_length = 100)
    Age = models.IntegerField()
    Gender = models.CharField(max_length = 50)
    Blood_Type = models.CharField(max_length = 20)
    Medeical_Condition = models.CharField(max_length = 100)
    Date_Of_Admission = models.DateField()
    Doctor_name = models.CharField(max_length = 100)
    Hospital = models.CharField(max_length = 100)
    Insurance_Provider = models.CharField(max_length = 100)
    Billing_Amount = models.FloatField()


    def __str__(self):
        return(f"{self.Name} {self.Gender}")
    
