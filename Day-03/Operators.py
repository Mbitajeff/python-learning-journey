# Constants
SECONDS_IN_A_YEAR = 365 * 24 * 60 * 60  # Seconds in a year (ignoring leap years)
MAX_YEARS = 100  # Assumed maximum lifespan in years

# Prompt the user for input
years_lived = int(input("Enter number of years you have lived: "))

# Check if input exceeds the maximum lifespan
if years_lived > MAX_YEARS:
    print(f"A person is assumed to live up to {MAX_YEARS} years. Adjusting to {MAX_YEARS}.")
    years_lived = MAX_YEARS

# Calculate seconds lived
seconds_lived = years_lived * SECONDS_IN_A_YEAR

# Output the result
print(f"You have lived for {seconds_lived} seconds.")
