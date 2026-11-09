import os
import sys


def format_size(size_bytes):
  units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
  val = float(size_bytes)
  idx = 0
  while val >= 1024 and idx < len(units) - 1:
    val /= 1024
    idx += 1
  return f'{round(val)}{units[idx]}'


def get_top_cluttered_dirs(target_path='.', top_n=10):
  items_sizes = {}

  for root, dirs, files in os.walk(target_path):
    for f in files:
      fp = os.path.join(root, f)
      try:
        sz = os.path.getsize(fp)
        curr = root
        while True:
          items_sizes[curr] = items_sizes.get(curr, 0) + sz
          parent = os.path.dirname(curr)
          if parent == curr:
            break
          curr = parent
      except (OSError, FileNotFoundError):
        pass

    for f in files:
      fp = os.path.join(root, f)
      try:
        sz = os.path.getsize(fp)
        items_sizes[fp] = sz
      except (OSError, FileNotFoundError):
        pass

  sorted_items = sorted(items_sizes.items(), key=lambda x: x[1], reverse=True)

  output = []
  for path, sz in sorted_items[:top_n]:
    name = os.path.basename(path) or path
    output.append(f'{name}\n | {format_size(sz)}')

  return '\n\n'.join(output)


if __name__ == '__main__':
  path_to_scan = sys.argv[1] if len(sys.argv) > 1 else '.'
  print(get_top_cluttered_dirs(path_to_scan))