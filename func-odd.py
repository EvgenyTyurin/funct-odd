# Bill Lubanovich "Introducing Python"
# Chapter 4, Exercises: Create function returning third odd number

odd_idx = 3

# Returns odd number by index in range
# using comprehension and generator
def odd_n(idx):
    # Make odd numbers
    odd_numbers = (number for number in range(idx * 2) if number % 2 != 0)
    # Find odd number by idx
    count = 0
    for number in odd_numbers:
        count += 1
        if count == idx:
            return number
    
print( "Odd number number " + str(odd_idx) + " is " + str( odd_n(odd_idx) ) )
