from rest_framework import serializers
from review.models import Review, Mark


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'body', 'food', 'owner']


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ['food', 'owner', 'mark']
