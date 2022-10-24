class Family:
    family_name = 'Common Family'
    family_funds = 100000
    have_a_house = False

    def print_info(self):
        print(
            'Family name: {}\nFamily funds: {}\nHaving a house: {}'.format(
                self.family_name, self.family_funds, self.have_a_house
            )
        )

    def earn_money(self, amount):
        self.family_funds += amount
        print(
            'Earned {} money! Current value: {}'.format(
                amount, self.family_funds
            )
        )

    def buy_house(self, house_price, discount=0):
        house_price -= house_price * discount / 100
        if self.family_funds >= house_price:
            self.family_funds -= house_price
            self.have_a_house = True
            print('House purchased! Current money: {}'.format(
                self.family_funds
            )
            )
        else:
            print('Not enough money!')


my_family = Family()
my_family.print_info()
print('Try to buy a house')
my_family.buy_house(10 ** 6)
if not my_family.have_a_house:
    my_family.earn_money(800000)
    print('Try to buy house afain')
    my_family.buy_house(10 ** 6, 10)

my_family.print_info()
