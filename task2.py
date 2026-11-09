import os
import sys
import zipfile


def format_size(size_bytes):
  units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
  val = float(size_bytes)
  idx = 0
  while val >= 1024 and idx < len(units) - 1:
    val /= 1024
    idx += 1
  return f'{round(val)}{units[idx]}'


def print_zip_structure(zip_path):
  if not os.path.exists(zip_path):
    return

  with zipfile.ZipFile(zip_path, 'r') as zf:
    infolist = zf.infolist()
    if not infolist:
      return

    tree = {}
    for info in infolist:
      parts = [p for p in info.filename.split('/') if p]
      if not parts:
        continue
      is_dir = info.is_dir() or info.filename.endswith('/')
      curr = tree
      for i, part in enumerate(parts):
        if part not in curr:
          curr[part] = {} if (i < len(parts) - 1 or is_dir) else info.file_size
        else:
          if not isinstance(curr[part], dict) and i < len(parts) - 1:
            curr[part] = {'_size': curr[part]}
        curr = curr[part] if isinstance(curr[part], dict) else curr

    def _print_tree(node, depth=0):
      for name, val in sorted(node.items()):
        if name == '_size':
          continue
        indent = '  ' * depth
        if isinstance(val, dict):
          print(f'{indent}{name}')
          _print_tree(val, depth + 1)
        else:
          print(f'{indent}{name} {format_size(val)}')

    _print_tree(tree)


if __name__ == '__main__':
  archive_name = sys.argv[1] if len(sys.argv) > 1 else 'archive.zip'
  print_zip_structure(archive_name)