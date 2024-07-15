from functools import wraps

from sevdesk.client import AuthenticatedClient


class AuthenticatedAccountingObject:

    """
    The client attribute should be set in the child class.
    """

    _client: AuthenticatedClient = NotImplemented

    def __init__(self):

        super().__init__()

        if self._client is NotImplemented:
            raise NotImplementedError(
                f"Please set the _client attribute in {self.__class__.__name__}"
            )

    def __getattribute__(self, item):
        attr_ = super().__getattribute__(item)

        if callable(attr_):
            # assert client is not given in kwargs
            @wraps(attr_)
            def wrapper(*args, **kwargs):
                client = kwargs.get("client")

                if client is not None:
                    raise ValueError(
                        f"Do not pass client in {self.__class__.__name__} methods. Must be implemented in the class."
                    )
                return attr_(*args, **kwargs)
            return wrapper
        return attr_
