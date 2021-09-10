from partenaire.entities import PartenaireEntity


class PartenaireUsecases():
    """Class containing all Partenaire use cases."""

    def __init__(self, storage):
        """Instantiate with a storage instance that defines the persistence layer."""
        self.storage = storage

    def create_partenaire(self, partenaire_dict):
        """Take a dictionary representing a partenaire, save to DB and return entity."""
        if 'name' not in partenaire_dict.keys():
            raise ValueError('Name required to create partenaire.')
        if 'email' not in partenaire_dict.keys():
            raise ValueError('email required to create partenaire.')
        if 'phone_number' not in partenaire_dict.keys():
            raise ValueError('phone number required to create partenaire.')

        try:
            partenaire = PartenaireEntity(**partenaire_dict)
        except TypeError:
            raise ValueError('Partenaire initialized with invalid field')

        return self.storage.save_partenaire(partenaire)

    def get_partenaire(self, partenaire_uuid):
        return self.storage.get_partenaire(partenaire_uuid=partenaire_uuid)

    def get_all_partenaire(self):
        return self.storage.get_all_partenaire()

    def update_partenaire(self, partenaire_dict):
        """Take a dictionary representing a partenaire, save to DB and return entity."""
        if 'id' not in partenaire_dict.keys():
            raise ValueError('Id required to update partenaire.')
        if 'name' not in partenaire_dict.keys():
            raise ValueError('Name required to update partenaire.')
        if 'email' not in partenaire_dict.keys():
            raise ValueError('email required to update partenaire.')
        if 'phone_number' not in partenaire_dict.keys():
            raise ValueError('phone number required to update partenaire.')

        try:
            return self.storage.update_partenaire(partenaire_dict['id'], partenaire_dict)
        except TypeError:
            raise ValueError('Partenaire initialized with invalid field')

    def delete_partenaire(self, partenaire_uuid):
        return self.storage.delete_partenaire(partenaire_uuid)
