# WARNING: The pseudo-random generators of this module SHOULD NOT be used for security purposes.
# Use "os.urandom()" or "SystemRandom" if you require a cryptographically secure pseudo-random number generator.

# Import random module then print directory.
import random
print(dir(random), "\n")

#================================================================

# We will use the random.random() function to generate 10 random numbers.
print("10 randomly generated numbers: ")
for i in range(10):
    print(random.random())
print(38 * "=", "\n")

#================================================================

# Use random.uniform() function to generate 10 random numbers from interval [3, 7).
print(help(random.uniform), "\n")


print("10 Randomly generated numbers from interval [3, 7): ")
for i in range(10):
    print(random.uniform(3,7))
print(38 * "=", "\n")

#================================================================

# Use random.randint() function to generate 10 random numbers between 1-10.
print(help(random.randint), "\n")

print("10 Randomly generated integers from interval [1,10]: ")
for i in range(10):
    print(random.randint(1,10))
print(38 * "=", "\n")

#================================================================

# Use random.choice() function to simulate rock, paper, scissors game.
print(help(random.choice) , "\n")

print("3 Random choices for rock, paper, scissors game: ")
outcomes = ['rock', 'paper', 'scissors']
for i in range(3):
    print(random.choice(outcomes))  # Passes in sequence data called "outcomes" to "random.choice()" 
print(38 * "=", "\n")
