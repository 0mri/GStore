from rest_framework import serializers
from backend.api.product.models import Product, Category, ProductImage
from rest_framework.reverse import reverse
from django.utils.text import slugify
from backend.api.comment.api.serializers import CommentSerializer


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['image']


class ProductSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SerializerMethodField('category_details')
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail',
        lookup_field='slug'
    )
    image = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'url', 'slug', 'name', 'image', 'category',
                  'price', 'description', 'quantity_avialable']

    # def get_description(self, obj):
    #     return obj.description[:30] + '...' if len(obj.description) > 30 else obj.description

    def get_image(self, obj):
        image_obj = obj.images.first()
        serializer = ProductImageSerializer(image_obj)
        return serializer.data

    def category_details(self, obj):
        request = self.context.get('request')
        data = {
            'url': reverse("category-detail", kwargs={'slug': obj.category.slug}, request=request),
            'slug': obj.category.slug,
            'name': obj.category.name
        }
        return data


class DetailCategorySerialiser(serializers.ModelSerializer):
    product = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['slug', 'name', 'description', 'product']


class CategorySerialiser(serializers.HyperlinkedModelSerializer):
    # product = serializers.SlugRelatedField(
    #     slug_field='name',
    #     many=True,
    #     read_only=True
    # )
    url = serializers.HyperlinkedIdentityField(
        view_name='category-detail',
        lookup_field='slug'
    )

    class Meta:
        model = Category
        fields = ['id', 'url', 'name', 'slug', 'description']

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.slug = slugify(validated_data.get('name', instance.slug))
        instance.description = slugify(
            validated_data.get('description', instance.description))
        instance.save()
        return instance


class DetialedProductSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField('category_details')

    # comments = CommentSerializer(many=True, read_only=True)
    comments = serializers.SerializerMethodField()
    images = ProductImageSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'slug', 'images', 'category', 'description',
                  'price', 'quantity_avialable', 'comments']

    def category_details(self, obj):
        request = self.context.get('request')
        data = {
            'url': reverse("category-detail", kwargs={'slug': obj.category.slug}, request=request),
            'slug': obj.category.slug,
            'name': obj.category.name
        }
        return data

    def get_comments(self, obj):
        serializer = CommentSerializer(obj.comments.all_comments(), many=True)
        return serializer.data

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.slug = slugify(validated_data.get('name', instance.slug))
        instance.price = validated_data.get('price', instance.price)
        instance.description = validated_data.get(
            'description', instance.description)
        instance.quantity_avialable = validated_data.get(
            'quantity_avialable', instance.quantity_avialable)
        instance.save()
        return instance
