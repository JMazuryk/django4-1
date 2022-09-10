# Створюємо в коні проекту файл users.json (в нього будете записувати ваших юзерів)
#
# Реалізовуємо ось такі EndPoints:
#
# GET http://localhost:8000/users           //витягнути всіх юзерів з файлу
# POST http://localhost:8000/users        // записати нового юзера в файл (не забудьте про id, він має бути унікальним)
#
# GET http://localhost:8000/users/<ID>           // витягти юзера по ID
# PUT http://localhost:8000/users/<ID>          // змінити юзера по ID
# DELETE  http://localhost:8000/users/<ID>          // видалити юзера по ID