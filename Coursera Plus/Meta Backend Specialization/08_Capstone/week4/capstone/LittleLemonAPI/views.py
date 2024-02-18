from django.shortcuts import render
from rest_framework import generics, filters
from django.shortcuts import get_object_or_404
from datetime import date
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.core import serializers
from django.http import HttpResponse
import json

from .models import MenuItem, Category, Cart, Order, OrderItem
from .models import Booking

from .forms import BookingForm

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
#from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.views import APIView

from .serializers import MenuItemSerializer, CategoryMenuSerializer
from .serializers import UserSerializer
from .serializers import OrderItemSerializer
from .serializers import OrderSerializer
from .serializers import BookingSerializer

# from .serializers import  CartSerializer
from .serializers import CartSerializerView
from .permissions import MenuItemPermission
from .permissions import SingleMenuItemPermission
from .permissions import ManagerGroupPermissions
from .permissions import CartItemsPermissions
from .permissions import SingleOrderItemPermission

# Create your views here.

def home(request):
    return render(request, 'index.html')

# Add your code here to create new views
def menu(request):
    menu_data = MenuItem.objects.all()
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', {"menu": main_data})

def about(request):
    return render(request, 'about.html')

@permission_classes([IsAuthenticated])
def reservations(request):
    booking_json = []
    date = request.GET.get('date',datetime.today().date())
    bookings = Booking.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html',{"bookings":booking_json})

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)


class BookingViewSet(viewsets.ModelViewSet ):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]

   
#@csrf_exempt
@permission_classes([IsAuthenticated])
def bookings(request):
    if request.method == 'POST':
        data = json.load(request)
        exist = Booking.objects.filter(reservation_date=data['reservation_date']).filter(
            reservation_slot=data['reservation_slot']).exists()
        if exist==False:
            booking = Booking(
                first_name=data['first_name'],
                reservation_date=data['reservation_date'],
                reservation_slot=data['reservation_slot'],
            )
            booking.save()
        else:
            return HttpResponse("{'error':1}", content_type='application/json')
    
    date = request.GET.get('date', datetime.today().date())
    
    if not date:
        date = datetime.today().date()    
        
    bookings = Booking.objects.all().filter(reservation_date=date)
    booking_json = serializers.serialize('json', bookings)

    return HttpResponse(booking_json, content_type='application/json')

class CategorItemsView(generics.ListCreateAPIView):
     queryset = Category.objects.all()
     serializer_class = CategoryMenuSerializer
     permission_classes = [MenuItemPermission]

class MenuItemViews(generics.ListCreateAPIView):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer
    permission_classes = [MenuItemPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'category__title']


class SingleMenuItemsView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [SingleMenuItemPermission]


class ManagerUsersView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Manager')
    serializer_class = UserSerializer
    permission_classes = [ManagerGroupPermissions]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        if username:
            user = get_object_or_404(User, username=username)
            managers = Group.objects.get(name="Manager")
            managers.user_set.add(user)
            return Response({"message": "User {} added to Manager group.".format(username)}, status=status.HTTP_201_CREATED)
        return Response({"message":"error"}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        username = request.data.get("username")
        if username:
            user = get_object_or_404(User, username=username)
            managers = Group.objects.get(name="Manager")
            if user in managers.user_set.all():
                managers.user_set.remove(user)
                return Response({"message": "User {} removed from Manager group.".format(username)}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"message": "User {} is not in Manager group.".format(username)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"error"}, status=status.HTTP_400_BAD_REQUEST)
    

class SingleManagerUsersView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [SingleMenuItemPermission]


class DeliveryCrewView(generics.ListCreateAPIView):
    queryset = User.objects.filter(groups__name='Delivery')
    serializer_class = UserSerializer
    permission_classes = [ManagerGroupPermissions]

    def post(self, request, *args, **kwargs):
        username = request.data.get("username")
        if username:
            user = get_object_or_404(User, username=username)
            delivery = Group.objects.get(name="Delivery")
            delivery.user_set.add(user)
            return Response({"message": "User {} added to Delivery group.".format(username)}, status=status.HTTP_201_CREATED)
        return Response({"message":"error"}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        username = request.data.get("username")
        if username:
            user = get_object_or_404(User, username=username)
            delivery = Group.objects.get(name="Delivery")
            if user in delivery.user_set.all():
                delivery.user_set.remove(user)
                return Response({"message": "User {} removed from Delivery group.".format(username)}, status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"message": "User {} is not in Delivery group.".format(username)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"error"}, status=status.HTTP_400_BAD_REQUEST)
    
class SingleDeliveryCrewView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes = [SingleMenuItemPermission]




@api_view(['GET', 'POST', 'DELETE'])
@permission_classes([ManagerGroupPermissions])
def add_to_managers(request):
    username = request.data.get("username")
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Manager")
        if request.method == 'POST':
            managers.user_set.add(user)
            message = "User {} added to Manager group.".format(username)
            res_status = status.HTTP_201_CREATED
        if request.method == 'DELETE':
            managers.user_set.remove(user)
            message = "User {} removed from Manager group.".format(username)
            res_status = status.HTTP_200_OK
        return Response({"message":message}, status=res_status) 
    return Response({"message":"error"}, status=status.HTTP_400_BAD_REQUEST)


# class CartViewSet(viewsets.ModelViewSet):
#     queryset = Cart.objects.all()
#     serializer_class = CartSerializer

#     def list(self, request):
#         queryset = Cart.objects.filter(user=request.user)
#         serializer = CartSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def create(self, request):
#         data = request.data
#         menu_item = MenuItem.objects.get(id=data.get('menu_item_id'))
#         cart_item, created = Cart.objects.get_or_create(user=request.user, menuitem=menu_item)
#         if not created:
#             cart_item.quantity += int(data.get('quantity', 1))
#         cart_item.save()
#         serializer = CartSerializer(cart_item)
#         return Response(serializer.data)

#     def destroy(self, request, pk=None):
#         Cart.objects.filter(user=request.user).delete()
#         return Response(status=204)
    


class CartView(APIView):
    permission_classes = [CartItemsPermissions]

    def post(self, request, format=None):
        menu_item_id = request.data.get('menuitem')
        quantity = int(request.data.get('quantity'))
        menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
        unit_price = menu_item.price
        price = quantity * unit_price
        cart_item = Cart.objects.create(
            user=request.user,
            menuitem=menu_item,
            quantity=quantity,
            unit_price=unit_price,
            price=price
        )
        serializer = CartSerializerView(cart_item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def get(self, request, format=None):
        cart_items = Cart.objects.filter(user=request.user)
        serializer = CartSerializerView(cart_items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, format=None):
        Cart.objects.filter(user=request.user).delete()
        return Response(status=status.HTTP_200_OK)
    


class OrdersView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
            if request.user.groups.filter(name='Customer').exists():
                orders = Order.objects.filter(user=request.user)
            elif request.user.groups.filter(name='Manager').exists():
                orders = Order.objects.all()
            elif request.user.groups.filter(name='Delivery').exists():
                orders = Order.objects.filter(delivery_crew=request.user)
            elif request.user.is_superuser:
                orders = Order.objects.all()
            else:
                return Response({"message": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
            serializer = OrderSerializer(orders, many=True)
            return Response(serializer.data)
    
    def post(self, request):
        if request.user.groups.filter(name='Customer').exists():
            cart_items = Cart.objects.filter(user=request.user)
            if cart_items.exists():
                order = Order.objects.create(user=request.user, total=sum(item.price for item in cart_items), date=date.today())
                for item in cart_items:
                    OrderItem.objects.create(order=order, menuitem=item.menuitem, quantity=item.quantity, unit_price=item.unit_price, price=item.price)
                cart_items.delete()
                serializer = OrderSerializer(order)
                return Response(serializer.data, status=201)
            else:
                return Response({"message": "No items in cart to create an order."}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"message": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
    

class OrderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [SingleOrderItemPermission]

    def patch(self, request, pk, format=None):
        if request.user.groups.filter(name='Manager').exists() or request.user.is_superuser:
            username = request.data.get("delivery_crew")
            if username:
                user = get_object_or_404(User, username=username)
                order = get_object_or_404(Order, id=pk)
                delivery = Group.objects.get(name="Delivery")
                if user in delivery.user_set.all():
                    order.delivery_crew = user
                    order.save()  # Save the updated order
                    return Response({"message": "The delivery crew {} successfully assigned to deliver order {}".format(username, pk)}, status=status.HTTP_200_OK)
                else:
                    return Response({"message": "The user {} is not a member of the Delivery group".format(username)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": "Missing data. Check delivery crew username exists in the request."}, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.user.groups.filter(name='Delivery').exists():
            user = request.user
            status_str = request.data.get("status")
            if status_str is not None:
                bool_status = status_str.lower() in ['true', '1', 'yes']
                delivery = Group.objects.get(name="Delivery")
                if user in delivery.user_set.all():
                    order = get_object_or_404(Order, id=pk)
                    if order.delivery_crew == user:
                        order.status = bool_status
                        order.save()
                        return Response({"message": "The status of the requested order {} is updated".format(pk)}, status=status.HTTP_200_OK)
                    else:
                        return Response({"message": "The order is not assigned to this delivery crew"}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({"message": "The user is not a member of the Delivery group"}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({"message": "Missing the status field"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "You do not have permission to perform this task."}, status=status.HTTP_403_FORBIDDEN)



class OrderItemView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return OrderItem.objects.get(pk=pk)
        except OrderItem.DoesNotExist:
            return Response({"error": "OrderItem with id {} does not exist".format(pk)}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, pk, format=None):
        order_item = self.get_object(pk)
        if isinstance(order_item, Response):
            return order_item
        
        if request.user.groups.filter(name='Customer').exists() and order_item.order.user == request.user:
            serializer = OrderItemSerializer(order_item)
            return Response(serializer.data)
        else:
            return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)

    def put(self, request, pk, format=None):
        order_item = self.get_object(pk)
        if isinstance(order_item, Response):
            return order_item
        if request.user.groups.filter(name='Customer').exists() and order_item.order.user == request.user:
            serializer = OrderItemSerializer(order_item, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk, format=None):
        order_item = self.get_object(pk)
        if isinstance(order_item, Response):
            return order_item
        if request.user.groups.filter(name='Manager').exists():
            order_item.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)

    def patch(self, request, pk, format=None):
        order_item = self.get_object(pk)
        if isinstance(order_item, Response):
            return order_item
        if request.user.groups.filter(name='Delivery').exists() and order_item.order.delivery_crew == request.user:
            serializer = OrderItemSerializer(order_item, data=request.data, partial=True) # set partial=True to update a data partially
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({"detail": "You do not have permission to perform this action."}, status=status.HTTP_403_FORBIDDEN)
