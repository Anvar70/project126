from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer


@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def user_create(request):
    serializer = UserSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(
            {"error": "User topilmadi"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['PUT'])
def user_update(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(
            {"error": "User topilmadi"},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = UserSerializer(user, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def user_delete(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(
            {"error": "User topilmadi"},
            status=status.HTTP_404_NOT_FOUND
        )

    user.delete()
    return Response(
        {"message": "User o'chirildi"},
        status=status.HTTP_204_NO_CONTENT
    )

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_view(request, pk=None):

    if request.method == 'GET' and pk is None:
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'GET' and pk is not None:
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "User topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Response({"error": "User topilmadi"}, status=status.HTTP_404_NOT_FOUND)

        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(
            {"message": "User o'chirildi"},
            status=status.HTTP_204_NO_CONTENT
        )