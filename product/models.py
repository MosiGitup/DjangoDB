from django.db import models
from django.urls import reverse


class Project(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'project'
        verbose_name_plural = 'projects'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('list_by_project', args=[self.slug])
    def get_absolute_url(self):
        return reverse('DBhome_by_project', args=[self.slug])


class Region(models.Model):
    project = models.ForeignKey(Project, related_name='regions', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    image = models.ImageField(upload_to='regions', blank=True)
    available = models.BooleanField(default=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'region'
        verbose_name_plural = 'regions'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('region_detail', args=[self.id, self.slug])


class Product(models.Model):
    region = models.ForeignKey(Region, related_name='products', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products', blank=True)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    download = models.FileField(upload_to='products/region', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'product'
        verbose_name_plural = 'products'
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', args=[self.region, self.slug, self.id])
