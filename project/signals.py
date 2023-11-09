from django.db.models.signals import post_save
from django.dispatch import receiver
from django.apps import apps

from django.contrib.auth.models import User
from .models import Blog, Notification


@receiver(post_save, sender=Blog)
def notify_new_course(sender, instance, **kwargs):
    # Получаем модель Notification динамически
    Notification = apps.get_model('project', 'Notification')
    # Создаем уведомление о новом курсе
    notification = Notification.objects.create(message=f'Новый курс "{instance.title}" доступен для обучения')
    notification.users.set(User.objects.all())
