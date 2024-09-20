from djitellopy import Tello

tello = Tello()

tello.connect()

print(tello.get_battery())

tello.takeoff()

tello.go_xyz_speed(100,-100,100,100)
tello.go_xyz_speed(-100,100,-100,100)

tello.go_xyz_speed(100,100,100,100)
tello.go_xyz_speed(-100,-100,-100,100)

tello.go_xyz_speed(-100,100,100,100)
tello.go_xyz_speed(100,-100,-100,100)

tello.go_xyz_speed(-100,-100,100,100)
tello.go_xyz_speed(100,100,-100,100)



tello.land()