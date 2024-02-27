from collections.abc import MutableMapping
# MutableMapping is the one that we want to let us
# make something like a dict

class HashTable(MutableMapping):
    def __hash(self, key):
        # take a key - anything that works
            # as a dictionary key
        # return an integer in range(0, self.__bins)

        # lets say self.__hash("apple") -> 5
        # we would put the key "apple" and its value
        # in bin #5
        return key % self.__n_bins
    
    def __init__(self):
        self.__n_bins = 2
        self.__keys = [None] * self.__n_bins
        self.__values = [None] * self.__n_bins
        self.__size = 0

    def __getitem__(self, key):
        bindex = self.__hash(key)
        print(f"get {key} from {bindex}/{self.__n_bins}")
        if self.__keys[bindex] == key:
            return self.__values[bindex]
        else:
            index = bindex + 1
            while index != bindex:
                if self.__keys[index] == key:
                    return self.__values[index]
                elif self.__keys[index] is None:
                    raise KeyError()
                index += 1

    def __grow(self):
        self.__n_bins = self.__n_bins * 2
        print(f"grow to {self.__n_bins}")
        old_keys = self.__keys
        old_values = self.__values
        self.__keys = [None] * self.__n_bins
        self.__values = [None] * self.__n_bins
        for index in range(0, len(old_keys)):
            key = old_keys[index]
            if key is not None:
                self[key] = old_values[index]
                        
    def __setitem__(self, key, value):
        assert key is not None
        if self.__size >= 0.6 * self.__n_bins:
            self.__grow()

        bindex = self.__hash(key)
        if self.__keys[bindex] == key:
            # we already have it
            self.__values[bindex] = value
        elif self.__keys[bindex] is None:
            # new
            print(f"Perfect: {key} in {bindex}/{self.__n_bins}")
            self.__keys[bindex] = key
            self.__values[bindex] = value
            self.__size += 1
        else:
            index = bindex + 1
            while index != bindex:
                if self.__keys[index] == key:
                    # we already have it
                    self.__values[index] = value
                    return
                elif self.__keys[index] is None:
                    # new
                    print(f"Collision: {key} in {index} instead of {bindex}")
                    self.__keys[index] = key
                    self.__values[index] = value
                    self.__size += 1
                    return
                index = (index + 1) % self.__n_bins
            raise RuntimeError("This shouldn't happen!")
                    
    def __delitem__(self, key):
        bindex = self.__hash(key)
        if self.__keys[bindex] == key:
            self.__values[bindex] = None
            self.__keys[bindex] = None
            self.__size -= 1
        else:
            index = bindex + 1
            while index != bindex:
                if self.__keys[index] == key:
                    self.__values[index] = None
                    self.__keys[index] = None
                    self.__size -= 1
                elif self.__keys[index] is None:
                    raise KeyError()
                index += 1

    def __iter__(self):
        all_keys = list()
        for key in self.__keys:
            if key is not None:
                all_keys.append(key)
        return iter(all_keys)

    def __len__(self):
        return self.__size

            
ht = HashTable()
ht[11] = "a"
ht[22] = "b"
ht[33] = "c"
ht[44] = "d"
ht[55] = "e"
ht[66] = "f"
ht[77] = "g"
ht[88] = "h"
assert ht[11] == "a"
assert ht[22] == "b"
assert ht[33] == "c"
assert ht[44] == "d"
assert ht[55] == "e"
assert ht[66] == "f"
assert ht[77] == "g"
assert ht[88] == "h"
ht[64] = "i"
ht[128] = "j"
ht[256] = "k"



