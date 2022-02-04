from rest_framework import serializers
from rest_framework.serializers import ModelSerializer, ValidationError

# from comment.serializers import CommentSerializer
from comment.serializers import CommentSerializer
from main.models import *


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AutoPostSerializer(ModelSerializer):
    rating_user = serializers.BooleanField()
    middle_star = serializers.IntegerField()
    class Meta:
        model = AutoPost
        fields = '__all__'


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['images'] = AutoPostImageSerializer(instance.images.all(), many=True, context=self.context).data
        representation['comments'] = CommentSerializer(instance.comment.all(), many=True, context=self.context).data
        # representation['like'] = instance.like.filter(like=True).count()
        # representation['reviews'] = AutoPostReviewSerializer(
        #     AutoPostReview.objects.filter(post=instance.id),
        #     many=True
        # ).data
        return representation


class AutoPostImageSerializer(ModelSerializer):
    class Meta:
        model = AutoPostImage
        fields = '__all__'

class CreateRatingSerializer(serializers.ModelSerializer):
    """Добавление рейтинга пользователем"""
    class Meta:
        model = Rating
        fields = ("star", "post")

    def create(self, validated_data):
        rating, _ = Rating.objects.update_or_create(
            ip=validated_data.get('ip', None),
            post=validated_data.get('post', None),
            defaults={'star': validated_data.get("star")}
        )
        return rating


# class LikeSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = Like
#         fields = '__all__'


