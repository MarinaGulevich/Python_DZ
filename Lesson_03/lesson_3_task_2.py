from smartphone import Smartpone

smartphone_1 = Smartpone("Samsung", "Galaxy S25 Ultra", "+79024587735")

smartphone_2 = Smartpone("Apple", "iPhone 17", "+79232571251")

smartphone_3 = Smartpone("Xiaomi", "15 Ultra", "+79138573636")

smartphone_4 = Smartpone("15 Ultra", "Xperia 1 VII", "+79064576961")

smartphone_5 = Smartpone("Honor", "Magic V5", "+79994572154")

catalog = [smartphone_1, smartphone_2,
           smartphone_3, smartphone_4, smartphone_5]

for smartphone in catalog:

    print(f"{smartphone.brand}, {smartphone.model}, {smartphone.number}")
