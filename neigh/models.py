from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Neighbourhood(models.Model):
    name = models.CharField(max_length=200)
    hood_location = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    hood_photo = models.ImageField(upload_to='images/')
    admin = models.ForeignKey(User, on_delete=models.CASCADE, related_name='admin')

    def __str__(self):
        return self.name
        

    def save_neigborhood(self):
        self.save()

    def delete_neigborhood(self):
        self.delete()

    @classmethod
    def find_neigborhood(cls, hood_id):
        return cls.objects.filter(id=hood_id)

    @property
    def occupants_count(self):
        return self.neighbourhood_users.count()

    def update_neigborhood(self):
        hood_name = self.hood_name
        self.hood_name = hood_name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_no = models.IntegerField(default=0)
    email = models.CharField(max_length=30, blank=True)
    profile_pic = models.ImageField(upload_to='images/')
    bio = models.TextField(max_length=500, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.user.username

    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def update_profile(cls, id):
        Profile.objects.get(user_id=id)


class Business(models.Model):
    business_name = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    business_hood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    business_email = models.CharField(max_length=30)
    business_desc = models.TextField(blank=True)


    def __str__(self):
        return f'{self.business_name} business'

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def get_business(cls, business_id):
        business = cls.objects.get(id=business_id)
        return business

    @classmethod
    def business_by_id(cls, id):
        business = Business.objects.filter(id=id)
        return business

    def update_business(self):
        name = self.business_name
        self.business_name = name

    @classmethod
    def search_business(cls, name):
        return cls.objects.filter(business_name__icontains=name).all()

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images')
    content = models.TextField(max_length=300, blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, default='',blank=True)

    def __str__(self):
        return self.title

    def save_post(self):
        return self.save()

    def delete_post(self):
        self.delete()
