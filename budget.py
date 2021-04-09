class BudgetCategory:
    def __init__(self, categoryName):
        self.categoryName = categoryName
        self.budgetAccount = []
        

    def deposit(self, amount):
        self.budgetAccount.append({"amount": amount})
        print("%s category have initial deposit of %d" % (self.categoryName, amount))
        
    def withdraw(self, amount):    
            if self.inspectFundUsage(amount): 
                self.budgetAccount.append({"amount": -amount})
                print("You withdraw %d from %s category and your balance is %d" % (amount, self.categoryName, self.categoryBalance()))
            else:
                return False
    
    def categoryBalance(self):
        totalAmount = 0
        for amount in self.budgetAccount:
            totalAmount = totalAmount + amount["amount"]
        return totalAmount

    def inspectFundUsage(self, amount):
        if amount <= self.categoryBalance():
            return True
        else:
            return False    

    def transfer(self, amount, category):
        if self.inspectFundUsage(amount):       
            self.withdraw(amount)
            category.deposit(amount)
            print(f"{amount} transferred to %s category from %s category" % (category.categoryName, self.categoryName))

#All Category Instances
Clothings = BudgetCategory("Clothings")
Food = BudgetCategory("Food")
Entertainment = BudgetCategory("Entertainment")   

#Clothings category Account# 
print("clothing Category Instances")           
Clothings.deposit(1000)
Clothings.withdraw(200)
Clothings.transfer(300, Food)
print(f"Balance: {Clothings.categoryBalance()}")

#Food Category Account#
print("###Food Category Instances##")
Food.deposit(2000)
Food.withdraw(400)
Food.transfer(500, Entertainment)
print(f"Balance: {Food.categoryBalance()}")

#Entertainment Category Account#
print("####Entertainment Category Instances#####")
Entertainment.deposit(2000)
Entertainment.withdraw(400)
Entertainment.transfer(500, Clothings)
print(f"Balance: {Entertainment.categoryBalance()}")


        