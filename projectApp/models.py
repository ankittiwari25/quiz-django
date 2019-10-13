from django.db import models

# Create your models here.
class Register(models.Model):

    name = models.CharField(max_length=50)  
    email = models.EmailField()
    password = models.CharField(max_length=50)
    #con_password = models.CharField(max_length=50)
    
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

class Question(models.Model):
    #question_id=models.AutoField
    question=models.CharField(max_length=250)
    op1=models.CharField(max_length=250)
    op2=models.CharField(max_length=250)
    op3=models.CharField(max_length=250)
    ans=models.CharField(max_length=250)



    # def __int__(self):
    #     return self.question_id

class Questions(models.Model):
    CAT_CHOICES = (
    ('java','Java'),
    ('c','C'),
    ('python','Python'),
    ('android','Android')
    )
    question = models.CharField(max_length = 250)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    catagory = models.CharField(max_length=20, choices = CAT_CHOICES)

    class Meta:
        ordering = ('-catagory',)

    def __str__(self):
        return self.question


class Advancejava(models.Model):
  
    question = models.CharField(max_length = 250)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.question

class C(models.Model):
  
    question = models.CharField(max_length = 250)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.question


class Advancepython(models.Model):
  
    question = models.CharField(max_length = 250)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.question

class Advanceandroid(models.Model):
  
    question = models.CharField(max_length = 250)
    optiona = models.CharField(max_length = 100)
    optionb = models.CharField(max_length = 100)
    optionc = models.CharField(max_length = 100)
    optiond = models.CharField(max_length = 100)
    answer = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.question


class Result(models.Model):
  
    id = models.AutoField
    name = models.CharField(max_length = 100)
    category=models.CharField(max_length=250)
    score = models.PositiveIntegerField(max_length = 100)
    total = models.PositiveIntegerField(max_length = 100)
    date = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.name

