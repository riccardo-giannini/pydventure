# TODO: this should be a METACLASS producing the concrete classes ocnsisting of 
# actions, like go, look, take, talk, use
class Interaction():
    def __init__(self, command:tuple, room:object):
        for cmd in command:
            # get first cmd as command: look talk use etc.
            # what to use
            # call look talk etc. for peculiar methods, like look: look around
            if (cmd in room.content):
                import importlib
                looking_at = importlib.import_module('models.onscene.' + cmd)
                print(looking_at.look)
        pass

    command = tuple