from time import sleep
# Python II - Lab 7 - Annie Yen


class Restaurant():
    '''Singleton class'''
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance = super(Restaurant, cls).__new__(cls, *args, **kwargs)
            setattr(cls._instance, '_orders', 0)
            setattr(cls._instance,'_total_sales',0)
        return cls._instance
    def __str__(self):
        '''string of total orders and sales'''
        return f"You have orders(s) {self._orders}, and the total cost is ${self._total_sales}" 
    def order_food(self, food_type):
        '''
		Call order_food static method from the base class Food()
        Args:
            food_type: string
        Return:
            order: call staticmethod
        '''
        try:
            food = Food()
            order = food.order_food(food_type)
            self._orders = food.order_count
            self._total_sales = food.food_price
        except Exception as err:
            del err
            order = f"Sorry, the Restaurant does not make '{food_type}'"
        return order


class Food():
    ''' Base class for the derivative classes '''
    order_count = 0
    food_price = 0
    def __init__(self):
        pass
    def price(self):
        '''placeholder for derivative class'''
        return 0  
    def prepare(self):
        '''placeholder for derivative class'''
        print("complex preparation process")
    @staticmethod
    def order_food(food_type):
        '''factory method to make Food objects'''
        food_name = food_type.lower().strip()
        if food_name == "cheeseburger":
            food = Cheeseburger()
            prepare = food.prepare()
            Food.order_count+=1
            Food.food_price+=food.price()
        elif food_name == "pasta":
            food = Pasta()
            prepare = food.prepare()
            Food.order_count+=1
            Food.food_price+=food.price()
        elif food_name == "pancake":
            food = Pancake()
            prepare = food.prepare()
            Food.order_count+=1
            Food.food_price+=food.price()
        return food


class Cheeseburger(Food):
    '''Food derivative class to implement prepare method'''
    def __init__(self):
         pass
    def  __str__(self):
        '''the class name and the price'''
        return f"{__class__.__name__}: ${self.price():.2f}"
    def price(self):
        '''return price'''
        return 5.99
    def prepare(self):
        '''facade process for derivative class'''
        print(f"{__class__.__name__}: gril all-beef patty")
        sleep(2)
        print(f"{__class__.__name__}: flip patty")
        sleep(2)
        print(f"{__class__.__name__}: put cheese on patty")
        sleep(2)
        print(f"{__class__.__name__}: put patty on bun and add toppings")
        sleep(2)
        print(f"{__class__.__name__}: All done!")


class Pasta(Food):
    '''Food derivative class to implement prepare method'''
    def __init__(self):
         pass

    def  __str__(self):
        '''the class name along and the price'''
        return f"{__class__.__name__}: ${self.price():.2f}"

    def price(self):
        '''return price'''
        return 7.99

    def prepare(self):
        '''facade process for the derivative class '''
        print(f"{__class__.__name__}: boil water for noodles")
        sleep(2)
        print(f"{__class__.__name__}: saute onions, garlic and tomatoes for sauce")
        sleep(2)
        print(f"{__class__.__name__}: put noodles in water")
        sleep(2)
        print(f"{__class__.__name__}: season the sauce")
        sleep(2)
        print(f"{__class__.__name__}: plate noodles and add sauce on top")
        sleep(2)
        print(f"{__class__.__name__}: All done!")


class Pancake(Food):
    '''Food derivative class to implement prepare method '''
    def __init__(self):
         pass

    def  __str__(self):
        '''the class name and the price'''
        return f"{__class__.__name__}: ${self.price():.2f}"

    def price(self):
        '''return the price'''
        return 9.99

    def prepare(self):
        '''facade process for the derivative class'''
        print(f"{__class__.__name__}: Sift the flour, baking powder and salt in a large bowl")
        sleep(2)
        print(f"{__class__.__name__}: Mix in milk, egg and melted butter")
        sleep(2)
        print(f"{__class__.__name__}: Heat a lightly oiled griddle")
        sleep(2)
        print(f"{__class__.__name__}: Scoop the batter onto the griddle")
        sleep(2)
        print(f"{__class__.__name__}: Brown on both sides")
        sleep(2)
        print(f"{__class__.__name__}: All done!")


def main():
    r=Restaurant()
    food = r.order_food("cheeseBurger")
    if food:
        print(food)
    food = r.order_food("pasta")
    if food:
        print(food)
    food = r.order_food("cheeseBURger ")
    if food:
        print(food)
    food = r.order_food("pancake")
    if food:
        print(food)
    food = r.order_food("mac and cheese")
    if food:
        print(food)
    print(r)
    r2=Restaurant()
    print(r2)


if __name__ == '__main__':
    main()