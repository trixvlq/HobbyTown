from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from Games.models import Comment


@receiver(pre_save, sender=Comment)
def set_comment_level(sender, instance, **kwargs):
    if instance.parent is None:
        instance.level = 0
    else:
        if instance.parent.level == 0:
            instance.level = instance.parent.level + 2
        else:
            instance.level = instance.parent.level + 2
