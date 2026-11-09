from datetime import datetime
import os
import shutil
import sys


def make_reserve_arc(source, dest):
  if not os.path.exists(source):
    raise FileNotFoundError(f'Каталог {source} не найден.')

  os.makedirs(dest, exist_ok=True)
  timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
  base_name = os.path.join(dest, f'reserve_{timestamp}')
  archive_path = shutil.make_archive(base_name, 'zip', source)
  print(f'Архив успешно создан: {archive_path}')
  return archive_path


if __name__ == '__main__':
  src = sys.argv[1] if len(sys.argv) > 1 else '.'
  dst = sys.argv[2] if len(sys.argv) > 2 else './backups'
  make_reserve_arc(src, dst)