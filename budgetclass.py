class budget:
    def __init__(self, name):
        self.name = name 

        """
         This is a budget class for the Zuri internship assignment.

        """ 


    def deposit(self):
        print('====== DEPOSIT =====')
        print(f'You want to deposit for {self.name}')
        self.current_balance = 100000
        put_in = int(input('How much do you want to deposit? \n'))
        print(f'You have deposited {put_in} Naira for {self.name}')
        print(f'Your current balance for {self.name} Naira is {self.current_balance + put_in} ')
        self.current_balance = self.current_balance + put_in

        """

        For the deposit function of the classes, i created a code that has an initial deposit of 10000 naira
        and also adds what ever the input of the deposit is to the initial deposit

        """

    def withdrawal(self):
        print('===== WITHDRAWAL =====')
        self.current_balance = 100000
        print(f'You have selected withdrawal for {self.name}')
        take_out = int(input('How much do you want to withdraw? \n'))
        print(f'You have withdrawn {take_out} Naira from {self.name}')
        self.current_balance = self.current_balance - take_out

        """

        For the withdrawal function of the classes, i created a code that deducts the input of the user from 
        the current balance of the category.

        """


    def balance(self):
        print('===== CHECK BALANCE =====')
        print('You have selected the balance option')
        print(f'Your balance for {self.name} is {self.current_balance} naira ')

    
        
food = budget('Monthly food')
clothing = budget('School clothing')
entertainment = budget('Occasional entertainment')

# please input the category and the method you want to perform an operation on

