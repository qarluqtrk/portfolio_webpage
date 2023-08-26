from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=55)
    email = models.EmailField()
    subject = models.CharField(max_length=155)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'


class MainInfo(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=55)
    description1 = models.TextField()
    description2 = models.TextField()
    address = models.CharField(max_length=155)
    study = models.CharField(max_length=155)
    degree = models.CharField(max_length=155)
    email = models.CharField(max_length=155)
    phone = models.CharField(max_length=13)
    location = models.CharField(max_length=55, null=True, blank=True)

    def __str__(self):
        return self.name


class Features(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Services(models.Model):
    icon = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title


class Interests(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Skills(models.Model):
    title = models.CharField(max_length=50)
    percentage = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class Language(models.Model):
    title = models.CharField(max_length=50)
    percentage = models.FloatField()

    def __str__(self):
        return self.title


class Education(models.Model):
    title = models.CharField(max_length=55)
    degree = models.CharField(max_length=100)
    start = models.CharField(max_length=100)
    finish = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    title = models.CharField(max_length=55)
    position = models.CharField(max_length=100)
    start = models.IntegerField()
    finish = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title


class Partners(models.Model):
    title = models.CharField(max_length=55)
    link = models.TextField()
    icon = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


class PortfolioCategories(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=55)
    description = models.TextField()
    link = models.TextField()
    category = models.ForeignKey(to=PortfolioCategories,
                                 on_delete=models.CASCADE,
                                 related_name='Categories',
                                 related_query_name='categories')
    client = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self):
        return self.title





class SocialNetworks(models.Model):
    icon = models.ImageField(upload_to='images/')
    link = models.TextField()
