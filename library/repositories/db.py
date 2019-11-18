from tinydb import TinyDB, Query, where
from tinydb.storages import JSONStorage
from tinydb.middlewares import CachingMiddleware
import os

class Db:
    
    def __init__(self):
        self.db = TinyDB('{}/db.json'.format(os.path.dirname(os.path.realpath(__file__))), storage=JSONStorage)        
        
    def get_table(self,table):
        return self.db.table(table, cache_size=0)