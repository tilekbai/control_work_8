from django.db import models

# Create your models here.



class Good(models.Model):
    CHOICES = [("1", "food"), ("2", "education"), ("3", "clothes"), ("4", "electronic")]
    summary = models.CharField(max_length = 60, null = False, blank = False, verbose_name = "Заголовок")
    description = models.CharField(max_length = 2000, null = True, blank=True, verbose_name = "Описание")
    category = models.CharField(max_length = 29, null = True, blank=False, verbose_name = "Категория", choices= CHOICES)
    picture = models.ImageField(blank=True)

    class Meta:
        db_table = "goods"
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

