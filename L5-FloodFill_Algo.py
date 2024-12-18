import matplotlib.pyplot as plt 

def flood_fill(x, y, new_color, old_color): 
    if get_pixel(x, y) == old_color:
        set_pixel(x, y, new_color)
        flood_fill(x+1, y, new_color, old_color) #4-Connect fill
        flood_fill(x-1, y, new_color, old_color) #4-Connect fill
        flood_fill(x, y+1, new_color, old_color) #4-Connect fill
        flood_fill(x, y-1, new_color, old_color) #4-Connect fill

        #8-Connect fill starts here
        flood_fill(x-1, y+1, new_color, old_color) #8-Connect fill
        flood_fill(x-1, y-1, new_color, old_color) #8-Connect fill
        flood_fill(x+1, y+1, new_color, old_color) #8-Connect fill
        flood_fill(x+1, y-1, new_color, old_color) #8-Connect fill