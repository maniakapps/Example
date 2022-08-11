class ListGenerator:
    def __init__(self, file_name):
        with open(file_name) as self.file:
            self.__data = self.file.read().strip().split()

    def get_data(self) -> list[str]:
        """
        Returns the file content
        :return: self.__data file content
        """
        return self.__data

    def get_size(self) -> int:
        """
        Computes the list size
        :return: integer with the size of the list
        """
        return len(self.__data)
