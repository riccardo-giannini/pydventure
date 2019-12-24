class Look:
    # command: tuple. It's a case of typing the parameter of a function.
    # This way we know that command should always be a tuple, if not, it should return an error.
    def __init__(self, command:tuple):
        self.command = command

        # TODO
        # for itm in command:
        #     import models.room
        #     room = Room()
        

        # What room are we in?
        # Foreach member in tuple:
        # Does an object in the room have a name equal to a member of tuple?
        #   yes: describe it
        #   no: return error (Nothing to look at here)
        # case: look around? how to manage it? better an attribute in class,
        # or something in database? check it

    command = tuple