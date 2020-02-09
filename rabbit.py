import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
same = True

while same:

    print('Choose form the menu options')
    print('1: Enter coordinates')
    print('2 exit')

    userInput = input()

    if userInput == '1':
        print('please enter x coordinate')
        userInputXCoordinate = input()
        print('please enter y coordinate')
        userInputYCoordinate = input()

        body = userInputXCoordinate + ' ' + userInputYCoordinate

        channel.queue_declare(queue='CVstats')
        channel.basic_publish(exchange='',
                              routing_key='CVstats',
                              body=body)

    elif userInput == '2':
        same = False

    else:
        print('Enter a valid menu option')

connection.close()
