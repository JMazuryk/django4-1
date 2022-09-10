from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms.models import model_to_dict
from rest_framework.generics import get_object_or_404
from rest_framework import status

from .models import UserModel
from .serializers import UserSerializer


class UserListCreateView(APIView):
    def get(self, *args, **kwargs):
        qs = UserModel.objects.all()
        # res = [model_to_dict(user) for user in qs]
        # qs = qs.filter(name='Adam')
        # print(qs)
        # print(qs.query)
        serializer = UserSerializer(qs, many=True)
        return Response(serializer.data,status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        data = self.request.data
        # user = UserModel(**data)
        # user.save()
        # return Response(model_to_dict(user))
        serializer = UserSerializer(data=data)
        # if not serializer.is_valid():
        #     return Response(serializer.errors)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)


class UserRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        # qs = UserModel.objects.filter(pk=pk)
        # exists = qs.exists()
        # if not exists:
        #     return Response('Not found user')
        # # user = qs.first()
        # user = UserModel.objects.get(pk=pk)
        user = get_object_or_404(UserModel, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data,status.HTTP_200_OK)

        # return Response(model_to_dict(user))

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        data = self.request.data
        serializer = UserSerializer(user, data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status.HTTP_200_OK )

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = get_object_or_404(UserModel, pk=pk)
        data = self.request.data
        serializer = UserSerializer(user, data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status.HTTP_200_OK)

    # qs = UserModel.objects.filter(pk=pk)
    # exists = qs.exists()
    # if not exists:
    #     return Response('Not found user')
    # data = self.request.data
    # # qs.update(**data)
    # user = UserModel.objects.get(pk=pk)
    # name = data.get('name')
    # age = data.get('age')
    # user.name = name
    # user.age = age
    # user.save()
    #
    # return Response(model_to_dict(user))

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        # qs = UserModel.objects.filter(pk=pk)
        # exists = qs.exists()
        # if not exists:
        #    return Response('Not found user')
        user = get_object_or_404(UserModel, pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
