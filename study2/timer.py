import time
def countdown_timer(seconds):
    while seconds>0:
        hours_remaining=seconds//3600
        minutes_remaining=(seconds%3600)//60
        seconds_remaining=seconds%60
        time.sleep(0.5)
        seconds-=1
        print(f"Осталось времени {hours_remaining:02d}:{minutes_remaining:02d}:{seconds_remaining:02d}")

    print("Время вышло")

# countdown_timer(500)


# Функция для форматирования времени
def format_time(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{hours:02}:{minutes:02}:{seconds:02}"

# Инициализируем начальное время в секундах
start_time = 0

while start_time<3666:
    print(f"Прошло {format_time(start_time)}")
    start_time += 1
    # Задержка на 1 секунду (1000 миллисекунд)
    for _ in range(1):
        pass
