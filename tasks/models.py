from mptt.models import MPTTModel, TreeForeignKey
from river.models.fields.state import StateField

from django.db import models

from userprofiles.models import UserProfile


class Task(MPTTModel):
    subject = models.CharField('Subject', max_length=200)
    description = models.TextField('Description', max_length=1000, blank=True)
    status = StateField(editable=False, verbose_name='Status')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')
    supervisor = models.ForeignKey(UserProfile, related_name='tasks_by_supervisor')
    agent = models.ForeignKey(UserProfile, related_name='taks_by_agent')

    class MPTTMeta:
        level_attr = 'mptt_level'
