import json
from typing import TypedDict
from rest_framework.views import APIView
from rest_framework.response import Response

User = TypedDict('User', {'id': int, 'name': str, 'age': int})
FILE = 'users.json'


class FileTools:
    @property
    def users(self) -> list[User]:
        try:
            with open(FILE) as file:
                return json.load(file)
        except:
            return []

    @staticmethod
    def save(users: list[User]) -> None:
        with open(FILE, 'w') as file:
            json.dump(users, file)


class UserListCreateView(APIView, FileTools):
    def get(self, *args, **kwargs):
        return Response(self.users)

    def post(self, *args, **kwargs):
        users = self.users
        user = self.request.data
        user['id'] = users[-1]['id'] + 1 if users else 1
        users.append(user)
        try:
            self.save(users)
        except:
            return Response('Error')

        return Response(user)


class UserRetrieveUpdateDestroyView(APIView, FileTools):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = next((item for item in self.users if item['id'] == pk), None)
        if not user:
            return Response('Not found user')
        return Response(user)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        users = self.users
        user = next((item for item in users if item['id'] == pk), None)
        if not user:
            return Response('Not found user')
        user |= self.request.data
        try:
            self.save(users)
        except:
            return Response('Error')
        return Response(user)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        users = self.users
        index = next((i for i, item in enumerate(users) if item['id'] == pk), None)
        if index is None:
            return Response('Not found user')
        del users[index]
        try:
            self.save(users)
        except:
            return Response('Error')

        return Response('deleted')
