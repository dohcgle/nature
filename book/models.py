from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse

CHAPTER_CHOICES = (
    ('I', '1-BO’LIM. MAKTABGACHA TA’LIMDA BOLALARNI TABIAT BILAN TANISHTIRISHNING NAZARIY ASOSLARI VA TABIAT HAQIDA TUSHUNCHA'),
    ('II', '2-BO’LIM. MAKTABGACHA TA’LIM TASHKILOTLARIDA TABIATSHUNOSLIK ISHLARINI TASHKIL ETISH'),
    ('III', '3-BO’LIM. MAKTABGACHA TA’LIM TASHKILOTLARIDA TABIAT BILAN TANISHTIRISHNING MAZMUNI'),
    ('IV', '4-BO’LIM. MAKTABGACHA YOSHDAGI BOLALARNI TABIAT BILAN TANISHTIRISH METOD, VOSITALARI'),
    ('V', '5-BO’LIM. MAKTABGACHA YOSHDAGI BOLALARNING TABIAT BILAN TANISHTIRISHNING ISH SHAKLLARI'),
    ('VI', '6- BO’LIM. MAKTABGACHA TA’LIM TASHKILOTLARIDA TABIAT BURCHAGINI TASHKIL QILISH'),
    ('VII', '7- BO’LIM. YER MAYDONCHALARINI TASHKIL QILISH VA ULARNING TURLARI'),
    ('VIII', '8- BO’LIM. MAKTABGACHA TA’LIM MUASSASALARIDA TABIAT TANISHTIRISH ISHLARINI REJALASHTIRISH'),
)


class Topic(models.Model):
    category = models.CharField(choices=CHAPTER_CHOICES, max_length=5)
    title = models.CharField(verbose_name="Mavzu", max_length=512)
    content = RichTextField()
    slug = models.SlugField(max_length=200, blank=True, null=True)
    position = models.IntegerField(verbose_name='Tartib raqami', default=1)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Mavzu"
        verbose_name_plural = 'Mavzular'
        ordering = ('position', )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topic-detail', kwargs={"pk": self.pk})



CATEGORY_CHOICES = (
    ('OA', 'O`QUV ADABIYOTLAR'),
    ('V', 'VIDEODARSLAR'),
    ('P', 'TAQDIMOTLAR'),
    ('T', 'TEST'),
)


class Page(models.Model):
    category = models.CharField(verbose_name="Kategoriya", choices=CATEGORY_CHOICES, max_length=5)
    title = models.CharField(verbose_name="Mavzu", max_length=512)
    description = models.CharField(verbose_name="Qisqacha mazmuni", max_length=1024, null=True, blank=True)
    content = RichTextField(verbose_name="Kontent")
    image = models.ImageField(verbose_name="Rasm", blank=True, null=True)
    # file = models.FileField(verbose_name="Fayl", blank=True, null=True)
    slug = models.SlugField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_published = models.BooleanField(verbose_name="Holati", default=True)

    class Meta:
        verbose_name = "Statik sahifa"
        verbose_name_plural = 'Statik sahifalar'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('page-detail', kwargs={"pk": self.pk})



