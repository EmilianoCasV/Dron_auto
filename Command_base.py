from djitellopy import Tello
tello = Tello()
print("Conectado con exito")
print(tello.get_battery)
tello.takeoff()
tello.move_forward(100)
tello.move_up(150)
tello.rotate_clockwise(90)
tello.move_up(20)
tello.land()