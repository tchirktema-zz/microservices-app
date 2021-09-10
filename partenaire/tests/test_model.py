from partenaire.models import PartenaireModel
from partenaire.entities import PartenaireEntity
from django.test import TestCase


class PartenaireTestCase(TestCase):
    def setUp(self):
        self.entity = PartenaireEntity(
            name='partenaire 1',
            email='email@partenaire',
            website='partenaire.com',
            description='description partenaire',
            phone_number='930349304',
            is_suspend=False
        )

    def test_from_entity(self):
        partenaire = PartenaireModel.objects.from_entity(self.entity)
        self.assertEqual(partenaire.name, self.entity.name)

    def test_save(self):
        partenaire = PartenaireModel.objects.from_entity(self.entity)
        partenaire.save()

        self.assertTrue(partenaire.slug is not None)
        self.assertEqual(partenaire.slug, 'partenaire-1')

    def test_to_entity(self):
        partenaire = PartenaireModel(
            name='partenaire 1',
            email='email@partenaire',
            website='partenaire.com',
            description='description partenaire',
            phone_number='930349304',
            is_suspend=False
        )
        entity = partenaire.to_entity()
        self.assertEqual(partenaire.name, entity.name)
        self.assertEqual(partenaire.email, entity.email)
        self.assertEqual(partenaire.phone_number, entity.phone_number)
