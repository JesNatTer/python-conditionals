speed_limit = int(input("ENTER THE SPEED LIMIT OF ROAD:"))
speed = int(input("ENTER YOUR DRIVING SPEED:"))
points = (speed - speed_limit)/5
if speed <= 60:
    print("OK")
elif speed > speed_limit:
    if points > 12:
        print("You going to jail lmao. Demerit Points:" + str(points))
    else:
        print("Demerit Points:" + str(points))
