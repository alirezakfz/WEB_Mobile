from rest_framework import serializers
from .models import MenuItem, Category, Cart, Order, OrderItem, Booking
from django.contrib.auth.models import User

class CategoryMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    category = CategoryMenuSerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = MenuItem
        fields = ['id', 'title', 'price', 'featured' ,'category', 'category_id']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'is_active')


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
        
# class CartSerializer(serializers.ModelSerializer):
#     #menuitem = MenuItemSerializer(read_only=True)
#     unit_price = serializers.SerializerMethodField()
#     price = serializers.SerializerMethodField()

#     class Meta:
#         model = Cart
#         fields = ['id', 'user', 'menuitem', 'quantity', 'unit_price', 'price']

#     def get_unit_price(self, cart):
#         return cart.menuitem.price

#     def get_price(self, cart):
#         return cart.quantity * cart.menuitem.price
    
#     def create(self, validated_data):
#         menu_item_id = self.context['request'].data.get('menuitem')
#         menu_item = MenuItem.objects.get(id=menu_item_id)
#         quantity = validated_data.get('quantity')
#         unit_price = menu_item.price
#         price = quantity * unit_price
#         cart_item = Cart.objects.create(
#             user=self.context['request'].user,
#             menuitem=menu_item,
#             quantity=quantity,
#             unit_price=unit_price,
#             price=price
#         )
#         return cart_item
        

class CartSerializerView(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','user', 'menuitem', 'quantity', 'unit_price', 'price']


class OrderItemSerializer(serializers.ModelSerializer):
    menuitem = MenuItemSerializer(read_only=True)

    class Meta:
        model = OrderItem
        fields = ['id','order', 'menuitem', 'quantity', 'unit_price', 'price']
    


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    delivery_crew = serializers.StringRelatedField()
    order_items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'delivery_crew', 'status', 'total', 'date', 'order_items']