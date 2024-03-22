from .._compat import properties
from ..backend import KeyringBackend


class Keyring(KeyringBackend):
    """
    Keyring that return None on every operation.

    >>> kr = Keyring()
    >>> kr.get_password('svc', 'user')
    """

    @properties.classproperty
    def priority(cls) -> float:
        return -1

    def get_password(self, service, username, password=None):
        pass

    set_password = delete_password = get_password  # type: ignore
