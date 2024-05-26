import uuid

from django.db import models
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404


class AbstractManager(models.Manager):

    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            return Http404


class AbstractModel(models.Model):
    """
        Define fields that will be present in every model.

        This class has abstract property to True, so that it
        can't be instantiated, and it can't create a table in db.

    """

    public_id = models.UUIDField(
        db_index=True,
        unique=True,
        default=uuid.uuid4(),
        editable=False
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = AbstractManager()

    class Meta:
        abstract = True
