from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    text = models.CharField(max_length=500, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    @property
    def ImageURL(self):
        if self.image.url:
            return self.image.url
        else:
            return ''


class Product(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    sub_description = models.CharField(max_length=500, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    image1 = models.ImageField(null=True, blank=True)
    image2 = models.ImageField(null=True, blank=True)
    image3 = models.ImageField(null=True, blank=True)

    @property
    def Image1URL(self):
        try:
            return self.image1.url
        except:
            return ''

    @property
    def Image2URL(self):
        if self.image2.url:
            return self.image2.url
        else:
            return ''

    @property
    def Image3URL(self):
        if self.image3.url:
            return self.image3.url
        else:
            return ''


class FAQ(models.Model):
    question = models.TextField(max_length=500, null=True, blank=True)
    answer = models.TextField(max_length=500, null=True, blank=True)


class Youtube(models.Model):
    link = models.CharField(max_length=1000, null=True, )


class Blog(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    description = models.TextField(max_length=1000, null=True, blank=True)


class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)

    @property
    def ImageURL(self):
        if self.image.url:
            return self.image.url
        else:
            return ''


class Partner(models.Model):
    image = models.ImageField(null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
