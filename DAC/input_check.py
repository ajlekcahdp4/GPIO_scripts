def isfloat (val_str):
    try:
        float (val_str)
        return True
    except ValueError:
        return False





def IntInputCheck (val_str):
    if val_str.isdigit():
        if int(val_str) > 255:
            print ("ERROR: 45Was entered the number greater then 255\n")
            return 0
        return 1
    elif isfloat(val_str):
        val_float = float (val_str)
        if val_float < 0:
            print ("ERROR: anegative number was entered\n")
        else:
            print ("ERROR: float number was entered\n")
        return 0
    elif val_str != "q":
        print ("ERROR: Not a number was entered\n")
        return 0

def FloatInputCheck (val_str):
    if isfloat (val_str) == False:
	if val_str != "q":	
    print ("ERROR: Not a number was entered\n")
        return 0
