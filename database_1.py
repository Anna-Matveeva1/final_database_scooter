# Задание 1
# Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
# Для этого: выведи список логинов курьеров с количеством их заказов в статусе
#  «В доставке» (поле inDelivery = true). 

# ssh <имя пользователя>@<хост> -p<порт>
ssh 3f3a9f94-2ddb-4aa7-ac3e-9dcf86e57535@serverhub.praktikum-services.ru -p4554
# Доступ к базе осуществляется с помощью команды psql -U morty -d scooter_rent. 
# Пароль: smith.
morty@028b3c7de0d8:~$ psql -U morty -d scooter_rent
Password for user morty:
psql (11.18 (Debian 11.18-0+deb10u1))
Type "help" for help.

# Создаем 2 курьера в Postman https://{stend}/api/v1/courier
# 1 курьер
{
    "login": "ninja",
    "password": "1234",
    "firstName": "Alex"
}
# 2 курьер
{
    "login": "nina",
    "password": "1234",
    "firstName": "Nina"
}

# Создаем 3 заказа меняя станции метро в Postman https://{stend}/api/v1/orders
{
    "address": "Центральный проезд Хорошёвского Серебряного Бора 2",
    "metroStation": "204",
    "rentTime":4,
    "deliveryDate": "2025-12-04",
    "comment": " ",
    "color": [
        "BLACK"
    ]
}

# В эмуляторе Android Studio или через Postman (https://{stend}/1?courierId=1 
# - где "1?" - id заказа, а "courierId=1" - id курьера)
# Принимаем 1 курьер - 1 заказ, 2 курьер - 2 заказа

# SQL запрос
SELECT 
     c.login,
     COUNT(o.id) AS active_deliveries
FROM "Couriers" c
JOIN "Orders" o ON c.id = o."courierId"
WHERE o."inDelivery" = true
GROUP BY c.login
ORDER BY active_deliveries DESC;

# Ответ из Базы данных
 login | active_deliveries
-------+-------------------
 nina  |                 4
 ninja |                 2
(2 rows)
# Заказы удваиваются из-за бага А1 найденного при регрессионном тестировании