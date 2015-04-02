
# Collections en itereren {{{
import itertools # {{{

count = itertools.count
cycle = itertools.cycle

takewhile = itertools.takewhile
dropwhile = itertools.dropwhile
compress = itertools.compress
filterfalse = itertools.filterfalse
islice = itertools.islice

def how_not_to_list_evens():
    small = lambda x: x < 10
    print(list(takewhile(small, compress(count(), cycle([True,
        False])))))
    print(list(islice(count(), 0, 10, 2)))

repeat = itertools.repeat
accumulate = itertools.accumulate

def my_count(n):
    return accumulate(repeat(1, n))

itertools.chain
from_iterable = itertools.chain.from_iterable
tee = itertools.tee

def counted_cycle(seq, n):
    return from_iterable(tee(seq, n))

groupby = itertools.groupby

def odds_and_evens(seq):
    return groupby(seq, key=lambda x: x % 2)

itertools.starmap
zipl = itertools.zip_longest

def my_starmap(func, seq1, seq2):
    return map(lambda p: func(*p), zip(seq1, seq2))

itertools.product
itertools.permutations
itertools.combinations
itertools.combinations_with_replacement

def show_combinatorics():
    print(list(itertools.product("ABCD", repeat=2)))
    print(list(itertools.permutations("ABCD", 2)))
    print(list(itertools.combinations_with_replacement("ABCD", 2)))
    print(list(itertools.combinations("ABCD", 2)))

# }}}

import collections # {{{

collections.deque
collections.namedtuple
collections.OrderedDict
collections.defaultdict
collections.Counter

collections.UserDict
collections.UserList
collections.UserString

# }}}

import array # {{{
# }}}

import bisect # {{{
# }}}

import heapq # {{{
# }}}

# Bytes {{{
# }}}

# }}}

# Multiprocessing en threading {{{

import queue # {{{
queue.Queue
#queue.LIFOQueue
queue.PriorityQueue
# }}}

import threading # {{{
# Gebaseerd op het Java threading model
threading.Thread
threading.Lock
threading.Condition
threading.Semaphore
threading.BoundedSemaphore
threading.Timer
threading.Barrier
threading.Event
# Maar merk op dat GIL
# }}}

import multiprocessing # {{{
multiprocessing.Process
multiprocessing.Pipe
multiprocessing.Queue
multiprocessing.Pool
# ...
# }}}

import subprocess
# }}}

# Divers {{{

import pdb # {{{
# }}}

import functools # {{{
functools.partialmethod
functools.singledispatch
functools.update_wrapper
functools.wraps
# }}}

import asyncio # {{{
# }}}

import pickle # {{{


class Foo:
    x = 'blabla'

    def __init__(self, y):
        self.y = y


def how_to_pickle():
    print(pickle.dumps(True))
    print(pickle.dumps(5))
    print(pickle.dumps((None, [{'a': 1}])))
    print(pickle.dumps(Foo))
    print(pickle.dumps(Foo(42)))

    foo = Foo(42)
    with open('somefile', 'wb') as picklefile:
        pickle.dump(foo, picklefile)

    pickled_foo = pickle.dumps(foo)
    print(pickle.loads(pickled_foo))

    with open('somefile', 'rb') as picklefile:
        print(pickle.load(picklefile))

# }}}

import shelve
import pprint
import locale
import logging
import decimal
import requests
# }}}

# profiling
# C extensions en SWIG

# vim: foldmethod=marker
