# Bottle Detection and Indication
bottle_count = 0
while True:
    try:
        detect_bottle = bool(int(input()))
        bottle_count += 1
        if detect_bottle:
            print('A bottle is detected')
        else:
            print('No bottle is detected')
    except:
        print('No. of bottles', bottle_count)
        break

    
