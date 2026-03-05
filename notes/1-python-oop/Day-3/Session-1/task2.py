'''
### ⚡ Micro Task 2 (5 min)

Create a `BankAccount` class where:
- Class variables: minimum balance (1000), max daily withdrawals (3), bank name ("National Bank")
- Instance variables: owner, balance, daily withdrawal count

Write a `withdraw` method that:
- Checks if daily withdrawal limit reached (using class variable)
- Checks if withdrawal would go below minimum balance (using class variable)
- Raises appropriate errors for both cases

Create 2 accounts. Withdraw from one 3 times (should work). Try 4th withdrawal (should fail with limit error). Verify the other account still has 3 withdrawals available (independent counter).
'''

class BankAccount:
    minimun_balance = 1000
    max_daily_withdrawls = 3
    bank_name = "National Bank"

    def __init__(self,owner:str,balance:float):
        self.owner:str = owner
        self.balance:float = balance
        self.daily_withdrawls_count:int = 0
    
    def withdraw(self,amount:float)->None:
        if BankAccount.max_daily_withdrawls == self.daily_withdrawls_count:
            raise ValueError("Withdrawl limit reached")
        if self.balance - amount <BankAccount.minimun_balance:
            raise ValueError("Transaction makes the balance less than minimum balance")
        self.daily_withdrawls_count += 1 
        self.balance -= amount
        


if __name__ == "__main__":

    # Test 1: Basic initialization
    try:
        acc = BankAccount("Alice", 5000)
        assert acc.owner == "Alice"
        assert acc.balance == 5000
        print("Test 1 passed: Initialization works")
    except Exception as e:
        print(f"Test 1 failed: {e}")

    # Test 2: First withdrawal — WILL FAIL (AttributeError)
    try:
        acc = BankAccount("Bob", 5000)
        acc.withdraw(500)
        assert acc.balance == 4500
        print("Test 2 passed: Withdrawal works")
    except AttributeError as e:
        print(f"Test 2 FAILED: {e}")
    except Exception as e:
        print(f"Test 2 failed: {e}")

    # Test 3: Check if counter attribute exists
    try:
        acc = BankAccount("Charlie", 5000)
        # Your code creates 'max_daily_withdrawls' but references 'daily_withdrawls_count'
        assert hasattr(acc, 'daily_withdrawls_count'), "Missing daily_withdrawls_count attribute"
        print("Test 3 passed")
    except AssertionError as e:
        print(f"Test 3 FAILED: {e}")

    # Test 4: Three withdrawals should work
    try:
        acc = BankAccount("Diana", 10000)
        acc.withdraw(500)
        acc.withdraw(500)
        acc.withdraw(500)
        assert acc.balance == 8500
        print("Test 4 passed: Three withdrawals work")
    except Exception as e:
        print(f"Test 4 failed: {e}")

    # Test 5: Fourth withdrawal should fail with limit error
    try:
        acc = BankAccount("Eve", 10000)
        acc.withdraw(500)
        acc.withdraw(500)
        acc.withdraw(500)
        acc.withdraw(500)  # 4th should fail
        print("Test 5 FAILED: Should have raised ValueError for limit")
    except ValueError as e:
        if "limit" in str(e).lower():
            print("Test 5 passed: 4th withdrawal blocked")
        else:
            print(f"Test 5 failed: Wrong error — {e}")
    except Exception as e:
        print(f"Test 5 failed: {e}")

    # Test 6: Independent counters for different accounts
    try:
        acc1 = BankAccount("Frank", 10000)
        acc2 = BankAccount("Grace", 10000)
        
        # Withdraw 3 times from acc1
        acc1.withdraw(500)
        acc1.withdraw(500)
        acc1.withdraw(500)
        
        # acc2 should still have 3 withdrawals available
        acc2.withdraw(500)  # Should work
        assert acc2.balance == 9500
        print("Test 6 passed: Accounts have independent counters")
    except Exception as e:
        print(f"Test 6 failed: {e}")

    # Test 7: Minimum balance check
    try:
        acc = BankAccount("Henry", 1500)
        acc.withdraw(600)  # Would leave 900, below minimum 1000
        print("Test 7 FAILED: Should have raised ValueError for minimum balance")
    except ValueError as e:
        if "minimum" in str(e).lower():
            print("Test 7 passed: Minimum balance enforced")
        else:
            print(f"Test 7 failed: Wrong error — {e}")

    print("\nAll tests completed!")