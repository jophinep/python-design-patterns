"""
Decorator Patterns
"""

def decorate_non_cls_methods(decorator):
    """
    Class level decorator which decorated all methods in a class except the followings:
        - magic methods (dunders) E.g. __init__(), __some_method__()
        - classmethods
    When there is a need to decorate class methods, that can be done explicitly

    Example:
    ```python
    @decorate_non_cls_methods(monitor)
    class SampleClass:

        # prometheus decorator will not be applied on dunders
        def __init__(self):
            pass

        # Will be decorated
        def instance_method(self):
            pass

        # prometheus decorator will not be applied
        @classmethod
        def class_method1(cls):
            pass

        # prometheus decorator will not be applied but we have added it explicitly
        @classmethod
        @prometheus
        def class_method2(cls):
            pass

        # Will be decorated
        @staticmethod
        def static_method():
            pass

    ```
    """
    def wrapper(cls):
        """
        Wrapper method for class decorator
        """
        for attr in cls.__dict__:
            method = getattr(cls, attr)
            method_obj = cls.__dict__.get(attr)
            # Conditions
            dunder_condition = attr.startswith("__") and attr.endswith("__")
            classmethod_condition = isinstance(method_obj, classmethod)
            empty_obj_condition = not method_obj
            if any((dunder_condition, classmethod_condition, empty_obj_condition)):
                continue
            if callable(method):
                if isinstance(method_obj, staticmethod):
                    decorated = type(method_obj)(decorator(method))
                else:
                    decorated = decorator(method)
                setattr(cls, attr, decorated)
        return cls
    return wrapper
