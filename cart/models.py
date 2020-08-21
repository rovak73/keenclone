from django.db import models
from django.conf import settings
from uuslug import uuslug, slugify
from django.urls import reverse
from autoslug import AutoSlugField


CATEGORY_CHOICES = [
    ('co', 'consulta'),
    ('cl', 'clase'),
    ('le', 'lectura')
]
LABEL_CHOICES = [
    ('pr', 'primary'),
    ('se', 'secondary'),
    ('da', 'danger')

]


class Item(models.Model):
    profile = models.ForeignKey(
        'profiles.Profile', on_delete=models.CASCADE)
    description = models.CharField(max_length=280, blank=True, null=True)
    title = models.CharField(max_length=100)
    slug = AutoSlugField(populate_from='title')
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(choices=LABEL_CHOICES, max_length=2)

    class Meta:
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def __str__(self):
        return '%s, %s, %s' % (self.profile, self.title, self.id)

    def save(self, *args, **kwargs):  # new
        self.slug = slugify(f'{self.id}-{self.title}')
        super().save(*args, **kwargs)

        # ABSOLUTE URL METHOD
    def get_absolute_url(self):
        return reverse('cart:item-detail', kwargs={'slug': self.slug})

    def get_add_to_cart_url(self):
        return reverse('cart:add-to-cart', kwargs={'slug': self.slug})

    def get_remove_from_cart_url(self):
        return reverse('cart:remove-from-cart', kwargs={'slug': self.slug})


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.email

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_final_price()
        return total
