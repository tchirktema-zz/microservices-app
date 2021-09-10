"""Test adapter for Django ORM."""

from django.test import TestCase
from partenaire import models as partenaires_models
from adapters.django_storage import DjangoStorage

storage = DjangoStorage()


class SavePartenaireTestCase(TestCase):
    """ Test to save partenaire """

    def test_save_partenaire(self):
        partenaire = partenaires_models.PartenaireModel(
            name='partenaire 1',
            email='email@partenaire',
            website='partenaire.com',
            description='description partenaire',
            phone_number='930349304',
        )

        partenaire = storage.save_partenaire(partenaire)
        saved_partenaire = partenaires_models.PartenaireModel.objects.get(
            pk=partenaire.pk)
        self.assertEqual(partenaire.name, saved_partenaire.name)
