'''
### ⚡ Micro Task 2 (7 min)

Create a `UserProfile` class with name (required), bio (optional, could be None), age (optional, could be None — but 0 IS a valid age for a baby account).

Write these methods using the correct None-handling pattern:
- `get_bio_display()` → returns bio or "No bio set" if None
- `get_age_display()` → returns age or "Age not provided" if None (**careful: 0 is valid!**)
- `get_profile_completeness()` → returns percentage (name=40%, bio=30%, age=30%)
- `is_complete()` → True if nothing is None

Test with: a fully complete profile, a profile with only name, and a profile with age=0.
'''

class UserProfile:
    def __init__(self,name:str,bio:str|None=None,age:int|None=None):
        self.name=name
        self.bio=bio
        self.age=age
    def get_bio_display(self)->str:
        return self.bio if self.bio is not None else "No bio set"
    def get_age_display(self)->int|str:
        if self.age is None:
            return "Age not provided"
        return self.age
    def get_profile_completeness(self)->int:
       percentage=40
       if self.bio is not None:
           percentage += 30
       if self.age is not None:
           percentage +=30
       return percentage
    def is_complete(self)->bool:
        if self.age is not None and self.bio is not None:
            return True
        return False
    

if __name__ == "__main__":

    # Test 1: Fully complete profile
    try:
        user1 = UserProfile("Alice", "Love coding", 25)
        assert user1.get_bio_display() == "Love coding"
        assert user1.get_age_display() == 25
        assert user1.is_complete() == True
        print("Test 1 passed: Complete profile works")
    except Exception as e:
        print(f"Test 1 failed: {e}")

    # Test 2: Profile with only name
    try:
        user2 = UserProfile("Bob")
        assert user2.get_bio_display() == "No bio set"
        assert user2.get_age_display() == "Age not provided"
        assert user2.is_complete() == False
        print("Test 2 passed: Name-only profile works")
    except Exception as e:
        print(f"Test 2 failed: {e}")

    # Test 3: Profile with age=0 (baby account) — CRITICAL TEST
    try:
        user3 = UserProfile("Baby", "Newborn", 0)
        result = user3.get_age_display()
        assert result == 0, f"Expected 0, got {result}"
        print("Test 3 passed: age=0 handled correctly")
    except Exception as e:
        print(f"Test 3 failed: {e}")

    # Test 4: get_bio_display with empty string — POTENTIAL BUG
    try:
        user4 = UserProfile("Test", "", 20)
        result = user4.get_bio_display()
        # Empty string IS a valid bio (user cleared it intentionally)
        # But your code returns "No bio set" due to `or` pattern
        assert result == "", f"Expected empty string, got '{result}'"
        print("Test 4 passed")
    except AssertionError as e:
        print(f"Test 4 FAILED: Empty string bio treated as None — {e}")

    # Test 5: get_profile_completeness — WRONG IMPLEMENTATION
    try:
        user5 = UserProfile("Alice", "Bio here", 25)
        result = user5.get_profile_completeness()
        # Should return a NUMBER (percentage), not a dict!
        # Full profile = 40 + 30 + 30 = 100%
        assert result == 100, f"Expected 100, got {result}"
        print("Test 5 passed")
    except AssertionError as e:
        print(f"Test 5 FAILED: Should return percentage number, not dict — {e}")

    # Test 6: get_profile_completeness with only name
    try:
        user6 = UserProfile("Bob")
        result = user6.get_profile_completeness()
        # Only name = 40%
        assert result == 40, f"Expected 40, got {result}"
        print("Test 6 passed")
    except AssertionError as e:
        print(f"Test 6 FAILED: {e}")

    # Test 7: get_profile_completeness with name + age=0
    try:
        user7 = UserProfile("Baby", None, 0)
        result = user7.get_profile_completeness()
        # name(40) + age(30) = 70%
        assert result == 70, f"Expected 70, got {result}"
        print("Test 7 passed")
    except AssertionError as e:
        print(f"Test 7 FAILED: {e}")

    print("\nAll tests completed!")