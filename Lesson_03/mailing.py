class Mailing:

    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        return (f"Отправление {self.track} из {self.from_address.index},"
                f"{self.from_address.city}, {self.from_address.street},"
                f"{self.from_address.home}, {self.from_address.flat} в "
                f"{self.to_address.index} {self.to_address.city} "
                f"{self.to_address.street} {self.to_address.home}"
                f"{self.to_address.flat}. Стоимость {self.cost} рублей.")
