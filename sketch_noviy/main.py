import serial.tools.list_ports
import time
# # Получаем список доступных Serial портов
# # ports = list(serial.tools.list_ports.comports())
# # # Выводим информацию о каждом порте
# # for port in ports:
# #     print(f"Порт: {port.device}")
# #     print(f"Описание: {port.description}")
# #     print(f"Производитель: {port.manufacturer}\n")
ser = serial.Serial('COM16', 9600)
x = int(input())

while True:
    ser.write(b'1')
    time.sleep(1)
    ser.write(b'2')
    time.sleep(1)
    ser.write(b'3')

ser.close()