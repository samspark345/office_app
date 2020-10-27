def welcome_message(name, greeting):
    '''(str,str)->None
        input must be a string
        prints a message to the screen when called '''
    add = "__"
    starts = (len(name)+len(greeting)+len(add)*2+2)
    print()
    print(starts*"*")
    print("*"+(starts-2)*" "+"*")
    print("*"+add+name+greeting+add+"*")
    print("*" + (starts - 2) * " " + "*")
    print(starts * "*")
    print()


class employee:
    def __init__(self, name, email, tag, work):

        self.name = name
        self.email = email
        self.tag = tag
        self.position = position


class worker(employee):
    '''
     a class that inherits from the main employee class
    '''
    users = {}

    def add(self):
        '''
        (None) -> None
        adds a user to the worker systems
        '''
        worker.users[self.name.strip()] = (self.tag, self.email)

    @classmethod
    def remove(cls, name):
        '''
        (None) -> None
        removes a user from the maintainance systems
        '''
        if name in worker.users:
            del worker.users[name]
            print("you are now logged out")

    @classmethod
    def pr_user(cls):
        '''
        (None) -> None
        displays the users using the worker systems
        '''
        if len(worker.users) >= 1:
            for keys in worker.users:
                print(("admin systems users {}:{}").format(keys, worker.users[keys]))


class admin(employee):
    '''
     a class that inherits from the main employee class
    '''

    users = {}

    def add(self):
        '''
        (None) -> None
        adds a user to the admin systems
        '''
        admin.users[self.name.strip()] = (self.tag, self.email)

    @classmethod
    def remove(cls, name):
        '''
        (None) -> None
        removes a user from the admin systems
        '''
        if name in admin.users:
            del admin.users[name]
            print("{} you are now logged out")

    @classmethod
    def pr_user(cls):
        '''
        (None) -> None
        displays the users using the admin systems
        '''
        if len(admin.users) >= 1:
            for keys in admin.users:
                print(("admin systems users {}:{}").format(keys, admin.users[keys]))


class maintainance(employee):
    '''
     a class that inherits from the main employee class
    '''
    users = {}

    def add(self):
        '''
     adds a user to the maintainance systems
    '''
        maintainance.users[self.name.strip()] = (self.tag, self.email)

    @classmethod
    def remove(cls, name):
        '''
        (None) -> None
        removes a user from the maintainance systems
        '''

        if name in maintainance.users:
            del maintainance.users[name]
            print("you are now logged out")
    @classmethod
    def pr_user(cls):
        '''
        (None) -> None
        displays the users using the maintainance systems
        '''
        if len(maintainance.users) >= 1:
            for keys in maintainance.users:
                print(("maintainance systems users {}:{}").format(keys(), maintainance.users[keys]))


welcome_message("Hello!!! welcome", "")
i = 0
shutdown = True
while shutdown:
    question = input("what do you want to do toaday?\n (1) for login, (2) for logout, (3) to see current users and (4) to shutdown\n")
    if question == "1":
        name = input("Please what is your name? : ")
        email = input("what is your email? : ")
        tag = input("what is your tag? : ")
        position = input("what system would you like to use?\n (a) for admin, (m) for maintainance, (w) for worker: ")

        if position.lower().strip() == "a":
            person = admin(name, email, tag, position)
            person.add()
        elif position.lower().strip() == "m":
            person = maintainance(name, email, tag, position)
            person.add()
        elif position.lower().strip() == "w":
            person = maintainance(name, email, tag, position)
            person.add()
    elif question == "2":
        name = input("please provide your name")
        admin.remove(name)
        maintainance.remove(name)
        worker.remove(name)
    elif question == "3":
        maintainance.pr_user()
        admin.pr_user()
        worker.pr_user()
    elif question == "4":
        welcome_message("Goodbye", "")
        shutdown = False
    else:
        print("Invalid option, please try again")

    i = i + 1
