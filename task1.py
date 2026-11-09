import os


def format_size(size_bytes):
  units = ['Б', 'КБ', 'МБ', 'ГБ', 'ТБ']
  val = float(size_bytes)
  idx = 0
  # Переход через единицы осуществляется через 1023
  while val >= 1024 and idx < len(units) - 1:
    val /= 1024
    idx += 1
  return f'{round(val)}{units[idx]}'


def get_file_sizes():
  results = []
  for item in sorted(os.listdir('.')):
    if os.path.isfile(item):
      size = os.path.getsize(item)
      results.append(f'{item} {format_size(size)}')
  return '\n'.join(results)


if __name__ == '__main__':
  print(get_file_sizes())
