import random
import time
import numpy as np
from itertools import product

# Number of test runs
num_tests = 10

# Function to calculate the entropy of a probability distribution
def calculate_entropy(probabilities):
    return -np.sum(probabilities * np.log2(probabilities))

# Function to generate probabilities based on entropy and guess frequency
def generate_probability_distribution(remaining_digits):
    # Uniform distribution over remaining digits
    prob = np.ones(len(remaining_digits)) / len(remaining_digits)
    return prob

# Number of tests to run
total_time = 0
total_attempts = 0

print(f"Running entropy-based brute-force attack {num_tests} times...\n")

for test in range(1, num_tests + 1):
    # Generate a random 6-digit passcode
    passcode = [random.randint(0, 9) for _ in range(6)]
    passcode_str = "".join(map(str, passcode))

    print(f"Test {test}: Passcode is {passcode_str}")

    # Start timer
    start_time = time.time()

    # Track remaining digits for each position (initially all digits 0-9)
    remaining_digits = [list(range(10)) for _ in range(6)]

    # Store the attempts and guesses
    attempts = 0
    found_passcode = False

    while not found_passcode:
        # Generate a guess based on the most probable values
        guess = []
        for i in range(6):
            prob = generate_probability_distribution(remaining_digits[i])
            chosen_digit = np.random.choice(remaining_digits[i], p=prob)
            guess.append(chosen_digit)

        guess_str = "".join(map(str, guess))
        attempts += 1

        print(f"Attempt {attempts}: Trying {guess_str}...", end=" ")

        if guess_str == passcode_str:
            found_passcode = True
            print("Correct! Passcode cracked.")
        else:
            print("Incorrect.")
            # Reduce the remaining digits for each incorrect guess
            for i in range(6):
                if guess[i] != passcode[i]:
                    remaining_digits[i].remove(guess[i])

    # Stop timer
    end_time = time.time()

    # Calculate time taken and store results
    time_taken = end_time - start_time
    total_time += time_taken
    total_attempts += attempts

    print(f"Test {test} completed: {attempts} attempts, {time_taken:.4f} seconds\n")

# Calculate and print averages
average_time = total_time / num_tests
average_attempts = total_attempts / num_tests

print(f"\n--- Entropy-based Brute-Force Summary ---")
print(f"Average time taken: {average_time:.4f} seconds")
print(f"Average attempts needed: {average_attempts:.0f}")
