# Use dict. When inserting, if already present, delete it and add it again. If cache full, delete first element of dict and add new val.

class LRUCache:
    def __init__(self, capacity: int):
        self.d = dict()
        self.c = capacity

    def get(self, key: int) -> int:
        val = self.d.get(key, -1)
        if val==-1:
            pass
        else:
            del self.d[key]
            self.d[key] = val
        return val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            del self.d[key]
            
        else:
            if len(self.d.keys())==self.c:
                for oldest in self.d.keys():
                    del self.d[oldest]
                    break
        self.d[key] = value