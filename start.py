class User():
    import models.room
    room = models.room.Room(1)
    exit()
    name = 'Little Red Riding Hood'

    def whoAmI(self):
        return print('You are ' + self.name)

    # this is the main loop for letting the user do anything in our story
    # It is recursive, by definition: it is a function that calls itself

    # We first declare the function
    def whatDo(self):
        # ask for user input
        do = input('What do you want to do?\n')

        # elaborate that input

        # Tokenizer time!
        # This is a matter of UI.
        # Let's imagine that the user it's writing a command in natural language,
        # something like: "Look at the basket"

        # For simplicity's sake, let's ask the user to write always the verb at
        # the beginning of the command (it was commonplace in old text adventures)

        # But what about all the other words in the sentence? And how could the 
        # software be able to recognize the words, and what we mean?

        # We should break the sentence down in simple words and pass it to a nice
        # function that elaborates them for us! Let's go

        # First, as we know we will not use any punctuation mark into our commands,
        # we strip all of them away from our string, so that "look at basket." and
        # "look at basket" mean the same thing

        # we import the built in string object, that helps us manage strings in python
        import string
        # punctuation it's a property inside the string class that lists all the 
        # punctuation marks in python. It is a useful built in that helps us in not
        # writing all the punctuation marks by ourselves.
        do = do.translate(str.maketrans('','',string.punctuation))

        # We also make all the string lowercase, so that "LooK" and "look" are treated as equal
        do = do.lower()

        # Second, we split the user's phrase into a List of words, eliminating any whitespace
        do = do.split()

        # Third, we convert the List in a Tuple!
        # Why so? It's because the items in a list can be ordered as we like,
        # while tuple's items cannot. This is actually a feature we want, so that 
        # we can be sure that our variable holds something very similar to our user's input
        # This way, for example, we can be sure that do[0] is always our verb, and that
        # "use water on fire" is assured to be different than "use fire on water"
        # even though they hold the same elements (but their indexes are different!)
        do = tuple(do)


        # we use this library to check on existing modules and importing them when possibile
        import importlib
        # we compose the path that brings us to the module that we want to use. Look at the filesystem!
        # TODO: I should write some words on how path are written 
        # (absolute and relative, moving through directories and selecting files)

        #getting the module
        interaction = 'controllers.interactions.' + do[0]
        cont_loader = importlib.util.find_spec(interaction)
        if cont_loader is not None:
            interaction = importlib.import_module(interaction)

            # checking the class in the module. we should only write one class
            # per module, so that we can alway get one from [0][0]
            # built in module inspector
            import inspect
            # inspecting all classes inside a module
            of_class = inspect.getmembers(interaction, inspect.isclass)
            # we get the class name from the first class
            class_name = of_class[0][0]
            # we check if there's a class with the name we just got
            the_class = getattr(interaction,class_name)
            # we instantiate the object of class with the data input from user
            the_class(do)
            exit()
        else:
            print('Sorry, I didn\'t understand')

        # and then start over again!
        return self.whatDo()

        # usually, recursive functions have a bottom case that allow us to exit the function
        # in this case we want this loop to be infinite, so that we can always
        # explicitly ask user for input, and elaborate it.
        # We can add an "exit game" command that closes everything. it would be a sort of
        # bottom case

        # example of recursive function:
        # add numbers until you reach 20

        # def toHundred(number):
        #     if number == 20:
        #         return print(number)
        #     else:
        #         print(number)
        #         number = number + 1
        #         return toHundred(number)
        # 
        # toHundred(5)    

    # Remember, after you declare a function you should use it,
    # unless it will not take effect!

me = User()
me.whoAmI()
me.whatDo()