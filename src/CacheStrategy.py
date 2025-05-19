from abc import ABC, abstractmethod
class CacheStrategy(ABC):
    @abstractmethod
    def get(key: str) -> dict[str, str]: ...

    @abstractmethod
    def put(key: str, response: dict): ...

    @abstractmethod
    def clear(): ...