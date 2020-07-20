from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save
from django.dispatch import receiver

from mjstore_main.models import Customer

@receiver(post_save, sender=User)
def create_customer(sender, instance, created, **kwargs):
    if created:
        print(instance.username)
        group = Group.objects.get(name='customer')
        group.user_set.add(instance)
        Customer.objects.create(user=instance)
        print('customer created!')

# post_save.connect(create_customer, sender=User)
