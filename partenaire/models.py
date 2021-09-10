from partenaire.entities import PartenaireEntity
import uuid
from django.db import models
from django.template.defaultfilters import slugify


class PartenaireManager(models.Manager):
    """ Helper function for partenaire """

    def from_entity(self, entity):
        return self.model(
            name=entity.name,
            email=entity.email,
            website=entity.website,
            description=entity.description,
            phone_number=entity.phone_number,
            is_suspend=entity.is_suspend

        )


class PartenaireModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=100,
        unique=True,
        null=False,
        blank=False,
        db_index=True,
    )

    slug = models.SlugField(unique=True)
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
        db_index=True
    )
    phone_number = models.CharField(
        max_length=100,
        unique=False,
        null=False,
        blank=False,
        db_index=True
    )
    website = models.CharField(
        max_length=100,
        unique=False,
        null=False,
        blank=False,
        db_index=True
    )
    description = models.TextField(max_length=100)
    is_suspend = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = PartenaireManager()

    class Meta:
        verbose_name_plural = 'partenaires'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(PartenaireModel, self).save(*args, **kwargs)

    def to_entity(self):
        return PartenaireEntity(
            id=self.id,
            name=self.name,
            email=self.email,
            website=self.website,
            description=self.description,
            phone_number=self.phone_number,
            is_suspend=self.is_suspend
        )

    def to_Json(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "website": self.website,
            "description": self.description,
            "phone_number": self.phone_number,
            "is_suspend": self.is_suspend,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }
