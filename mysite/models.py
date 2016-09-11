from django.utils import timezone
from django.db import models


class Contact(models.Model):

    """
    This models holds the contact requests submitted by general users.
    """
    created_date = models.DateField(
        verbose_name='Created Date',
        null=True,
        blank=True,
    )

    name = models.CharField(
        verbose_name='Contact name',
        max_length=50,
    )

    email = models.EmailField(
        verbose_name='Contact Email',
        max_length=50,
        null=True,
        blank=True
    )

    phone = models.CharField(
        verbose_name='Contact Number',
        max_length=15,
        null=True,
        blank=True
    )

    message = models.TextField(
        verbose_name='Detailed message',
        max_length=500,
        null=True,
        blank=True
    )

    attended = models.BooleanField(
        verbose_name='Attended to Contact Request',
        default=False
    )

    def save(self, *args, **kwargs):
        self.created_date = timezone.datetime.now().date()
        super(Contact, self).save(*args, **kwargs)

    def __str__(self):
        return '{}, {}, {}'.format(self.name, self.email, self.phone)

    class Meta:
        app_label = 'mysite'