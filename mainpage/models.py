from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField


# Create your models here.
class detail(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, help_text="Write something about your institute.", null=True)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=20)
    address = models.TextField(help_text="")
    address_url = models.URLField(help_text="Enter url of your address from GoogleMaps.")
    embedd_map = models.CharField(max_length=2000)
    whatsapp = models.CharField(max_length=20, help_text="Enter your phone number, i.e. 9898541267")
    facebook = models.CharField(max_length=500, help_text="Enter url of your facebook profile.")
    instagram = models.CharField(max_length=500, help_text="Enter url of instagram profile.")
    google_form_url = models.URLField(help_text="Enter url of google form you created for accepting applications.")
    video_src = models.CharField(max_length=5000, help_text="Enter src of video file from drive.")
    number_of_students = models.IntegerField()
    number_of_faculties = models.IntegerField()
    number_of_courses = models.IntegerField()
    number_of_awards = models.IntegerField()
    owner_image = models.ImageField(upload_to='mainpage/')
    # website = models.URLField(help_text="Enter url of your website.")


    def delete(self, using=None, keep_parents=False):
        self.owner_image.storage.delete(self.owner_image.name)
        super().delete()


    def __str__(self):
        return self.title


class course(models.Model):
    name = models.CharField(max_length=500)
    instructor = models.CharField(max_length=500)
    total_seats = models.IntegerField()
    duration = models.CharField(max_length=100, help_text="i.e. 1 Month, 4 Weeks, 1 Year etc.")
    image = models.ImageField(upload_to='courses/')
    description = models.CharField(max_length=200, help_text="Describe your couse in short here.")
    details = models.TextField(help_text="Enter All Details of your course here.")
    tags = models.CharField(max_length=600, help_text="Enter Tags for your course i.e. photoshop,excel,microsoft office,access etc. Don't forget to seperate them by comma.")
    # google_form_url = models.URLField(help_text="Enter URL of google form for applying to this course.")
    
    # instructor_image = models.ImageField(upload_to='courses/', blank=True, null=True)

    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()
    

    def __str__(self):
        return self.name

class facultie(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='faculties/')
    whatsapp = models.CharField(max_length=20, help_text="Enter your phone number, i.e. 9898541267")
    facebook = models.CharField(max_length=500, help_text="Enter url of your facebook profile.")
    instagram = models.CharField(max_length=500, help_text="Enter url of instagram profile.")
    
    def delete(self, using=None, keep_parents=False):
        self.owner_image.storage.delete(self.owner_image.name)
        super().delete()


    def __str__(self):
        return self.name

class students_review(models.Model):
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to='reviews/')
    review = models.CharField(max_length=500)

    def delete(self, using=None, keep_parents=False):
        self.owner_image.storage.delete(self.owner_image.name)
        super().delete()


    def __str__(self):
        return self.name


class image(models.Model):
    album_name = models.CharField(max_length=100)
    
    main_image1 = models.ImageField(upload_to='images/', null=True, blank=True, help_text="Upload image if you want otherwise default images will be shown.")
    main_image2 = models.ImageField(upload_to='images/', null=True, blank=True, help_text="Upload image if you want otherwise default images will be shown.")
    video_background = models.ImageField(upload_to='images/', null=True, blank=True, help_text="Upload image if you want otherwise default images will be shown.")
    what_we_offer = models.ImageField(upload_to='images/', null=True, blank=True, help_text="Upload image if you want otherwise default images will be shown.")
    about_us_background = models.ImageField(upload_to='images/', null=True, blank=True, help_text="Upload image if you want otherwise default images will be shown.")
    request_a_call_background = models.ImageField(upload_to='images/', null=True, blank=True, help_text="Upload image if you want otherwise default images will be shown.")
    

    def delete(self, using=None, keep_parents=False):
        if self.main_image1:
            self.main_image1.storage.delete(self.main_image1.name)
        if self.main_image2:
            self.main_image2.storage.delete(self.main_image2.name)
        if self.video_background:
            self.video_background.storage.delete(self.video_background.name)
        if self.what_we_offer:
            self.what_we_offer.storage.delete(self.what_we_offer.name)
        if self.about_us_background:
            self.about_us_background.storage.delete(self.about_us_background.name)
        if self.request_a_call_background:
            self.request_a_call_background.storage.delete(self.request_a_call_background.name)

        super().delete()


    def __str__(self):
        return self.album_name


class PeolpeContactUs(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    time_of_creation = models.DateTimeField()
 
 
    class Meta:
        ordering = ['time_of_creation']

    def __str__(self):
        return self.name

class People_Request_For_Call(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True, null=True)
    time_of_creation = models.DateTimeField()


    class Meta:
        ordering = ['time_of_creation']

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    detail = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

