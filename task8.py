import argparse


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('nums', nargs='*')
  try:
    parsed = parser.parse_args()
    nums = parsed.nums
    if len(nums) == 0:
      print('NO PARAMS')
    elif len(nums) == 1:
      print('TOO FEW PARAMS')
    elif len(nums) > 2:
      print('TOO MANY PARAMS')
    else:
      val1 = int(nums[0])
      val2 = int(nums[1])
      print(val1 + val2)
  except Exception as e:
    print(type(e).__name__)


if __name__ == '__main__':
  main()