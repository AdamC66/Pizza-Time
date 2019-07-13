#Variable Declaration
current_order = []

#Class creation
class Pizza:
    def __init__(self, name="pizza", size="L",num_toppings="0", toppings=[]):
        self.name=name
        self.size = size
        self.num_toppings = num_toppings
        self.toppings = []
    def add_topping(self, topping):
        self.toppings.append(topping)
    def calc_price(self):
        regular_toppings=["peppers","olives","mushrooms","anchovies","pineapple","hot peppers","extra cheese","no cheese"]
        premium_toppings=["pepperoni","sausage", "ham","bacon","chicken"]
        total=0
        for item in self.toppings:
            if item in regular_toppings:
                total += 1
            else:
                total += 2
        if self.size =='s':
            total += 10
        elif self.size =='m':
            total += 13
        elif self.size == 'l':
            total += 15
        elif self.size == 'xl':
            total += 17
        return(total)

#Functions
def get_input(inputstring):
    variable=0
    wait_for_input=True
    while wait_for_input == True:
        print(inputstring)
        user_input = input()
        try:
            variable = int(user_input)
            wait_for_input = False
            return(variable)   
        except ValueError:
            print("Your input was invalid or unrecognized, please enter a number")

def get_size(current_order):
    for pizza in current_order:
        wait_for_input=True
        while wait_for_input == True:
            print(f'Please enter size for {pizza.name} (S,M,L,XL)')
            user_input = input().lower()
            if user_input in ["s","m","l","xl"]:
                pizza.size=user_input
                wait_for_input=False
            else:
                print("Your input was invalid or unrecognized, please enter S, M, L, or XL")
                

def get_toppings(current_order):
    list_of_toppings = ["pepperoni","peppers","olives","sausage","mushrooms","anchovies","pineapple","ham","bacon","chicken","hot peppers","extra cheese","no cheese"]
    for pizza in current_order:
        for x in range(pizza.num_toppings):
            wait_for_input=True    

            while wait_for_input == True:
                print(f"\nPlease enter topping {x+1}/{pizza.num_toppings} for {pizza.name}, for a list of toppings, type \"list\"")
                print("please note, cheese is automatically added to all orders, for no cheese, enter \"no cheese\"")
                user_input=input().lower()
                if user_input == "list":
                    for item in list_of_toppings:
                        print(item)
                elif user_input not in list_of_toppings:
                    print("input not recognized or invalid")
                else:
                    pizza.add_topping(user_input)
                    wait_for_input=False

def display_order(current_order):
    print("\nYour Order:")
    for item in current_order:
        print(f'{item.name},',f'Size: {item.size.upper()},',f'{item.num_toppings} Toppings')
        for topping in item.toppings:
            print('*',topping)
        print(f"total price: ${item.calc_price()}.00\n")


for i in range(get_input("Please enter how many pizza\'s you would like to order")
):
    current_order.append(Pizza(name=f'Pizza {i+1}'))

for i in range(len(current_order)):
    current_order[i].num_toppings= get_input(f'How many toppings would you like on {current_order[i].name}')

get_size(current_order)
get_toppings(current_order)
display_order(current_order)