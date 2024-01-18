# Практика -> leetcode - 2 задачи лёгкого уровня на выбор


# Given a valid (IPv4) IP address, return a defanged version of that IP address.
# A defanged IP address replaces every period "." with "[.]".
# Example 1:
# Input: address = "1.1.1.1"
# Output: "1[.]1[.]1[.]1"

# Example 2:
# Input: address = "255.100.50.0"
# Output: "255[.]100[.]50[.]0"


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")

    # There is a programming language with only four operations and one variable X:
    #
    # ++X and X++ increments the value of the variable X by 1.
    # --X and X-- decrements the value of the variable X by 1.
    # Initially, the value of X is 0.
    #
    # Given an array of strings operations containing a list of operations, return the final value of X after
    # performing all the operations.
    #
    #
    #
    # Example 1:
    #
    # Input: operations = ["--X","X++","X++"]
    # Output: 1
    # Explanation: The operations are performed as follows:
    # Initially, X = 0.
    # --X: X is decremented by 1, X =  0 - 1 = -1.
    # X++: X is incremented by 1, X = -1 + 1 =  0.
    # X++: X is incremented by 1, X =  0 + 1 =  1.
    # Example 2:
    #
    # Input: operations = ["++X","++X","X++"]
    # Output: 3
    # Explanation: The operations are performed as follows:
    # Initially, X = 0.
    # ++X: X is incremented by 1, X = 0 + 1 = 1.
    # ++X: X is incremented by 1, X = 1 + 1 = 2.
    # X++: X is incremented by 1, X = 2 + 1 = 3.
    # Example 3:
    #
    # Input: operations = ["X++","++X","--X","X--"]
    # Output: 0
    # Explanation: The operations are performed as follows:
    # Initially, X = 0.
    # X++: X is incremented by 1, X = 0 + 1 = 1.
    # ++X: X is incremented by 1, X = 1 + 1 = 2.
    # --X: X is decremented by 1, X = 2 - 1 = 1.
    # X--: X is decremented by 1, X = 1 - 1 = 0.
    #
    def finalValueAfterOperations(self, operations):
        x = 0
        for i in operations:
            if i == "++X" or i == "X++":
                x += 1
            elif i == "--X" or i == "X--":
                x -= 1
        return x


sol1 = Solution()
address1 = "1.1.1.1"
address2 = "255.255.255.0"
sol2 = Solution()
op = ["X++", "++X", "--X"]

if __name__ == "__main__":
    print(sol1.defangIPaddr(address1))
    print(sol1.defangIPaddr(address2))
    print(sol2.finalValueAfterOperations(op))
