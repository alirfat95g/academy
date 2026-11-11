from django.db import models
from decimal import Decimal
from django.core.validators import MinValueValidator
from datetime import timedelta


class Category(models.Model):
    name = models.CharField(
        verbose_name="نام دسته بندی",
        max_length=100,
        unique=True,
        help_text="مثلا برنامه نویسی",
        blank=False,
    )

    slug = models.SlugField(
        verbose_name="شناسه آدرس",
        max_length=120,
        unique=True,
        allow_unicode=True,
        help_text="web-design",
    )

    description = models.TextField(verbose_name="توضیحات", blank=True)

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ["name"]
        # ordering = ["-name"]

    def __str__(self):
        return self.name


class Course(models.Model):

    LEVEL_CHOICES = [
        ("beginner", "مقدماتی"),
        ("intermediate", "متوسط"),
        ("advanced", "پیشرفته"),
    ]

    title = models.CharField(verbose_name="عنوان دوره", max_length=200)

    category = models.ForeignKey(
        Category,
        verbose_name="دسته بندی",
        on_delete=models.PROTECT,
        related_name="courses",
        # blank=True,
        # null=True
    )

    slug = models.SlugField(
        verbose_name="شناسه آدرس",
        max_length=220,
        unique=True,
        allow_unicode=True,
        help_text="into-to-python",
    )

    description = models.TextField(
        verbose_name="توضیحات", help_text="توضیحات دوره را اینجا بنویسید"
    )

    level = models.CharField(
        verbose_name="سطح دوره",
        max_length=20,
        choices=LEVEL_CHOICES,
        default="beginner",
    )

    price = models.DecimalField(
        verbose_name="قیمت به تومان",
        max_digits=12,
        decimal_places=2,
        default=Decimal("0.00"),
        validators=[MinValueValidator(Decimal("0.00"))],
        help_text="برای دوره رایگان صفر وارد کنید",
    )

    capacity = models.PositiveBigIntegerField(
        verbose_name="ظرفیت",
        default=20,
        validators=[MinValueValidator(1)],
        help_text="حداکثر تعداد هنرجویان هر دوره",
    )

    duration = models.DurationField(
        verbose_name="مدت کل آموزش",
        default=timedelta(hours=10),
        validators=[MinValueValidator(timedelta(minutes=1))],
        help_text="10:00:00",
    )

    start_date = models.DateField(
        verbose_name="تاریخ شروع", blank=True, null=True, db_index=True
    )

    start_time = models.TimeField(
        verbose_name="ساعت شروع", blank=True, null=True, help_text="09:00:00"
    )

    is_active = models.BooleanField(
        verbose_name="فعال است؟",
        default=True,
        help_text="آیا دوره در سایت نمایش داده شود؟",
    )

    created_at = models.DateTimeField(
        verbose_name="زمان ایجاد",
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(verbose_name="آخرین ویرایش", auto_now=True)

    class Meta:
        verbose_name = "دوره"
        verbose_name_plural = "دوره ها"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title


