from django.db import models

# Create your models here.
class Register(models.Model):


    name = models.CharField(max_length=50)  
    email = models.EmailField()
    password = models.CharField(max_length=50)
    con_password = models.CharField(max_length=50)

    def __str__(self):
        return self.name



class Department(models.Model):


        did = models.IntegerField()  
        d_name = models.CharField(max_length=50)  


        def __str__(self):
            return self.d_name





class Semester(models.Model):


            sid = models.IntegerField()  
            s_name = models.CharField(max_length=50)  
    
    
            def __str__(self):
                return self.s_name