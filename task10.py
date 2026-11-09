import argparse
import textwrap


def format_text_block(frame_height, frame_width, file_name):
  """Форматирует текстовый файл под заданные размеры рамки и возвращает отформатированный текст.

  В случае ошибки работы с файлом возвращает текст исключения.
  """
  try:
    with open(file_name, 'r', encoding='utf-8') as f:
      content = f.read()

    wrapped_lines = []
    for line in content.splitlines():
      if not line.strip():
        wrapped_lines.append('')
      else:
        wrapped = textwrap.wrap(line, width=frame_width)
        if not wrapped:
          wrapped_lines.append('')
        else:
          wrapped_lines.extend(wrapped)

    result_lines = wrapped_lines[:frame_height]
    return '\n'.join(result_lines)
  except Exception as e:
    return str(e)


def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--frame-height', type=int, required=True)
  parser.add_argument('--frame-width', type=int, required=True)
  parser.add_argument('filename')
  parsed = parser.parse_args()

  res = format_text_block(
      parsed.frame_height, parsed.frame_width, parsed.filename
  )
  print(res)


if __name__ == '__main__':
  main()