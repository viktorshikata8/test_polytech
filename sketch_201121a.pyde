ox, oy = 0, 0
v_x, v_y = 7.5, 5.5
g = 9.81
tim, a = 0.00, 0.00
v = 1
dim = 50.0
def setup():
    size(600, 400)
def draw():
    background(60);
    global ox, oy, v_x, v_y, g, tim, a
    tim = tim+0.0005
    ox = ox + v_x    
    if ox > width-35: 
        v_x = -v_x
    if oy > height-35: 
        v_y = -v_y
        a=-a;
    if ox < 0-15: 
        v_x = -v_x
    if oy < 0-15: 
        v_y = -v_y
        a=-a;    
    a = a+0.5*g*tim*tim
    oy = oy+v_y*tim+a
    translate(ox, oy)
    fill(255)
    ellipse(0+dim/2, dim/2, dim/2, dim/2)
