from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.

def alpha_numeric_validator(value: str):
    if value.lower() != slugify(value) or '-' in value:
        raise ValidationError('Ensure this value contains only letters, numbers, and underscore')


class Profile(models.Model):

    username = models.CharField(
        max_length=15,
        validators=[
            MinLengthValidator(2),
            alpha_numeric_validator,
        ]
                                )

    email = models.EmailField()

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

