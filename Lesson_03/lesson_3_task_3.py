from address import Address
from mailing import Mailing

to_address = Address(f"344082", "Ростов-на-Дону",
                     "Буденовский пр-кт", "31", "12")

from_address = Address(f"634041", "Томск", "Вагонный переулок",
                       "12", "25")

mail = Mailing(to_address=to_address,
               from_address=from_address,
               cost=200,
               track="TRACK123456789")

print((f"Отправление {mail.track} из {mail.from_address.index},"
       f" {mail.from_address.city}, {mail.from_address.street},"
       f" {mail.from_address.home} - {mail.from_address.flat}"
       f" в {mail.to_address.index}, {mail.to_address.city},"
       f" {mail.to_address.street}, {mail.to_address.home} -"
       f" {mail.to_address.flat}. Стоимость {mail.cost} рублей."))


mailing = Mailing(to_address, from_address, cost=1300,
                  track="TRACK7770123456789")

print((f"Отправление {mailing.track} из {mailing.from_address.index},"
       f" {mailing.from_address.city}, {mailing.from_address.street},"
       f" {mailing.from_address.home} - {mailing.from_address.flat}"
       f" в {mailing.to_address.index}, {mailing.to_address.city},"
       f" {mailing.to_address.street}, {mailing.to_address.home} -"
       f" {mailing.to_address.flat}. Стоимость {mailing.cost} рублей."))
