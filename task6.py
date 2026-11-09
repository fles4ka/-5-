import sys


def parse_sys_argv():
  argv = sys.argv[1:]
  sort_flag = '--sort' in argv
  if sort_flag:
    argv = [arg for arg in argv if arg != '--sort']

  parsed = {}
  i = 0
  while i < len(argv):
    arg = argv[i]
    if '=' in arg:
      k, v = arg.split('=', 1)
      parsed[k] = v
      i += 1
    else:
      if i + 1 < len(argv) and '=' not in argv[i + 1]:
        parsed[argv[i]] = argv[i + 1]
        i += 2
      else:
        parsed[arg] = ''
        i += 1

  items = list(parsed.items())
  if sort_flag:
    items.sort(key=lambda x: x[0])

  for k, v in items:
    print(f'Key: {k} Value: {v}')


if __name__ == '__main__':
  parse_sys_argv()