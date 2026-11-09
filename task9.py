import argparse


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--sort', action='store_true')
  parser.add_argument('pairs', nargs='*')
  parsed = parser.parse_args()

  parsed_dict = {}
  i = 0
  argv_list = parsed.pairs
  while i < len(argv_list):
    arg = argv_list[i]
    if '=' in arg:
      k, v = arg.split('=', 1)
      parsed_dict[k] = v
      i += 1
    else:
      if i + 1 < len(argv_list) and '=' not in argv_list[i + 1]:
        parsed_dict[argv_list[i]] = argv_list[i + 1]
        i += 2
      else:
        parsed_dict[arg] = ''
        i += 1

  items = list(parsed_dict.items())
  if parsed.sort:
    items.sort(key=lambda x: x[0])

  for k, v in items:
    print(f'Key: {k} Value: {v}')


if __name__ == '__main__':
  main()