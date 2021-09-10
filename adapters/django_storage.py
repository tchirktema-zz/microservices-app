from adapters.storage import Storage
from partenaire import models as partenaires_models
from django.core.exceptions import ObjectDoesNotExist


class DjangoStorage(Storage):
    """Adapter to use Django ORM as a storage backend."""

    def save_partenaire(self, partenaire):
        """ store partenaire entity """
        django_partenaire = partenaires_models.PartenaireModel.objects.from_entity(
            partenaire)

        django_partenaire.save()

        return django_partenaire

    def get_partenaire(self, partenaire_uuid):
        """ Retrieve partenaire entity by uuid. """
        try:
            django_partenaire = partenaires_models.PartenaireModel.objects.get(
                pk=partenaire_uuid)

        except partenaires_models.PartenaireModel.DoesNotExist:
            raise self.DoesNotExist(
                'Partenaire {} was not found.'.format(partenaire_uuid))
        if django_partenaire:
            return django_partenaire

    def get_all_partenaire(self):
        """ Retrieve  all partenaires """
        django_partenaires = partenaires_models.PartenaireModel.objects.all()
        return django_partenaires

    def update_partenaire(self, uuid, partenaire_dict):
        try:
            django_partenaire = partenaires_models.PartenaireModel.objects.get(
                id=uuid)
        except partenaires_models.PartenaireModel.DoesNotExist:
            self.DoesNotExist('Partenaire {} was not found.'.format(uuid))

        partenaires_models.PartenaireModel.objects.filter(
            id=uuid).update(**partenaire_dict)
        data = partenaires_models.PartenaireModel.objects.get(id=uuid)

        return data

    def delete_partenaire(self, uuid):
        try:
            django_partenaire = partenaires_models.PartenaireModel.objects.get(
                id=uuid)
        except partenaires_models.PartenaireModel.DoesNotExist:
            self.DoesNotExist('Partenaire {} was not found.'.format(uuid))

        return django_partenaire.delete()
