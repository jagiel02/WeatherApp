from django.db.models.signals import post_save, pre_save, post_delete
from django.core.signals import request_finished
from django.dispatch import receiver, Signal
from .models import City
import logging

city_log = logging.getLogger("City_log")
city_log.setLevel(logging.DEBUG)
log_handler = logging.FileHandler('logs/added_cities.log')
log_handler.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
log_handler.setFormatter(formatter)
city_log.addHandler(log_handler)


my_signal = Signal()

@receiver([post_save], sender = City)
def city_save(sender, instance, **kwargs):
    print(f'You just added a city: {instance.name}')
    city_log.info(f'You just added a city: {instance.name}')

@receiver([post_delete], sender = City)
def city_delete(sender, instance, **kwargs):
    print(f'You just deleted a city: {instance.name}')
    city_log.info(f'You just deleted a city: {instance.name}')


@receiver(request_finished)
def strona_wczytana(sender, **kwargs):
    print('Page uploaded')