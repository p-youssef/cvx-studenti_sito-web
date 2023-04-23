from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class SupportGourp(models.Model):
    name    = models.CharField(max_length=100)
    admin   = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)
    about   = models.TextField()

    def __str__(self):
        return self.name


class SupportGourpUser(models.Model):
    suuport_gourp   = models.OneToOneField(SupportGourp, on_delete=models.CASCADE)
    user                    = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.suuport_gourp} - {self.user}'



class StudentStep(models.Model):
    id_name         = models.CharField(max_length=100)  
    name            = models.CharField(max_length=100)
    requirements    = models.TextField()
    notes           = models.TextField()
    suuport_gourp   = models.OneToOneField(SupportGourp, null=True, on_delete=models.SET_NULL)
    help_contacts   = models.TextField()
    
    def __str__(self):
        return self.name





class Profile(models.Model):
    user                    = models.OneToOneField(User, on_delete=models.CASCADE)
    resedence               = models.CharField(max_length=100)
    cvx_acceptance          = models.IntegerField(default = 0)
    current_step            = models.OneToOneField(StudentStep, null=True, on_delete=models.SET_NULL)
    step_status             = models.IntegerField( default=1)
    step_note               = models.TextField()
    steps_log               = models.JSONField()
    cv                      = models.URLField()
    phone_numer             = models.CharField(max_length = 100)
    study_log               = models.JSONField()
    followed_scholarships   = models.JSONField()
    earned_scholarships     = models.JSONField()

    

    @receiver(post_save, sender=User) 
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)


    def __str__(self):
        return self.user.username
    



