from rest_framework import serializers
from .models import Student, Blok, Cijfer, Toets



class Studentserializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'voornaam', 'achternaam')


    def create(self, validated_data):
        return Student.object.create(validated_data)

    def update(self, instance, validated_data):
        instance.voornaam = validated_data.get('voornaam', instance.voornaam)
        instance.achternaam = validated_data.get('achternaam', instance.achternaam)
        instance.id = validated_data.get('id', instance.id)

        instance.save()
        return instance





class Blokserializer(serializers.ModelSerializer):
    class Meta:
        model = Blok
        fields = ('id', 'blok')


    def create(self, validated_data):
        return Blok.object.create(validated_data)

    def update(self, instance, validated_data):
        instance.blok = validated_data.get('blok', instance.blok)
        instance.id = validated_data.get('id', instance.id)

        instance.save()
        return instance






class Cijferserializer(serializers.ModelSerializer):
    class Meta:
        model = Cijfer
        fields = ('id', 'cijfer', 'toets_id', 'blok_id')


    def create(self, validated_data):
        return Cijfer.object.create(validated_data)

    def update(self, instance, validated_data):
        instance.cijfer = validated_data.get('cijfer', instance.cijfer)
        instance.toets_id = validated_data.get('toets_id', instance.toets_id)
        instance.blok_id = validated_data.get('blok_id', instance.blok_id)
        instance.id = validated_data.get('id', instance.id)

        instance.save()
        return instance








class Toetsserializer(serializers.ModelSerializer):
    class Meta:
        model = Toets
        fields = ('id', 'toets')


    def create(self, validated_data):
        return Toets.object.create(validated_data)

    def update(self, instance, validated_data):
        instance.toets = validated_data.get('toets', instance.toets)
        instance.id = validated_data.get('id', instance.id)

        instance.save()
        return instance