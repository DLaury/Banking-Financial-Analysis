
def multiply_by_two(number):
  result = number * 2
  print(result)

if __name__ == "__main__":
  import sys
  if len(sys.argv) > 1:
    try:
      num = float(sys.argv[1])
      multiply_by_two(num)
    except ValueError:
      print("Invalid input. Please provide a number.")
  else:
    print("Please provide a number as a command line argument.")
