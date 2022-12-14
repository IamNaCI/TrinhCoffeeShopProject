from django.db import models
from phone_field import PhoneField

DRINK_CHOICES = [
    ('ca phe', 'Cà phê'),
    ('black coffee', 'Black Coffee'),
    ('latte', 'Latte'),
    ('macchiato', 'Macchiato'),
    ('cappucchino', 'Cappucchino'),
    ('cortado', 'Cortado'),
    ('cold brew', 'Cold Brew'),
    ('lemonade', 'Lemonade'),
    ('hot chocolate', 'Hot Chocolate'),
    ('tea', 'Tea'),
    ('thai iced tea', 'Thai Iced Tea'),
]

SUGAR_LEVEL = [
    ('none', 'None'),
    ('less', 'Less'),
    ('regular', 'Regular'),
    ('extra', 'Extra'),
]

ICE_LEVEL = [
    ('none', 'None'),
    ('less', 'Less'),
    ('regular', 'Regular'),
    ('extra', 'Extra'),
]

SNACK_CHOICES = [
    ('chocolate', 'Chocolate Donut'),
    ('plain', 'Plain Donut'),
    ('sugar', 'Sugar Donut'),
    ('che thai', 'Chè Thái'),
    ('banh bao', 'Bánh bao'),
    ('banh cam', 'Bánh Cam'),
]

STYLE = [
    ('hot', 'Hot'),
    ('ice', 'Iced'),
]

SIZE = [
    ('small', 'Small'),
    ('medium', 'Medium'),
    ('large', 'Large'),
    ('xtra', 'Xtra Large'),
]


class Subscribe(models.Model):
    name = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.task

    class Meta:
        db_table = 'Subscribe'
        app_label = 'coffee'


class Carousel(models.Model):
    image = models.ImageField(upload_to='static/images')
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)
    phone_number = PhoneField(help_text='Contact Phone number')
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Order(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = PhoneField(help_text='Contact Phone number')
    drink = models.CharField(max_length=30, null=True, blank=True, choices=DRINK_CHOICES)
    size = models.CharField(max_length=30, null=True, blank=True, choices=SIZE)
    style = models.CharField(max_length=30, null=True, blank=True, choices=STYLE)
    sugar = models.CharField(max_length=30, null=True, blank=True, choices=SUGAR_LEVEL)
    ice = models.CharField(max_length=30, null=True, blank=True, choices=ICE_LEVEL)
    snack = models.CharField(max_length=30, null=True, blank=True, choices=SNACK_CHOICES)
    message = models.TextField(max_length=500)

    def __str__(self):
        return self.drink

    class Meta:
        db_table = 'Order'
        app_label = 'coffee'
