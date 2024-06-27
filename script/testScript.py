import sys

# Check if the correct number of arguments is provided
if len(sys.argv) != 3:
    print("Usage: python your_script.py <param1> <param2>")
    sys.exit(1)

# Read parameters from command line arguments
param1 = sys.argv[1]
param2 = sys.argv[2]

# Display the received parameters
print(f"Received parameters: param1 = {param1}, param2 = {param2}")
