#Simulate a basic self-driving car decision for traffic signs.
#The car should detect a traffic sign color (red/green) 
#and decide to pass it on the right (red) or left (green).

def traffic_sign_color():
    return input("Traffic sign color received from sensor,red/green: ").lower()
#depth camera input is used

def pass_direction(color):
    if color == "red":
        return "pass right"
    elif color == "green":
        return "pass left"
    else:
        return "color unrecognized,code error"
    

color = traffic_sign_color()
decide = pass_direction(color)
print("move", decide)