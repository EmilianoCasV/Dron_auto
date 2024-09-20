# djitellopy-examples
Examples about how to drive a DJI Tello Drone through Python 

.connect()       --> Conectar con el Dron
.get_baterry()   --> Tomar el valor de la Bateria
.takeoff()       --> Despege
.land()          --> Aterrisar
.move_forward(c) --> Mover hacia delante    (centimetros)
.move_back(c)    --> Mover hacia atras      (centimetros)
.move_left(c)    --> Mover a la izquierda   (centimetros)
.move_right(c)   --> Mover a la derecha     (centimetros)
.move_up(c)      --> Mover arriba           (centimetros)
.move_down(c)    --> Mover abajo            (centimetros)

.rotate_clockwise(d)            --> Girar como reloj (grados 0-360)
.rotate_counter_clockwise(d)    --> Girar en contra de reloj (grados 0-360)
.go_xyz_speed(x,y,z,speed)      --> Mediante cordenada (centimetros, y speed)

.flip_forward()     ||                               ||
.flip_back()        ||||  Truquitos para presumir  ||||
.flip_left()        |||||          :D             |||||
.flip_right()       ||                               ||

.streamon()  --> Activar camara
.get_frame_read() --> Aun no se muy bien
