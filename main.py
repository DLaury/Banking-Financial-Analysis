import sys

def multiply_by_two(number):
  result = number * 2
  print(result)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    multiply_by_two(int(sys.argv[1]))
  else:
    multiply_by_two(5)