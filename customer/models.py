from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=640)
    code = models.CharField(max_length=255, null=True, blank=True)
    user = models.OneToOneField('erp_user.User', on_delete=models.PROTECT, null=True, related_name='customer')
    category = models.ForeignKey('category.Category', on_delete=models.PROTECT, null=True, blank=True)
    group = models.ForeignKey('category.Group', on_delete=models.PROTECT, null=True, blank=True)
    info = models.OneToOneField('document.Info', on_delete=models.PROTECT, null=True, blank=True,
                                related_name='owner_customer')
    document = models.OneToOneField('document.Document', on_delete=models.PROTECT, null=True, blank=True,
                                    related_name='owner_customer')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name} {self.user.get_full_name() if self.user else ""}'
