from threading import Thread
import time


def car(speed, pilot):
    distance = 0
    while distance <= 100:
        print('Car {}: {}\n'.format(pilot, distance))
        distance += speed
        time.sleep(0.5)


if __name__ == '__main__':
    car_thread_1 = Thread(target=car, args=[1, 'Alec'])
    car_thread_2 = Thread(target=car, args=[1.5, 'Brandon'])
    car_thread_1.start()
    car_thread_2.start()
