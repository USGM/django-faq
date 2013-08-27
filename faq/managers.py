from django.db import models

class PreOrderedManager(models.Manager):
    def all(self):
        all_items = super(PreOrderedManager, self).all()
        return all_items.order_by('sort_order')
