from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from Service.models import *

from pytils.translit import slugify


class GameMaker(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название производителя')

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название категории')

    def __str__(self):
        return self.name


class Game(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название игры')
    logo = models.ImageField(upload_to='logos/', verbose_name='Логотип игры')
    description = models.TextField(verbose_name='Описание игры')
    equipment = models.TextField(verbose_name='Оборудование для игры')
    rules = models.FileField(upload_to='rules/', verbose_name='Правила игры')
    images = models.ManyToManyField(Image, verbose_name='Изображения игры')
    players_min = models.IntegerField(verbose_name='Минимальное количество игроков')
    players_max = models.IntegerField(verbose_name='Максимальное количество игроков')
    game_duration = models.IntegerField(verbose_name='Продолжительность игры')
    complexity = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)],
                                             verbose_name='Сложность игры')
    expansion = models.ForeignKey('Game', on_delete=models.CASCADE, null=True, blank=True,
                                  verbose_name='Расширение игры')
    maker = models.ForeignKey(GameMaker, on_delete=models.CASCADE, verbose_name='Производитель игры')
    category = models.ManyToManyField(Category, verbose_name='Категория игры')
    supposed_age = models.IntegerField(verbose_name='Рекомендуемый возраст для игры')
    price = models.PositiveIntegerField(verbose_name='Цена игры')
    sale_price = models.PositiveIntegerField(null=True, blank=True, verbose_name='Цена со скидкой')
    slug = models.SlugField(unique=True, max_length=150, verbose_name='URL-адрес игры')

    def save(self, *args, **kwargs):
        if self.price < self.sale_price:
            raise ValueError('The sale price must be lower than the price')
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game', kwargs={'slug': self.slug})


class GameReview(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE, verbose_name='Игра')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    text = models.TextField(verbose_name='Текст отзыва')
    date = models.DateField(verbose_name='Дата отзыва')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.user.name} -> {self.game.name}'


class UserReview(GameReview):
    rating = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)],
                                         verbose_name='Рейтинг пользователя')


class Comment(MPTTModel, GameReview):
    parent = TreeForeignKey('self', on_delete=models.CASCADE,
                            null=True, blank=True, related_name='children', verbose_name='Родительский комментарий')

    class MPTTMeta:
        order_insertion_by = ['date']

    def __str__(self):
        return self.text


class Relatable(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, verbose_name='Пользователь')
    question = models.ForeignKey(Comment, on_delete=models.CASCADE, verbose_name='Вопрос')

    class Meta:
        abstract = True

    def __str__(self):
        return f'{self.user.name} -> {self.question.text}'


class Upvote(Relatable):
    pass


class Downvote(Relatable):
    pass