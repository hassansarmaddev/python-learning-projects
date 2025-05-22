# ==========================================
# Example 1: Counting from 0 to 4
# ==========================================
# Problem Statement:
# Write a program that uses a while loop to print the numbers from 0 to 4.
# Start with x = 0. In each iteration, print the current value of x and then increase x by 1.
# The loop should stop automatically when x becomes 5 (i.e., when x is no longer less than 5).

"""
x = 0  # Initialize x with the value 0

while x < 5:  # Continue looping while x is less than 5
    print("Current Value:", x)  # Print the value of x
    x += 1  # Increase x by 1 in each iteration
"""

# ==========================================
# Example 2: Breaking the loop when x is 5
# ==========================================
# Problem Statement:
# Write a program that starts with x = 0 and uses a while loop to print x as long as x is less than 10.
# However, if x reaches 5, immediately exit the loop using the break statement.
# Print the value of x in each iteration before increasing it by 1.

"""
x = 0  # Start x at 0

while x < 10:  # Keep looping as long as x is less than 10
    if x == 5:  # If x reaches 5, break out of the loop
        break
    
    print("Running loop with x =", x)  # Print current value of x
    x += 1  # Increase x by 1 each time
"""

# ==========================================
# Example 3: Skipping even numbers
# ==========================================
# Problem Statement:
# Write a program that uses a while loop to print only the odd numbers between 1 and 10.
# Start with x = 0. In each iteration, increase x by 1.
# If x is an even number, skip the rest of the loop using continue.
# Print x only if it is odd.

"""
x = 0  # Initialize x

while x < 10:  # Continue looping while x is less than 10
    x += 1  # Increase x by 1 in each iteration
    
    if x % 2 == 0:  # If x is even
        continue  # Skip the rest of the loop and move to next iteration
    
    print("Odd number:", x)  # This prints only when x is odd
"""

# ==========================================
# Example 4: Skipping a specific number (x = 4)
# ==========================================
# Problem Statement:
# Write a program that uses a while loop to print the numbers from 1 to 7, except for the number 4.
# Start with x = 0. In each iteration, increase x by 1.
# If x is 4, skip printing that value using continue.
# Print all other values of x.

"""
x = 0  # Start at 0

while x < 7:  # Loop while x is less than 7
    x += 1  # Increase x
    
    if x == 4:  # If x is 4
        continue  # Skip printing x when x is 4
    
    print("Value:", x)  # Print x for all values except 4
"""

# ==========================================
# Example 5: Increasing x differently based on conditions
# ==========================================
# Problem Statement:
# Write a program that uses a while loop to print numbers from 1 to 9.
# Start with x = 1. If x is a multiple of 3, increase x by 2 and skip the rest of the loop using continue.
# Otherwise, print the value of x and increase it by 1.
# The loop should stop when x reaches 10.

"""
x = 1  # Start with x at 1

while x < 10:  # Loop while x is less than 10
    if x % 3 == 0:  # If x is a multiple of 3
        x += 2  # Increase x by 2 and skip the rest of the loop
        continue  
    
    print("Number:", x)  # Print the value of x
    x += 1  # Increase x at the end of each iteration
"""

# ==========================================
# Example 6: Breaking the loop when x reaches 5
# ==========================================
# Problem Statement:
# Write a program that uses a while loop to print numbers from 0 to 7.
# If x reaches 5, print "Breaking at x = 5" and exit the loop using break.
# Otherwise, print the value of x.
# After the loop ends, print "Loop ended."

"""
x = 0  # Start at 0

while x < 8:  # Continue looping while x is less than 8
    if x == 5:  # If x reaches 5
        print("Breaking at x =", x)  
        break  # Exit the loop
    
    print("Inside loop:", x)  # Print x
    x += 1  # Increase x each time

print("Loop ended.")  # This prints after the loop finishes
"""

# ==========================================
# Example 7: Counting down and exiting early
# ==========================================
# Problem Statement:
# Write a program that starts with x = 10 and uses a while loop to count down to 1.
# In each iteration, print the value of x and decrease it by 1.
# If x reaches 4, exit the loop early using break.
# After the loop, print "Loop exited before x reached 0."

"""
x = 10  # Start at 10

while x > 0:  # Loop while x is greater than 0
    if x == 4:  # If x reaches 4
        break  # Stop the loop

    print("Counting down:", x)  # Print the value of x
    x -= 1  # Decrease x by 1 each time

print("Loop exited before x reached 0.")
"""

# ==========================================
# Example 8: Skipping multiple values
# ==========================================
# Problem Statement:
# Write a program that uses a while loop to print the numbers from 1 to 6, except for 3 and 5.
# Start with x = 0. In each iteration, increase x by 1.
# If x is 3 or 5, skip printing that value using continue.
# Print all other values of x.

"""
x = 0  # Start at 0

while x < 6:  # Loop while x is less than 6
    x += 1  # Increase x
    
    if x == 3 or x == 5:  # If x is 3 or 5
        continue  # Skip the print statement
    
    print("Running with x =", x)  # Print x only when it's not 3 or 5
"""