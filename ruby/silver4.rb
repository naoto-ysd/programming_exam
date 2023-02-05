# transfer method is for users to transfer money to another bank acocunt. 

class BankAccount
  attr_reader :balance

  def initialize(starting_balance)
    @balance = starting_balance
  end

  def deposit(amount)
    @balance += amount
  end

  def withdraw(amount)
    @balance -= amount
  end

  def transfer(amount, other_account)
    withdraw(amount)
    other_account.deposit(amount)
  end
end
