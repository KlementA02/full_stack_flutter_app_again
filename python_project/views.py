# from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

from .models import Pokemon  
from .serializers import PokemonSerializer,UserSerializer  
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404


# def myapp(request):
#     pokemon_list = Pokemon.objects.all().order_by('id')
#     return render(request, 'main.html', {
#         'name': 'Trainer',
#         'pokemon': pokemon_list,
#         'total_pokemon': pokemon_list.count()
#     })

@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = UserSerializer(instance=user)
    return Response({"token": token.key, "user": serializer.data})

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data["username"])
        user.set_password(request.data["password"])
        user.save()
        token = Token.objects.create(user=user)
        return Response({"token": token.key, "user":serializer.data})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def test_token(request):
    return Response({})
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_pokemon(request):
        pokemon_queryset = Pokemon.objects.all()

        # Turn them into JSON using the Serializer
        # We use many=True because it's a list
        serializer = PokemonSerializer(pokemon_queryset, many=True)
        pokedex_map = {str(p['id']): p for p in serializer.data}
        return Response(pokedex_map)  
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_pokemon(request, pokemon_id):
    try:
        # Fetch the specific Pokemon by ID
        pokemon = Pokemon.objects.get(id = pokemon_id)
        serializer = PokemonSerializer(pokemon)
        return Response(serializer.data)
    except Pokemon.DoesNotExist:
        return Response({'error': 'Pokemon not found'}, status=status.HTTP_404_NOT_FOUND)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_pokemon(request):
        # Use the Serializer to validate and save incoming data
    serializer = PokemonSerializer(data=request.data)

    if serializer.is_valid():
            # This saves the data to db.sqlite3!
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If the data sent was wrong, tell Flutter what happened
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)