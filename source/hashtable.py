#!python
import time
from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8): # O(n) time/space
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)] # O(n) time/space

    def __str__(self): # O(n) time/space
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()] # O(n) time/space
        return '{' + ', '.join(items) + '}'

    def __repr__(self): # O(1) time/space
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items()) # O(1) time/space

    def __iter__(self): # O(1) time/space
        """Return the iterator object itself"""
        self.index = 0 # O(1) time/space
        self.node = self.buckets[self.index].head # O(1) time/space
        return self # O(1) time/space

    def __next__(self):
        """Return the next item in the sequence.
        On reaching the end, and in subsequent calls,
        it must raise StopIteration"""
        if self.node is not None:
            node = self.node
            # assign next node to self.node
            self.node = self.node.next
            return node.data
        else:
            self.index += 1
            if self.index > len(self.buckets)-1:
                raise StopIteration
            self.node = self.buckets[self.index].head
            return self.__next__()

    def _bucket_index(self, key): # O(1) time/O(1) space
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets) # O(1) time/O(1) space

    def keys(self): # O(n) time/O(n) space　n: number of entries
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = [] # O(1) time/space

        # for bucket in self.buckets: # O(b) time for b
        #     for key, value in bucket.items(): # O(l) time for l items in list
        #         all_keys.append(key) # O(1) time/space

        for key, value in self:
            all_keys.append(key)
        return all_keys

    def values(self): # O(n) time/O(n) space
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        all_values = [] # O(1) time/space

        # for bucket in self.buckets: # O(b) time
        #     for key, value in bucket.items(): # O(l) time
        #         all_values.append(value) # O(1) time/space

        for key, value in self:
            all_values.append(value)
        return all_values

    def items(self): # O(n) time/space
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = [] # O(1) time/space
        for bucket in self.buckets: # O(b) time
            all_items.extend(bucket.items()) # O(l) time/O(1) space
        return all_items # O(1) time/O(n) space

    def length(self): # O(n) time/O(n) space
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket

        # counter = 0
        # for bucket in self.buckets:
        #     for _ in bucket.items():
        #         counter += 1
        # return counter

        all_items = self.items() # O(n) time/space
        return len(all_items) # O(1) time/space

    def contains(self, key): # O(n) time/space
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        all_keys = self.keys() # O(n) time/space
        return key in all_keys: # O(1) time/space

    def get(self, key): # O(l) time/O(1) space
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))

        index = self._bucket_index(key)
        for bucket_key, bucket_value in self.buckets[index].items(): # best case running time: O(1), worst case running time: O(l)
            if bucket_key == key:
                return bucket_value # O(1) time/O(1) space

        # for bucket_key, bucket_value in self:
        #     if bucket_key == key:
        #         return bucket_value # O(1) time/O(1) space

        raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):# O(l) time/O(1) space
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        if self.contains(key):
            for bucket_key, bucket_value in bucket.items(): # best case running time: O(1), worst case running time: O(l)
                if bucket_key == key:
                    bucket.replace((bucket_key, bucket_value), (key, value)) # O(n) time/O(1) space
                    break

            # for bucket_key, bucket_value in self: # best case running time: O(1), worst case running time: O(n)
            #     if bucket_key == key:
            #         bucket.replace((bucket_key, bucket_value), (key, value)) # O(n) time/O(1) space
            #         break

        else:
            bucket.append((key, value)) # O(1) time/space

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        if self.contains(key):
            for bucket_key, bucket_value in bucket.items(): # best case running time: O(1), worst case running time: O(l)
                if bucket_key == key:
                    bucket.delete((bucket_key, bucket_value)) # O(1) time/space
                    break

            # for bucket_key, bucket_value in self: # best case running time: O(1), worst case running time: O(n)
            #     if bucket_key == key:
            #         bucket.delete((bucket_key, bucket_value)) # O(1) time/space
            #         break

        else:
            raise KeyError('Key not found: {}'.format(key))

    # def clear(self):
    #     """Remove all items from the Buckets"""
    #     for bucket in self.buckets:



def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    start_set_time = time.time()
    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))
    end_set_time = time.time()
    elapsed_time = end_set_time - start_set_time
    print("elapsed time to set 3 items: {}".format(float(elapsed_time)))

    print('\nTesting get:')
    start_get_time = time.time()
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))
    end_get_time = time.time()
    elapsed_time = end_get_time - start_get_time
    print("elapsed time to get 3 items: {}".format(float(elapsed_time)))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    for key, value in ht:
        print (key, value)

    # Enable this after implementing delete method
    delete_implemented = True
    if delete_implemented:
        print('\nTesting delete:')
        start_delete_time = time.time()
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))
        end_delete_time = time.time()
        elapsed_time = end_delete_time - start_delete_time
        print("elapsed time to delte 3 items: {}".format(float(elapsed_time)))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))

if __name__ == '__main__':
    test_hash_table()
