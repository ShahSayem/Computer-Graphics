import matplotlib.pyplot as plt 

def boundary_fill(x, y, fill_color, boundary_color):
    if get_pixel(x, y) != boundary_color and get_pixel(x, y) != fill_color:
        set_pixel(x, y, fill_color)
        boundary_fill(x+1, y, fill_color, boundary_color) #4-Connect fill
        boundary_fill(x-1, y, fill_color, boundary_color) #4-Connect fill
        boundary_fill(x, y+1, fill_color, boundary_color) #4-Connect fill
        boundary_fill(x, y-1, fill_color, boundary_color) #4-Connect fill

        #8-Connect fill starts here
        boundary_fill(x-1, y+1, fill_color, boundary_color) #8-Connect fill
        boundary_fill(x-1, y-1, fill_color, boundary_color) #8-Connect fill
        boundary_fill(x+1, y+1, fill_color, boundary_color) #8-Connect fill
        boundary_fill(x+1, y-1, fill_color, boundary_color) #8-Connect fill