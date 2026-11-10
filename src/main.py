
namyeshgah = [
    {'name': 'pride'},
    {'name': 'perado'},
    {'name': 'benz'},
]


def main():
    while True:
        print('1) if u want to add a car.')
        print('2) if u want to remove.')
        print('3) if u want to show cars.')
        choose = input('Tell me the number: ')
        if choose == '1':
            add_car()
        elif choose == '2':
            remove_car()
        elif choose == '3':
            show_cars()

def show_cars():
    print(namyeshgah)

def add_car():
    car = {}
    while True:
        car['name'] = input('Tell me the name of the car: ')
        if not is_car_availible(car['name']):
            break
        print('you can\'t do it.')
    car['model'] = input('Tell me the model: ')
    car['color'] = input('Tell me the color: ')
    car['price'] = input('Tell me the price: ')
    namyeshgah.append(car)

def remove_car():
    while True:
        name = input('which car do u want to remove: ')
        for car in namyeshgah:
            print('checking:', car['name'])
            if car['name'] == name:
                print('dude')
                namyeshgah.remove(car)
                break
        else:
            print('couldn\'t find it.')
            continue
        break

def is_car_availible(name):
    for car in namyeshgah:
        if car['name'] == name:
            return True
    return False

if __name__ == '__main__':
    main()