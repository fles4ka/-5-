from datetime import datetime
import time
import schedule


def cuckoo_job():
  now = datetime.now()
  # В зависимости от 12-часового формата часа выводим от 1 до 12 раз "Ку"
  count = now.hour % 12
  if count == 0:
    count = 12
  print('Ку' * count)


if __name__ == '__main__':
  schedule.every().hour.at(':00').do(cuckoo_job)
  print('Планировщик запущен. Нажмите Ctrl+C для выхода.')
  while True:
    schedule.run_pending()
    time.sleep(1)