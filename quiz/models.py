from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.db import models

CHAPTER_CHOICES = (
    ('I', 'I BOB. SMM – IJTIMOIY MEDIA MARKETING'),
    ('II', 'II BOB. SMM LOYIHALARI BILAN ISHLASH'),
    ('III', 'III BOB. CMS – KONTENT BOSHQARUV TIZIMLARI'),
    ('IV', 'IV BOB. LMS – TA’LIMNI BOSHQARUV TIZIMLARI'),
    ('V', 'V BOB. MOOC – OMMAVIY OCHIQ ONLAYN KURSLAR'),
    ('VI', 'VI BOB. WEB-FREELANCE – INTERNET ORQALI DAROMAD OLISH'),
)


class Quiz(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='quizzes')
    name = models.CharField(max_length=255)
    chapter = models.CharField(choices=CHAPTER_CHOICES, max_length=5)

    def __str__(self):
        return self.name


class Question(models.Model):
    category = models.CharField(choices=CHAPTER_CHOICES, max_length=5)
    text = models.CharField(verbose_name="Savol", max_length=512)
    content = RichTextField()
    slug = models.SlugField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')
    text = models.CharField('Answer', max_length=255)
    is_correct = models.BooleanField('Correct answer', default=False)

    def __str__(self):
        return self.text


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')

    # User reputation score.
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.user
