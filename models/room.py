# This class is a model that istantiates a room based on its id
# You instantiate the object, put the id in, and the init will parse the modules
# looking for a room with that id.
# An SQL DB would rather be much more efficient. I should implement that.

# TODO: instantiate this class with data provided by SQL.
class Room():
    def __init__(self, id:int):
        import os
        roomspath = os.path.dirname(os.path.realpath(__file__)) + '/rooms'
        rooms = os.listdir(roomspath)

        for r in rooms:
            if r.endswith('.py'):
                r = os.path.splitext(r)[0]
            else:
                continue
            import importlib
            room = importlib.import_module('models.rooms.' + r)
            if id == room.id:
                self.name = room.name
                self.content = room.content
                self.look_around = room.look_around
            else:
                # TODO: print error
                pass
            pass
        pass

        # TODO: same thing as with rooms, but with content

    # Each room is identified by a number, so it's easier to refer to it
    id = int
    # Each room has a name too, so that is human-readable. Easier to identify
    name = str
    # The content set contains everything that's inside a room.
    # It's a set, so that it's unordered, like a list, but it cannot hold mulitple
    # copies of the same entity
    content = {}

    look_around = str