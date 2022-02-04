from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db import models

from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from account.models import User


class Category(models.Model):
    slug = models.SlugField(max_length=100, primary_key=True)
    name = models.CharField(max_length=150, unique=True)

    def __str__(self):
        return self.name


class AutoPost(models.Model):
    CHOICES2 = (
        ('in stock', 'В наличии'),
        ('soon', 'Скоро')
    )
    CHOICES3 = (
        ('mechanics', 'Механика'),
        ('auto', 'Автомат')
    )
    title = models.CharField(max_length=40)
    year = models.PositiveSmallIntegerField(default=2015)
    type = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='types')
    status = models.CharField(choices=CHOICES2, max_length=20)
    kpp = models.CharField(choices=CHOICES3, max_length=20)
    text = models.TextField(default='Ogon mawina')
    prices = models.PositiveSmallIntegerField(default=4000)
    draft = models.BooleanField(default=False)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Auto'
        verbose_name_plural = 'Auto'


class AutoPostImage(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)
    auto = models.ForeignKey(AutoPost, on_delete=models.CASCADE, related_name='images')


class RatingStar(models.Model):
    """Звезда рейтинга"""

    value = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    post = models.ForeignKey(
        AutoPost,
        on_delete=models.CASCADE,
        verbose_name="фильм",
        related_name="ratings"
    )

    def __str__(self):
        return f"{self.star} - {self.post}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


# class Like(models.Model):
#     user = models.ForeignKey(User, related_name='like', on_delete=models.CASCADE)
#     post = models.ForeignKey(AutoPost, related_name='like', on_delete=models.CASCADE)
#     like = models.BooleanField(default=False)
#
#     def __str__(self):
#         return f'{self.like}'