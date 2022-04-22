"""Module in which the file manager is written"""


class FileManager:
    def __init__(self, file_name, method):
        """Method accepts the name of the file and the mode of operation with this guy,
        if the mode of operation is not in the list, an error will occur"""
        if method not in ['w', 'r', 'a', 'b']:
            raise ValueError("Error mode")
        self.filename = file_name
        self.mode = method

    def __enter__(self):
        """File opening method"""
        print(f'Open file {self.filename}')
        self.__file = open(self.filename, self.mode)
        return self.__file

    def __exit__(self, type, value, traceback):
        """Method for closing a file"""
        print(f'Close file {self.filename}')
        if not self.__file.closed:
            self.__file.close()


with FileManager('asd.txt', 'w') as f:
    f.write('Hello World')

