import collections


class StrKeyDict(collections.UserDict):
    '''
    UserDict는 self.data에 dict를 가지고 있습니다
    '''

    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key):
        return str(key) in self.data

    def __setitem__(self, key, item):
        self.data[str(key)] = item
