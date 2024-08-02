from ckeditor.fields import RichTextField
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Категории публикаций"
        verbose_name = "Категория публикации"

    # def __str__(self):
    #     return self.title


class Hashtag(models.Model):
    title = models.CharField(max_length=255 )

    class Meta:
        verbose_name_plural = 'Хештеги'
        verbose_name = 'Хештег'

    def __str__(self):
        return self.title


class Publication(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='publications')
    hashtags = models.ManyToManyField(Hashtag, blank=True)
    image = models.ImageField(verbose_name='изображение', null=True)
    title = models.CharField(verbose_name='название', max_length=100, null=True)
    description = models.TextField(verbose_name='описание', null=True)
    read_time = models.PositiveSmallIntegerField(verbose_name='время чтения', null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Публикации"
        verbose_name = "Публикация"


class AboutMe(models.Model):
    description = RichTextField()

