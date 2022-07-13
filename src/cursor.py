class Cursors:
    """
    The cursor class provides access to the position cursor information. It can calculate the difference in membrane
    potential (Vm) between two cursors.
    """
    def __init__(self, y_data, time):
        """
        Create a cursor object.

        :param y_data: the current y_axis data being analysed
        :param time: the x position (time) of the cursor in milliseconds
        """
        self.y_data = y_data
        self.time = time

    def get_vm(self):
        print(self.y_data[self.time])


# class CursorA(Cursors):


class CursorB(Cursors):
    def get_diff_time(self, cursor_a):
        print(self.time - cursor_a.time)

    def get_min(self, cursor_a):
        print(min(self.y_data[cursor_a.time: self.time]))
