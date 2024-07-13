#!/usr/bin/python3
class MyList(list):
    """
    A custom list class that inherits from the built-in list type.
    Provides additional functionality for sorting and printing the list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """
        sorted_list = sorted(self)
        print(sorted_list)

# Example usage
if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)

    print(my_list)  # [1, 4, 2, 3, 5]
    my_list.print_sorted()  # [1, 2, 3, 4, 5]
    print(my_list)  # [1, 4, 2, 3, 5]
