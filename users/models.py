from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from social_django.models import UserSocialAuth



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
    def get_social_auth_obj(self):
        try:
            return UserSocialAuth.objects.get(user=self.user)
        except UserSocialAuth.DoesNotExist:
            pass
        except MultipleObjectsReturned:
            pass
        return None

    def get_access_token(self):
        if self.user.is_authenticated:
            usa = self.get_social_auth_obj()
            if usa:
                access_token = usa.extra_data.get('access_token')
                # todo: need to verify by facebook token tools
                if access_token:
                    return access_token
        return ''

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)
"""
        img = Image.open(self.image.url)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.url)
"""
    