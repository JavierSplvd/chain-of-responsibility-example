from abc import ABC, abstractmethod
import time
from request import Request

class Handler(ABC):
    @abstractmethod
    def process(self, data):
        pass
    @abstractmethod
    def internal_process(self, data):
        pass
    @abstractmethod
    def set_next(self, handler):
        pass
    

class AbstractHandler(Handler):
    handler_id: str = ""
    next_handler: Handler = None

    def process(self, data):
        print("Handler:" + self.handler_id)
        if self.next_handler is None:
            return self.internal_process(data)
        else:
            return self.next_handler.process(self.internal_process(data))
    
    @abstractmethod
    def internal_process(self, data):
        pass

    def set_next(self, handler):
        self.next_handler = handler

class CacheHandler(AbstractHandler):
    handler_id: str = "CacheHandler"
    cache_result = None

    def internal_process(self, data: str):
        if self.cache_result is None:
            return self.calculations(data)
        else:
            return self.cache_result

    def calculations(self, data):
        time.sleep(3)
        self.cache_result = "cache-" + data
        return data

class PrefixHandler(AbstractHandler):
    handler_id: str = "PrefixHandler"

    def internal_process(self, data):
        return "pre-" + data