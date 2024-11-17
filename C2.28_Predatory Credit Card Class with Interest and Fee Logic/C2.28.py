# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

    """An extension to CreditCard that compounds interest and fees."""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance.
        The initial balance is zero.
        customer the name of the customer (e.g., 'John Bowman')
        bank the name of the bank (e.g., 'California Savings')
        acnt the acount identifier (e.g., '5391 0375 9387 5309')
        limit credit limit (measured in dollars)
        apr annual percentage rate (e.g., 0.0825 for 8.25% APR)
        """
        super().__init__(customer, bank, acnt, limit)                                  #The class has an __init__ method that takes the customer name, bank name, account identifier, credit limit,
                                                                                     # and annual percentage rate (APR) as input parameters.
                                                                                       # The method initializes the card's balance to 0 and calls the __init__ method of the parent CreditCard class using the super() function.
        self._apr = apr
        self._charge_count = 0

    def charge(self, price):
        """Charge given price to the card, assuming sufficient credit limit.
        Return True if charge was processed.
        Return False and assess $5 fee if charge is denied.
        """
        if self._charge_count >= 10:                                            #The class has several accessor methods that return the customer name, bank name, account identifier, credit limit, and balance of the card.

                                                                    #Overall, the modified class provides a credit card that charges a $1 surcharge for each charge beyond the first 10 charges in a given month,
            self._balance += 1 # assess surcharge
        success = super().charge(price) # call inherited method
        if not success:
            self._balance += 5 # assess penalty
        self._charge_count += 1
        return success # caller expects return value

    def process_month(self):
        """Assess monthly interest on outstanding balance."""
        if self._balance > 0:
            # if positive balance, convert APR to monthly multiplicative factor
            monthly_factor = pow(1 + self._apr, 1/12)
            self._balance *= monthly_factor
        self._charge_count = 0

        print("Paolo lauricella project C")