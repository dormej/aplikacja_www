
from datetime import datetime
from rest_framework import serializers
from .models import Person, Team


class TeamSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    country = serializers.CharField(required=True)

    def create(self, validated_data):
        return Team.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.country = validated_data.get('name', instance.country)
        instance.save()
        return instance


class PersonModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'first_name', 'last_name', 'month_of_birth', 'team', 'published_date']
        read_only_fields = ['id']

    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError(
                'Name should contains only letters!'
            )
        return value

    def validate_published_date(self, value):
        if value.month > datetime.now().month:
            raise serializers.ValidationError(
                'Month of published date must be today or lesser!'
            )
        return value

