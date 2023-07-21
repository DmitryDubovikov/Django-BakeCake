from django.core.validators import MinValueValidator
from django.db import models

from accounts.models import User


class Level(models.Model):
    title = models.CharField("Количество уровней", max_length=30)
    price = models.DecimalField(
        "цена",
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = "Уровни торта"
        verbose_name_plural = "Уровни тортов"

    def __str__(self):
        return self.title


class Shape(models.Model):
    title = models.CharField("Наименование формы", max_length=50)
    price = models.DecimalField(
        "цена",
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = "Форма торта"
        verbose_name_plural = "Формы тортов"

    def __str__(self):
        return self.title


class Topping(models.Model):
    title = models.CharField("Топпинг", max_length=100)
    price = models.DecimalField(
        "цена",
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = "Топпинг"
        verbose_name_plural = "Топпинги"

    def __str__(self):
        return self.title


class Berry(models.Model):
    title = models.CharField("Ягода", max_length=50)
    price = models.DecimalField(
        "цена",
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = "Ягода"
        verbose_name_plural = "Ягоды"

    def __str__(self):
        return self.title


class Decor(models.Model):
    title = models.CharField("Наименование декора", max_length=50)
    price = models.DecimalField(
        "цена",
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )

    class Meta:
        verbose_name = "Декор"
        verbose_name_plural = "Декоры"

    def __str__(self):
        return self.title


class Cake(models.Model):
    name = models.CharField("Название торта", max_length=100, blank=True)
    levels = models.ForeignKey("Level", verbose_name="Уровни", on_delete=models.CASCADE)
    shape = models.ForeignKey("Shape", verbose_name="Форма", on_delete=models.CASCADE)
    topping = models.ForeignKey("Topping", verbose_name="Топинг", on_delete=models.CASCADE)
    berries = models.ForeignKey(
        "Berry", verbose_name="Ягоды", on_delete=models.CASCADE, blank=True, null=True
    )
    decor = models.ForeignKey(
        "Decor", verbose_name="Декор", on_delete=models.CASCADE, blank=True, null=True
    )
    inscription = models.CharField("Надпись", max_length=100, blank=True, null=True)
    image = models.ImageField(
        "Изображение", upload_to="media/", blank=True, null=True, default="media/no_image.png"
    )

    class Meta:
        verbose_name = "Торт"
        verbose_name_plural = "Торты"

    def __str__(self):
        if self.name:
            return self.name


class Order(models.Model):
    STATUSES = [
        ("В ОБРАБОТКЕ", "В обработке"),
        ("ГОТОВИТСЯ", "Готовится"),
        ("В ДОСТАВКЕ", "Передан в доставку"),
        ("ВЫПОЛНЕН", "Выполнен"),
    ]
    address = models.CharField("Адрес", max_length=150)
    date = models.DateField("Дата доставки")
    time = models.TimeField("Время доставки")
    comment = models.TextField("Комментарий к доставке", blank=True)
    status = models.CharField(
        "Статус заказа",
        max_length=20,
        choices=STATUSES,
        default="1",
    )
    client = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Клиент", related_name="orders"
    )
    cake = models.OneToOneField(
        to=Cake,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='торт'
    )

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

    def __str__(self):
        return self.address
