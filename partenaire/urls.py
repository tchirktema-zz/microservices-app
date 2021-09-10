""" Partenaire url """
from django.urls import path
from partenaire.views import ParternaireView

urlpatterns = [
    path(
        '',
        ParternaireView.get_all_partenaire,
        name='get_all_partenaire'),
    path(
        'create',
        ParternaireView.create_partenaire,
        name='create_partenaire'),
    path(
        '<uuid:uuid>',
        ParternaireView.get_partenaire,
        name="get_partenaire"),
    path(
        'update',
        ParternaireView.update_partenaire,
        name="update_partenaire"),
    path(
        '<uuid:uuid>/delete',
        ParternaireView.delete_partenaire,
        name="delete_partenaire"),


]
