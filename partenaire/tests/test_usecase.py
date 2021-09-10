"""
Tests for use cases in the partenaire module.

As much as possible we will test use cases with MemoryStorage to enforce independence between the
use cases and the Django ORM.
"""

import partenaire
from partenaire.entities import PartenaireEntity
from adapters.django_storage import DjangoStorage
from partenaire.use_cases import PartenaireUsecases
import unittest


def set_up_use_cases():
    return PartenaireUsecases(DjangoStorage())


class CreatePartenaireTestCase(unittest.TestCase):
    """ Tests for creating a partenaire """

    def setUp(self):
        self.use_cases = set_up_use_cases()
        self.storage = self.use_cases.storage

    def test_can_create_simple_partenaire(self):
        """ create partenaire """

        partenaire_data = {
            "name": 'partenaire 1',
            "email": 'email@partenaire',
            "website": 'partenaire.com',
            "description": 'description partenaire',
            "phone_number": '930349304',
        }

        partenaire = self.use_cases.create_partenaire(partenaire_data)
        saved_partenaire = self.use_cases.get_partenaire(
            partenaire_uuid=partenaire.pk)

        self.assertEqual(partenaire_data['name'], partenaire.name)
        self.assertEqual(partenaire_data['email'], partenaire.email)
        self.assertEqual(partenaire_data['name'], saved_partenaire.name)
        self.assertEqual(partenaire_data['email'], saved_partenaire.email)

    def test_can_create_partenaire_without_name(self):
        """Should raise value error when creating a partenaire without a name."""
        with self.assertRaises(ValueError):
            self.use_cases.create_partenaire({
                "email": 'email@partenaire',
                "website": 'partenaire.com',
                "description": 'description partenaire',
                "phone_number": '930349304',
            })

    def test_can_create_partenaire_without_email(self):
        """Should raise value error when creating a partenaire without a email."""
        with self.assertRaises(ValueError):
            self.use_cases.create_partenaire({
                "name": 'partenaire 1',
                "website": 'partenaire.com',
                "description": 'description partenaire',
                "phone_number": '930349304',
            })

    def test_can_create_partenaire_without_phone_number(self):
        """Should raise value error when creating a partenaire without a phone_number."""
        with self.assertRaises(ValueError):
            self.use_cases.create_partenaire({
                "name": 'partenaire 1',
                "email": 'email@partenaire',
                "website": 'partenaire.com',
                "description": 'description partenaire',
            })

    def test_can_create_partenaire_without_some_params(self):
        """Should raise value error when creating a partenaire without a phone_number."""
        with self.assertRaises(ValueError):
            self.use_cases.create_partenaire({
                "name": 'partenaire 1',
                "email": 'email@partenaire',
                "website": 'partenaire.com',
            })


class GetPartenaireTestCase(unittest.TestCase):
    """Tests for retrieving a single partenaire."""

    def setUp(self):
        self.use_cases = set_up_use_cases()
        self.storage = self.use_cases.storage
        self.partenaireget = PartenaireEntity(
            name='partenaire 2',
            email='email@partenaire2',
            website='partenaire2.com',
            description='description partenaire',
            phone_number='930349302',
            is_suspend=False
        )
        self.partenaireget = self.storage.save_partenaire(self.partenaireget)

    def test_get_partenaire_by_uuid(self):
        """Retrieve a single paternaire instance by uuid."""
        partenaire = self.use_cases.get_partenaire(self.partenaireget.pk)

        self.assertEqual(self.partenaireget.name, partenaire.name)


class UpdatePartenaireTestCase(unittest.TestCase):
    """ Test should be able to update partenaire """

    def setUp(self):
        self.use_cases = set_up_use_cases()
        self.storage = self.use_cases.storage
        self.partenaireupdate = PartenaireEntity(
            name='partenaire to update',
            email='email@partenaireupdate.com',
            website='partenaireupdate.com',
            description='description partenaire',
            phone_number='+232390030349302',
            is_suspend=False
        )
        self.partenaireupdate = self.storage.save_partenaire(
            self.partenaireupdate)

    def test_update_partenaire(self):
        partenaire = self.partenaireupdate
        partenaire.name = 'partenaire update magloire'
        partenaire.website = 'website.com'
        self.storage.update_partenaire(partenaire.pk, partenaire.to_Json())
        new_partenaire = self.storage.get_partenaire(partenaire.pk)
        self.assertEqual(new_partenaire.name, partenaire.name)


class DeletePartenaireTestCase(unittest.TestCase):
    """ Test should be able to delete partenaire """

    def setUp(self):
        self.use_cases = set_up_use_cases()
        self.storage = self.use_cases.storage
        self.partenairedelete = PartenaireEntity(
            name='partenaire to delete',
            email='email@delete.com',
            website='partenairedelete.com',
            description='description partenaire',
            phone_number='+232390121200',
            is_suspend=False
        )
        self.partenairedelete = self.storage.save_partenaire(
            self.partenairedelete)

    def test_delete_partenaire(self):
        self.storage.delete_partenaire(self.partenairedelete.pk)

        with self.assertRaises(self.storage.DoesNotExist):
            self.storage.get_partenaire(self.partenairedelete.pk)
