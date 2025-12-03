database_2.py
# Задание 2
# Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
# Для этого: выведи все трекеры заказов и их статусы. 
# Статусы определяются по следующему правилу:
# Если поле finished == true, то вывести статус 2.
# Если поле canсelled == true, то вывести статус -1.
# Если поле inDelivery == true, то вывести статус 1.
# Для остальных случаев вывести 0.
# Технические примечания:
# Доступ к базе осуществляется с помощью команды psql -U morty -d scooter_rent. 
# Пароль: smith.
# У psql есть особенность: если таблица в базе данных с большой буквы, 
# то её в запросе нужно брать в кавычки. Например, select * from Orders.

# ssh <имя пользователя>@<хост> -p<порт>
ssh 3f3a9f94-2ddb-4aa7-ac3e-9dcf86e57535@serverhub.praktikum-services.ru -p4554
morty@028b3c7de0d8:~$ psql -U morty -d scooter_rent
Password for user morty:
psql (11.18 (Debian 11.18-0+deb10u1))
Type help for help.

# Создаем еще 2 заказа, для проверки отражения в базе данных не принятых заказов.
# Завершаем один заказ в эмуляторе Android Studio или через Postman (https://{stend}/api/v1/orders/finish/:id, 
# где :id - id курьера, с телом запроса {id: 123}, где id - id заказа

# SQL запрос
SELECT 
    track AS order_track,
    CASE 
        WHEN finished = true THEN 2
        WHEN cancelled = true THEN -1
        WHEN inDelivery = true THEN 1
        ELSE 0
    END AS order_status
FROM Orders
ORDER BY order_track;

# Ответ из Базы данных
 order_track | order_status
-------------+--------------
      124393 |            1
      124393 |            1
      195995 |            1
      195995 |            2
      790352 |            0
      831610 |            1
      831610 |            1
      854083 |            0
(8 rows)
# Из-за бага А1 найденного при регрессионном тестировании, который удваивает принятые 
# курьером заказы, мы видим что один и тот же заказ у нас выводится и как принятый в 
# процессе доставки, и как завершенный.
