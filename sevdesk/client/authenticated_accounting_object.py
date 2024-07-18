from sevdesk.client import AuthenticatedClient


class AuthenticatedAccountingObject:

    """
    The client attribute should be set in the child class.
    """

    _client: AuthenticatedClient = NotImplemented

    @classmethod
    def _get_client(cls) -> AuthenticatedClient:
        if cls._client is NotImplemented:
            raise NotImplementedError(
                f"Please set the _client attribute in {cls.__name__}"
            )
        return cls._client
