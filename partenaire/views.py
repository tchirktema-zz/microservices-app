from partenaire.serializer.partenaire_serializer import PartenaireSerializer
from rest_framework import response, status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from partenaire.actions import PartenaireActions
from adapters.django_storage import DjangoStorage
from drf_spectacular.utils import extend_schema
storage = DjangoStorage()
actions = PartenaireActions(storage=storage)


class ParternaireView(APIView):
    serializer_class = PartenaireSerializer

    @api_view(['GET'])
    def get_all_partenaire(request):
        partenaires = actions.get_all_partenaire()
        serializers = PartenaireSerializer(partenaires, many=True)
        return response.Response(serializers.data, status=status.HTTP_200_OK)

    @extend_schema(
        request=PartenaireSerializer,
        responses={PartenaireSerializer}
    )
    @api_view(['POST'])
    def create_partenaire(request):
        """ create a new partenaire """
        try:
            name = request.data['name']
        except KeyError:
            return response.Response(
                {"error": "Name required to create partenaire"},
                status=status.HTTP_403_FORBIDDEN
            )
        try:
            email = request.data['email']
        except KeyError:
            return response.Response(
                {"error": "Email required to create partenaire"},
                status=status.HTTP_403_FORBIDDEN
            )
        try:
            website = request.data['website']
        except KeyError:
            return response.Response(
                {"error": "website required to create partenaire"},
                status=status.HTTP_403_FORBIDDEN
            )
        try:
            description = request.data['description']
        except KeyError:
            return response.Response(
                {"error": "description required to create partenaire"},
                status=status.HTTP_403_FORBIDDEN
            )
        try:
            phone_number = request.data['phone_number']
        except KeyError:
            return response.Response(
                {"error": "phone_number required to create partenaire"},
                status=status.HTTP_403_FORBIDDEN
            )

        paratenaire_dict = {
            "name": name,
            "email": email,
            "website": website,
            "description": description,
            "phone_number": phone_number
        }
        partenaire = actions.create_partenaire(paratenaire_dict)

        return response.Response(
            partenaire.to_Json(),
            status=status.HTTP_201_CREATED)

    @api_view(['GET'])
    def get_partenaire(request, uuid):
        """ get a  partenaire """
        try:
            partenaire = actions.get_partenaire(uuid)
            return response.Response(
                partenaire.to_Json(),
                status=status.HTTP_200_OK)
        except DjangoStorage.DoesNotExist:
            data = {"error": "Partenaire matching query does not exist."}
            return response.Response(data, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(
        request=PartenaireSerializer,
        responses={PartenaireSerializer}
    )
    @api_view(['PUT'])
    def update_partenaire(request):
        """ update a partenaire """
        try:
            name = request.data['name']
        except KeyError:
            return response.Response(
                {"error": "partenaire id required to update partenaire"},
                status=status.HTTP_403_FORBIDDEN
            )
        try:
            email = request.data['email']
        except KeyError:
            return response.Response(
                {"error": "Email required to create partenaire"},
                status=status.HTTP_403_FORBIDDEN
            )
        try:
            website = request.data['website']
        except KeyError:
            return response.Response(
                {"error": "website required to create partenaire"},
                status=status.HTTP_403_FORBIDDEN
            )
        try:
            description = request.data['description']
        except KeyError:
            return response.Response(
                {"error": "description required to create partenaire"},
                status=status.HTTP_403_FORBIDDEN
            )
        try:
            phone_number = request.data['phone_number']
        except KeyError:
            return response.Response(
                {"error": "phone_number required to create partenaire"},
                status=status.HTTP_403_FORBIDDEN
            )

        paratenaire_dict = {
            "id": request.data['id'],
            "name": name,
            "email": email,
            "website": website,
            "description": description,
            "phone_number": phone_number
        }

        try:
            partenaire = actions.update_patenaire(paratenaire_dict)
            return response.Response(
                partenaire.to_Json(),
                status=status.HTTP_200_OK)
        except DjangoStorage.DoesNotExist:
            data = {"error": "Partenaire matching query does not exist."}
            return response.Response(data, status=status.HTTP_403_FORBIDDEN)

    @api_view(['DELETE'])
    def delete_partenaire(request, uuid):
        """ Delete a partenaire """

        try:
            actions.get_partenaire(uuid)

        except DjangoStorage.DoesNotExist:
            data = {"error": "Partenaire matching query does not exist."}

            return response.Response(data, status=status.HTTP_400_BAD_REQUEST)

        actions.delete_partenaire(uuid)
        data = {"message": "Partenaire was deleted"}
        return response.Response(data, status=status.HTTP_200_OK)
