from .models import Business,Neighbourhood,Post,Profile
from django.contrib.auth.models import User
from django.test import TestCase
import datetime


#Test for Classes


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user=User(username='username',password='password')
        self.user.save()
        self.neighborhood=Neighbourhood(name='kapsa',hood_location='katana',description='The best neighborhood',admin=self.user,hood_photo='image.jpg')
        self.neighborhood.save()
        self.profile=Profile(id=1,id_no=32435676,email='admin@gmail.com',profile_pic='prof.jpg',bio='software Engineer',neighbourhood=self.neighborhood,user=self.user)

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.profile.save_profile()
        profile = Profile.objects.all()
        self.assertTrue(len(profile) > 0)

    def test_delete_profile(self):
        self.profile.delete_profile()
        testsaved = Profile.objects.all()
        self.assertFalse(len(testsaved) > 0)

    def test_update_profile(self):
        self.profile.save_profile()
        self.profile.update_profile(self.profile.user_id)
        self.profile.save_profile()
        self.assertTrue(Profile,self.profile.user)

class BusinessTest(TestCase):
    def setUp(self):
        self.user=User(username='username',password='password')
        self.user.save()
        self.neighborhood=Neighbourhood(name='kapsa',hood_location='katana',description='The best neighborhood',admin=self.user,hood_photo='image.jpg')
        self.neighborhood.save()
        self.buss=Business(user=self.user,business_name='BenTec',business_hood=self.neighborhood,business_email='bentec@gmail.com',business_desc='The best mall around')
        self.buss.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.buss,Business))

    def test_save_business(self):
        self.buss.save_business()
        buss=Business.objects.all()
        self.assertTrue(len(buss)>0)
    
    def test_delete_business(self):
        self.buss.delete_business()
        buss=Business.objects.all()
        self.assertTrue(len(buss)>0)


class PostTest(TestCase):
    def setUp(self):
        self.user=User(username='username',password="password")
        self.user.save()
        self.neighborhood=Neighbourhood(name='kapsa',hood_location='katana',description='The best neighborhood',admin=self.user,hood_photo='image.jpg')
        self.neighborhood.save()
        self.post=Post(user=self.user,title='kkl',image='image.png',content='post test',created=datetime.datetime,neighbourhood=self.neighborhood)
        self.post.save()

    def test__instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_save_post(self):
        self.post.save_post()
        post=Post.objects.all()
        self.assertTrue(len(post)>0)

    def test_delete_post(self):
        self.post.delete_post()
        post=Post.objects.all()
        self.assertTrue(len(post)>0)

        

