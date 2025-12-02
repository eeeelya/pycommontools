class Singleton[T](type):
    """
    Metaclass that implements the Singleton pattern.

    Ensures that only one instance of a class exists throughout the application.
    When a class uses this metaclass, all calls to instantiate the class will
    return the same instance.

    Type Parameters:
        T: The type of the singleton instance.

    Attributes:
        _instances: Dictionary storing singleton instances keyed by class.

    Example:
        >>> class DatabaseConnection(metaclass=Singleton):
        ...     def __init__(self, host: str):
        ...         self.host = host
        ...
        >>> db1 = DatabaseConnection("localhost")
        >>> db2 = DatabaseConnection("localhost")
        >>> db1 is db2  # Both variables reference the same instance
        True

    Note:
        The singleton instance is created on first instantiation and cached.
        Subsequent instantiation attempts return the cached instance, ignoring
        any new arguments passed to __init__.
    """

    _instances: dict[object, T] = {}

    def __call__(cls, *args, **kwargs) -> T:
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)

        return cls._instances[cls]