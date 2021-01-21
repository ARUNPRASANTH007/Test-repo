# Bottle defect type
no_of_defective_bottles = 0
detect = input('Enter crack / shape / dust / no: ')

while True:
    no_of_defective_bottles += 1
    if detect == 'crack':
        print('A crack is detected on a bottle')
    elif detect == 'shape':
        print('The bottle is not in perfect shape')
    elif detect == 'dust':
        print('There is a foreign particle in the bottle')
    elif detect == 'no':
        no_of_defective_bottles -= 1
        print('Bottle is ready for filling')
    else:
        print('Invalid input')
        break

#counting the defective bottles
print('No. of defective bottles', no_of_defective_bottles)