from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework import status
from .forms import BookingForm
from .models import MenuItem, Category
from rest_framework.views import APIView

from rest_framework import generics
from .serializers import MenuItemSerializer, CategoryMenuSerializer, RenderMenuItemSerializer
from django.shortcuts import get_object_or_404

from rest_framework.renderers import TemplateHTMLRenderer, StaticHTMLRenderer

from django.core.paginator import Paginator, EmptyPage
from rest_framework import viewsets

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.decorators import throttle_classes
from .throttles import TenCallsPerMinute

from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User, Group

# Create your views here.
def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')



def menu(request):
    menu_data = MenuItem.objects.all()
    menu = {'menu': menu_data}
    return render(request, 'menu.html', menu)


def display_menu_item(request, pk=None):
    if(pk):
        menu_item = MenuItem.objects.get(pk=pk)
    else:
        menu_item = ""
    
    item = {'menu_item': menu_item}

    return render(request, 'menu_item.html', item)


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'book.html', context)

@api_view(['GET','POST'])
def menu_items(request):
    #return Response('List of the Menu Items', status=status.HTTP_200_OK)
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        # serialized_items = MenuItemSerializer(items, many=True)
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')

        perpage = request.query_params.get('perpage', default=2)
        page = request.query_params.get('page', default=1)

        if category_name:
            items = items.filter(Category__title =  category_name)
        
        if to_price:
            items = items.filter(price__lte = to_price)

        if search:
            items = items.filter(name__startswith = search) # contains, icontains, istartswith

        if ordering:
            ordering_fields = ordering.split(',')
            items = items.order_by(*ordering_fields)

        paginator = Paginator(items, per_page=perpage)

        try:
            items = paginator.page(number=page)
        except EmptyPage:
            items = []
        serialized_items = MenuItemSerializer(items, many=True, context={'request': request})
        return Response(serialized_items.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serialized_items = MenuItemSerializer(data = request.data)
        serialized_items.is_valid(raise_exception=True)
        # serialized_items.validated_data()
        serialized_items.save()
        return Response(serialized_items.data, context={'request': request},status=status.HTTP_201_created)



@api_view(['GET','POST'])
def single_item(request, id):
    item = get_object_or_404(MenuItem, pk=id)
    serialized_item = MenuItemSerializer(item, context={'request': request})
    return Response(serialized_item.data, status=status.HTTP_200_OK)

class MenuList(APIView):
    def get(self, request):
        return Response({"message":"List of the Menu Items"}, status=status.HTTP_200_OK)
    
    def post(self, request):
        return Response({"message": "New menu created"}, status= status.HTTP_200_OK)
    

class SingleMenuItem(APIView):
    def get(self, request, pk):
        return Response({"message": "Single item with id" + str(pk)}, status= status.HTTP_200_OK)
    
    def post(self, request, pk):
        return Response({"title": "Name for the new Menu item, " + request.data.get('name')}, status= status.HTTP_200_OK)


@api_view()
def category_detail(request, pk):
    category = get_object_or_404(Category,pk=pk)
    serialized_category = CategoryMenuSerializer(category)
    return Response(serialized_category.data)

class MenuItemViews(generics.ListCreateAPIView):
    queryset = MenuItem.objects.select_related('category').all()
    serializer_class = MenuItemSerializer


class SingleMenuItemsView(generics.RetrieveUpdateAPIView, generics.DestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


@api_view() 
@renderer_classes ([TemplateHTMLRenderer])
def menu_html(request):
    items = MenuItem.objects.select_related('category').all()
    serialized_item = RenderMenuItemSerializer(items, many=True)
    return Response({'data':serialized_item.data}, template_name='menu-items-html.html')

@api_view(['GET'])
@renderer_classes([StaticHTMLRenderer])
def welcome(request):
    data = '<html><body><h1>Welcome To Little Lemon API Project</h1></body></html>'
    return Response(data)

# filtering and pagination
class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = RenderMenuItemSerializer # MenuItemSerializer
    ordering_fields=['price','inventory']
    search_fields=['name', 'category__title']


class CategoriesView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategoryMenuSerializer


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message":"The secret message is porto."})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def manager_view(request):
    if request.user.groups.filter(name = 'Manager').exists():
        return Response({"message":"Only Manager Can See This."})
    else:
        return Response({"message": "You Are Not Authorized"}, status= status.HTTP_403_FORBIDDEN)
    


@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message":"successful"})



@api_view()
#@throttle_classes([UserRateThrottle])
@throttle_classes([TenCallsPerMinute])
def throttle_check_auth(request):
    return Response({"message":"successful"})

# Add throttling to authenticated users to view menu items
class MenuItemsViewSetAuth(viewsets.ModelViewSet):
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = MenuItem.objects.all()
    serializer_class = RenderMenuItemSerializer # MenuItemSerializer
    ordering_fields=['price','inventory']
    search_fields=['name', 'category__title']

    def get_throttles(self):
        if self.action == 'create':
            throttle_classes = [UserRateThrottle]
        else:
            throttle_classes = []
        return [throttle() for throttle in throttle_classes]
    


@api_view(['POST', 'DELETE'])
@permission_classes([IsAdminUser])
def add_to_managers(request):
    username = request.data["username"]
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Manager")
        if request.method == 'POST':
            managers.user_set.add(user)
            message = "User {} added to Manager group.".format(username)
        if request.method == 'DELETE':
            managers.user_set.remove(user)
            message = "User {} removed from Manager group.".format(username)

        return Response({"message":message})
    return Response({"message":"error"}, status=status.HTTP_400_BAD_REQUEST)