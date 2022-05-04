def merge(lst1, lst2):
    """Merges two sorted lists.

    >>> merge([1, 3, 5], [2, 4, 6])
    [1, 2, 3, 4, 5, 6]
    >>> merge([], [2, 4, 6])
    [2, 4, 6]
    >>> merge([1, 2, 3], [])
    [1, 2, 3]
    >>> merge([5, 7], [2, 4, 6])
    [2, 4, 5, 6, 7]
    """
    "*** YOUR CODE HERE ***"
    new_list=[]
    def func(lst1,lst2):
        if len(lst1)==0:
           if len(lst2)!=0:
              new_list.append(lst2[0])
              func(lst1,lst2[1:])
           return
        if len(lst2)==0:
           if len(lst1)!=0:
              new_list.append(lst1[0])
              func(lst1[1:],lst2)
           return 
        if lst1[0]>lst2[0]:
           new_list.append(lst2[0])
           func(lst1,lst2[1:])
           return
        else:
           new_list.append(lst1[0])
           func(lst1[1:],lst2)
           return
    func(lst1,lst2)
    return new_list

class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.present_year.

    >>> mint = Mint()
    >>> mint.year
    2021
    >>> dime = mint.create(Dime)
    >>> dime.year
    2021
    >>> Mint.present_year = 2101  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2021
    >>> nickel.worth()  # 5 cents + (80 - 50 years)
    35
    >>> mint.update()   # The mint's year is updated to 2101
    >>> Mint.present_year = 2176     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (155 - 50 years)
    115
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (155 - 50 years)
    125
    """
    present_year = 2021
    def __init__(self):
        self.update()

    def create(self, coin):
        "*** YOUR CODE HERE ***"
        return coin(self.year)

    def update(self):
        "*** YOUR CODE HERE ***"
        self.year=Mint.present_year


class Coin:
    cents = None  # will be provided by subclasses, but not by Coin itself

    def __init__(self, year):
        self.year = year

    def worth(self):
        "*** YOUR CODE HERE ***"
        temp=Mint.present_year-self.year-50
        if temp>0:
            return self.cents+temp
        else:
            return self.cents


class Nickel(Coin):
    cents = 5


class Dime(Coin):
    cents = 10


class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Nothing left to vend. Please restock.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must add $10 more funds.'
    >>> v.add_funds(7)
    'Current balance: $7'
    >>> v.vend()
    'You must add $3 more funds.'
    >>> v.add_funds(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.add_funds(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.add_funds(15)
    'Nothing left to vend. Please restock. Here is your $15.'
 
    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.add_funds(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    num=0
    funds=0
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def vend(self):
        if self.num>0:
            if self.funds>self.price:
               self.num-=1
               self.funds-=self.price
               print("'Here is your %s and $%d change.'"%(self.name,self.funds))
               self.funds=0
            elif self.funds==self.price:
               self.num-=1
               self.funds-=self.price
               print("'Here is your %s.'"%(self.name))
               self.funds=0
            else:
               print ("'You must add $%d more funds.'"%(self.price-self.funds))
        else:
            print("'Nothing left to vend. Please restock.'")
    def add_funds(self,money):
        self.funds+=money
        if self.num==0:
            print("'Nothing left to vend. Please restock. Here is your $%d.'"%(self.funds))
            self.funds=0
        else:
            print("'Current balance: $%d'"%(self.funds))
    def restock(self,number):
        self.num+=number
        print ("'Current %s stock: %d'"%(self.name,self.num))


