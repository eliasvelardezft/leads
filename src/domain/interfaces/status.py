from abc import ABC


class IStatus(ABC):
    status: str

    def progress(self):
        raise NotImplementedError

    def complete(self):
        raise NotImplementedError

    def fail(self):
        raise NotImplementedError

    def drop(self):
        raise NotImplementedError
