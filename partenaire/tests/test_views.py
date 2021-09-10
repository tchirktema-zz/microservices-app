"""Tests for views.

These tend to be integration tests that make sure views return correct data (or the correct errors).
They don't need to be very detailed. But they do test that view, use case, models, and entities
are all playing nicely together.
"""
import json
from partenaire.models import PartenaireModel
from django.test import TestCase, RequestFactory
from django.urls import reverse
from rest_framework import status
from partenaire.views import ParternaireView


class CreatePartenaireTestCase(TestCase):
    def setUp(self):
        self.req_factory = RequestFactory()

    def create_request(self, data):
        request = self.req_factory.post(
            reverse('create_partenaire'),
            content_type='application/json',
            data=json.dumps(data)
        )

        return request

    def test_create_partenaire_success(self):
        data = {
            "name": 'partenaire 1',
            "email": 'email@partenaire',
            "website": 'partenaire.com',
            "description": 'description partenaire',
            "phone_number": '930349304',
        }

        request = self.create_request(data)

        response = ParternaireView.create_partenaire(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_partenaire_invalid_name(self):
        data = {
            "email": 'email@partenaire',
            "website": 'partenaire.com',
            "description": 'description partenaire',
            "phone_number": '930349304',
        }

        request = self.create_request(data)

        response = ParternaireView.create_partenaire(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_partenaire_invalid_email(self):
        data = {
            "name": 'partenaire 1',
            "website": 'partenaire.com',
            "description": 'description partenaire',
            "phone_number": '930349304',
        }

        request = self.create_request(data)

        response = ParternaireView.create_partenaire(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_partenaire_invalid_phone_number(self):
        data = {
            "name": 'partenaire 1',
            "email": 'email@partenaire',
            "website": 'partenaire.com',
            "description": 'description partenaire'
        }

        request = self.create_request(data)

        response = ParternaireView.create_partenaire(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_partenaire_invalid_website(self):
        data = {
            "name": 'partenaire 1',
            "email": 'email@partenaire',
            "description": 'description partenaire',
            "phone_number": '930349304',
        }

        request = self.create_request(data)

        response = ParternaireView.create_partenaire(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_partenaire_invalid_description(self):
        data = {
            "name": 'partenaire 1',
            "email": 'email@partenaire',
            "website": 'partenaire.com',
            "phone_number": '930349304',
        }

        request = self.create_request(data)

        response = ParternaireView.create_partenaire(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class GetPartenaireTestCase(TestCase):
    def setUp(self):
        self.req_factory = RequestFactory()
        self.partenaire = PartenaireModel.objects.create(
            name='partenaire',
            description='description',
            email='email@partenaire.com',
            slug='partenaire',
            phone_number='0123456789',
            website='partenaire.com'
        )

    def test_get_all_partenaire(self):
        url = reverse('get_all_partenaire')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_partenaire_by_uuid(self):
        url = reverse('get_partenaire', kwargs={'uuid': self.partenaire.pk})
        response = self.client.get(url)
        self.assertEqual(response.data, self.partenaire.to_Json())
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_partenaire_with_invalid_uuid(self):
        url = reverse('get_partenaire', kwargs={
                      'uuid': '1a9ac93e-d3ce-448e-bcad-7f27517a9113'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdatePartenaireTestCase(TestCase):
    def setUp(self):
        self.req_factory = RequestFactory()
        self.partenaire = PartenaireModel.objects.create(
            name='partenaire',
            description='description',
            email='email@partenaire.com',
            slug='partenaire',
            phone_number='0123456789',
            website='partenaire.com'
        )

    def create_request(self, data):
        request = self.req_factory.put(
            reverse('update_partenaire'),
            content_type='application/json',
            data=data
        )

        return request

    def test_can_update_partenaire(self):
        data = {
            "id":  self.partenaire.pk,
            "name": 'partenaire updateeeeed',
            "description": 'description',
            "email": 'email@partenaire',
            "website": 'partenaire.com',
            "phone_number": '930349304',
        }
        request = self.create_request(data)
        response = ParternaireView.update_partenaire(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_can_update_partenaire_with_invalid_description(self):
        data = {
            "id":  self.partenaire.pk,
            "name": 'partenaire updateeeeed',
            "email": 'email@partenaire',
            "website": 'partenaire.com',
            "phone_number": '930349304',
        }
        request = self.create_request(data)
        response = ParternaireView.update_partenaire(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_update_partenaire_with_invalid_id(self):
        data = {
            "id":  'c3c8ae8e-74f7-43e1-9b49-2f720d51a539',
            "name": 'partenaire updateeeeed',
            "email": 'email@partenaire',
            "website": 'partenaire.com',
            "phone_number": '930349304',
        }
        request = self.create_request(data)
        response = ParternaireView.update_partenaire(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_update_partenairewith_invalid_website(self):
        data = {
            "id":  self.partenaire.pk,
            "name": 'partenaire updateeeeed',
            "description": 'description',
            "email": 'email@partenaire',
            "phone_number": '930349304',
        }
        request = self.create_request(data)
        response = ParternaireView.update_partenaire(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_update_partenairewith_invalid_phone_number(self):
        data = {
            "id":  self.partenaire.pk,
            "name": 'partenaire updateeeeed',
            "description": 'description',
            "email": 'email@partenaire',
            "website": 'partenaire.com',
        }
        request = self.create_request(data)
        response = ParternaireView.update_partenaire(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_update_partenaire_with_invalid_email(self):
        data = {
            "id":  self.partenaire.pk,
            "name": 'partenaire updateeeeed',
            "description": 'description',
            "website": 'partenaire.com',
            "phone_number": '930349304',
        }
        request = self.create_request(data)
        response = ParternaireView.update_partenaire(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_can_update_partenaire_with_invalid_name(self):
        data = {
            "id":  self.partenaire.pk,
            "description": 'description',
            "email": 'email@partenaire',
            "website": 'partenaire.com',
            "phone_number": '930349304',
        }
        request = self.create_request(data)
        response = ParternaireView.update_partenaire(request)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class DeletePartenaireTestCase(TestCase):
    def setUp(self):
        self.req_factory = RequestFactory()
        self.partenairedelete = PartenaireModel.objects.create(
            name='partenaire delete',
            description='description',
            email='email@partenairedelete.com',
            slug='partenaire',
            phone_number='012345786789',
            website='partenairedelete.com'
        )

    def test_can_delete_partenaire(self):
        url = reverse('delete_partenaire', kwargs={
                      'uuid': self.partenairedelete.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
