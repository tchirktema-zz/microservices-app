
from rest_framework import serializers
from partenaire.models import PartenaireModel


class PartenaireSerializer(serializers.ModelSerializer):
    class Meta:
        model = PartenaireModel
        fields = "__all__"
