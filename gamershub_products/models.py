# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid
from django.db import models
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings


# Create your models here.
class GamersHubProducts(models.Model):
    """
    product_images: a small preview image of the item
    name: the name of the item
    description: the item's description
    price: the price of the item
    """
    length = 255
    image_width = 200
    image_height = 200

    product_images = models.ImageField(upload_to='gamershub/product_images/%d/%m/%Y', height_field='image_height', width_field='image_width', blank=True)
    name = models.CharField(max_length=length, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    @property
    def paypal_form(self):
        """
        business: the email address of our merchant
        amount: the price of our production
        currency: GBP in our case!
        item_name: the item’s … name!
        Invoice: A string to uniquely identify our transaction. In our case, we’re combining
        the primary key value of our product and a randomly generated unique id
        notify_url: where PayPal can send any success or error messages on our site
        return_url: where to return a customer after the payment process is complete
        cancel_url: where to return the customer if they choose to cancel the payment process
        """
        paypal_dict = {
            "business": settings.PAYPAL_RECEIVER_EMAIL,
            "amount": self.price,
            "currency": "USD",
            "item_name": self.name,
            "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
            "notify_url": settings.PAYPAL_NOTIFY_URL,
            "return_url": "%s/paypal-return" % settings.SITE_URL,
            "cancel_return": "%s/paypal-cancel" % settings.SITE_URL
        }

        return PayPalPaymentsForm(initial=paypal_dict)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Gamers Hub Products"
