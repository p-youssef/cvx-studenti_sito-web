from django.db import models





class Univesity(models.Model):
    name            = models.CharField(max_length=100)
    city            = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.name} ({self.city})'



class Scholarship(models.Model):
    name            = models.CharField(max_length=100)
    university      = models.OneToOneField(Univesity, on_delete=models.CASCADE)
    about           = models.TextField(max_length=100)
    support_contacts       = models.TextField(max_length=100)

    
    def __str__(self):
        return self.name



class ScholarshipSession(models.Model):
    
    scholarship  = models.OneToOneField(Scholarship, on_delete=models.CASCADE)
    session        = models.CharField(max_length=100)
    about       = models.TextField()
    apply_link  = models.URLField()
    
    def __str__(self):
        return f'{self.scholarship} ({self.session})'



class ProgramCategory(models.Model):
    name        = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name



class Program(models.Model):
    name        = models.CharField(max_length=100)
    university  = models.OneToOneField(Univesity, on_delete=models.CASCADE)
    degree_type = models.CharField(choices = [(1, 'Bachler'), (2, 'Master'), (3, 'PHD')], max_length=100)
    program_category = models.OneToOneField(ProgramCategory, null=True, on_delete=models.SET_NULL)
    about       = models.TextField()

    
    def __str__(self):
        return self.name