#!/usr/bin/python3
"""
Module BaseGeometry
"""
class BaseGeometry:
    """
    Class BaseGeometry extra data
    """
    def area(self):
        """
        Raises an Exception with the message 'area() is not implemented'.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value:
        - If value is not an integer, raises a TypeError with the message '<name> must be an integer'.
        - If value is less than or equal to 0, raises a ValueError with the message '<name> must be greater than 0'.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

# Example usage
if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        bg.integer_validator("my_int", 12)
        bg.integer_validator("width", 89)
        bg.integer_validator("name", "John")  # Raises TypeError
        bg.integer_validator("age", 0)  # Raises ValueError
        bg.integer_validator("distance", -4)  # Raises ValueError
    except Exception as e:
        print(f"[{e.__class__.__name__}] {e}")
