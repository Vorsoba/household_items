from django.db import models


class Item(models.Model):
    CONSISTENCY_CHOICES = [
        ('liquid', 'Liquid'),
        ('solid', 'Solid'),
        ('textile', 'Textile'),
        ('chemistry', 'Chemistry'),
        ('viscous mass', 'Viscous mass'),
    ]

    USAGE_ENVIRONMENT_CHOICES = [
        ('kitchen', 'Kitchen'),
        ('bathroom', 'Bathroom'),
        ('bedroom', 'Bedroom'),
        ('livingroom', 'Living Room'),
        ('corridor', 'Corridor'),
    ]

    name = models.CharField(blank=False, default='Unknown', max_length=150, unique=True)
    lifetime = models.IntegerField(blank=False, null=True)
    consistency = models.CharField(blank=False, default='Unknown', choices=CONSISTENCY_CHOICES, max_length=20)
    usage_environment = models.CharField(blank=False, default='Unknown', choices=USAGE_ENVIRONMENT_CHOICES,
                                         max_length=20)

    price = models.FloatField(blank=True, default='Unknown', null=True)

    def depreciation(self):
        if self.price is None:
            return 0
        return round(self.price / 12, 2)

    def __str__(self):
        return f'{self.name}'
