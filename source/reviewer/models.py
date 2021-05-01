from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Good(models.Model):
    CHOICES = [("Еда", "food"), ("Обучение", "education"), ("Одежда", "clothes"), ("Электроника", "electronic")]
    summary = models.CharField(max_length = 60, null = False, blank = False, verbose_name = "Название")
    description = models.CharField(max_length = 2000, null = True, blank=True, verbose_name = "Описание")
    category = models.CharField(max_length = 29, null = True, blank=False, verbose_name = "Категория", choices= CHOICES)
    picture = models.ImageField(blank=True)

    class Meta:
        db_table = "goods"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.get_category_display()


class Review(models.Model):
    CHOICES = [("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")]
    author = models.ForeignKey(get_user_model(), related_name="reviews", on_delete=models.CASCADE)
    good = models.ForeignKey("reviewer.Good", related_name="reviews", on_delete=models.CASCADE)
    review_text = models.CharField(max_length = 2000, null = True, blank=False, verbose_name = "Текст Отзыва")
    rating = models.CharField(max_length = 4, null = True, blank=False, verbose_name = "Оценка", choices= CHOICES)
    moderation = models.BooleanField(default=False)
    
    class Meta:
        db_table = "reviews"
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return self.get_good_display()
