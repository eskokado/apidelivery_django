from rest_framework import serializers

from addresses.models import Address


class AddressInfoSerializer(serializers.Serializer):
    cep = serializers.CharField()
    logradouro = serializers.CharField()
    complemento = serializers.CharField()
    bairro = serializers.CharField()
    localidade = serializers.CharField()
    uf = serializers.CharField()
    ibge = serializers.CharField()
    gia = serializers.CharField()
    ddd = serializers.CharField()
    siafi = serializers.CharField()


class AddressSerializer(serializers.ModelSerializer):
    address_info = AddressInfoSerializer(read_only=True)
    class Meta:
        model = Address
        fields = '__all__'


