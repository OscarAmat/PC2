def patron(numero):
    for i in range(1, numero + 1):
        print('* ' * i)
    for i in range(numero - 1, 0, -1):
        print('* ' * i)

patron(5)