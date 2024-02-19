from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal


class CategoryMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    stock = serializers.IntegerField(source = 'inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='cal_tax')
    
    #category = serializers.StringRelatedField()

    # category = CategoryMenuSerializer()

    # category = CategoryMenuSerializer(read_only=True)
    # category_id = serializers.IntegerField(write_only=True)

    category = serializers.HyperlinkedRelatedField(
                queryset = Category.objects.all(),
                view_name='category-detail',
                )

    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'inventory', 'description', 'stock', 'price_after_tax' ,'category']

    def cal_tax(self, menu:MenuItem):
        return menu.price * Decimal(1.1)
    

# Serializer to be used with HTML template DRF and serializer
class RenderMenuItemSerializer(serializers.ModelSerializer):
    category = CategoryMenuSerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)
    class Meta:
        model = MenuItem
        fields = ['id', 'name', 'price', 'inventory', 'description', 'category', 'category_id']