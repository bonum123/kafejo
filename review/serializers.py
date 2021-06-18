from rest_framework import serializers

from food.models import Food
from review.models import Review, Mark, Marks


class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mark
        fields = ['food', 'owner', 'mark']


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.email')
    food = serializers.ChoiceField(choices=Food.objects.all())
    mark = serializers.ChoiceField(choices=Marks.choose_your_mark)

    class Meta:
        model = Review
        fields = ['id', 'body', 'food', 'owner', 'mark']

    def create(self, validated_data):
        print(validated_data)
        request = self.context.get('request')
        images_data = request.FILES
        created_review = Review.objects.create(**validated_data)
        print(created_review)
        images_obj = [
            Review(post=created_review, image=image)
            for image in images_data.getlist('images')
        ]
        Review.objects.bulk_create(images_obj)
        return created_review


class ReviewDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['body', 'owner', 'food']
