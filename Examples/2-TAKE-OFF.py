from djitellopy import Tello

tello = Tello()

tello.connect()
print(tello.get_battery())
tello.takeoff()

tello.land()