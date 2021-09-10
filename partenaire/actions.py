from partenaire.use_cases import PartenaireUsecases


class PartenaireActions():
    def __init__(self, storage):
        self.use_cases = PartenaireUsecases(storage)

    def get_all_partenaire(self):
        return self.use_cases.get_all_partenaire()

    def create_partenaire(self, partenaire_dict):
        return self.use_cases.create_partenaire(
            partenaire_dict=partenaire_dict)

    def get_partenaire(self, partenaire_uuid):
        return self.use_cases.get_partenaire(partenaire_uuid=partenaire_uuid)

    def update_patenaire(self, partenaire_dict):
        return self.use_cases.update_partenaire(partenaire_dict)

    def delete_partenaire(self, partenaire_uuid):
        return self.use_cases.delete_partenaire(partenaire_uuid)
