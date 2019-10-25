from abc import ABC, abstractmethod
class Command(ABC):

    def __init__(self,name):
        self.name = name
    
    
    async def get_params(self, command):
        self.params = command.split(" ")[1:]
        return self.params
    
    async def execute(self,ctx,command):
        self.to_execute(ctx,self.get_params(command))
    
    @abstractmethod
    async def to_execute(self, ctx, params):
        pass