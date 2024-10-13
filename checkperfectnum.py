#code to check whether a number is a perfect number or not 

def is_perfect(num):
    if num < 1:
        return False  # No perfect numbers less than 1
    
    # Find all divisors of the number (excluding the number itself)
    divisors_sum = sum(i for i in range(1, num) if num % i == 0)
    
    # Check if the sum of divisors equals the original number
    return divisors_sum == num

# Get user input
number = int(input("Enter a number: "))

# Check if the number is perfect
if is_perfect(number):
    print(f"{number} is a perfect number.")
else:
    print(f"{number} is not a perfect number.")
