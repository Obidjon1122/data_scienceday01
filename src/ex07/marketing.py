import sys

clients = ['andrew@gmail.com', 'jessica@gmail.com', 'ted@mosby.com','john@snow.is', 'bill_gates@live.com', 'mark@facebook.com','elon@paypal.com', 'jessica@gmail.com']
participants = ['walter@heisenberg.com', 'vasily@mail.ru','pinkman@yo.org', 'jessica@gmail.com', 'elon@paypal.com','pinkman@yo.org', 'mr@robot.gov', 'eleven@yahoo.com']
recipients = ['andrew@gmail.com', 'jessica@gmail.com', 'john@snow.is']


def operator():
    if len(sys.argv) == 2:
        if sys.argv[1] == 'call_center':
            return list(set(clients)-set(recipients))
        elif sys.argv[1] == 'potential_clients':
            return list(set(participants)-set(clients))
        elif sys.argv[1] == 'loyalty_program':
            return list(set(clients)-set(participants))
        else:
            print('Invalid argument. Use "call_center", "potential_clients", or "loyalty_program".')

if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(operator())
    else:
        print('Please provide an argument: "call_center", "potential_clients", or "loyalty_program".')
# The script takes a command line argument and returns a list of emails based on the argument.
# The three options are:
# 1. call_center: returns a list of clients who are not in the recipients list.
# 2. potential_clients: returns a list of participants who are not in the clients list.
# 3. loyalty_program: returns a list of clients who are not in the participants list.