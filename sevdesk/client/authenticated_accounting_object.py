from functools import wraps

from sevdesk.client import AuthenticatedClient


class AuthenticatedAccountingObject:

    """
    The client attribute should be set in the child class.
    """

    _client: AuthenticatedClient = NotImplemented

    def __init__(self):

        super().__init__()
        assert self._client is not NotImplemented, f"Client is not set in {self.__class__.__name__}"

    def __getattribute__(self, item):
        attr_ = super().__getattribute__(item)

        if callable(attr_):
            # assert client is not given in kwargs
            @wraps(attr_)
            def wrapper(*args, **kwargs):
                client = kwargs.get("client")
                assert client is None, f"Do not pass client in methods when using {self.__class__.__name__}"
                return attr_(*args, **kwargs)

            return wrapper
        return attr_
