#!/usr/bin/env python3

from collections import deque
from heapq import heappush, heappop
from random import expovariate

MAXT = 1000000
LAMBDA = 0.7

class Arrival:
    def __init__(self, id):
        self.id = id

    def process(self, state):
        self.arrival_time = arrival_time  # * save job arrival time in state.arrivals
        # * push the new job arrival in the event queue
        #   (the new event will happen at time t + expovariate(LAMBDA))
        # * if the server FIFO queue is empty, add this job termination
        #   (termination will happen at time t + expovariate(1))
        raise NotImplementedException
                     
class Completion:
    def process(self, state):
        # * remove the first job from the FIFO queue
        # * update its completion time in state.completions
        # * insert the termination event for the next job in queue
        raise NotImplementedException

class State:
    def __init__(self):
        self.t = 0  # current time in the simulation
        self.events = [(0, Arrival(0))]  # queue of events to simulate
        self.fifo = deque() # queue at the server
        self.arrivals = {}  # jobid -> arrival time mapping
        self.completions = {}  # jobid -> completion time mapping

state = State()
events = state.events

while events:
    t, event = heappop(events)
    if t > MAXT:
        break
    state.t = t
    event.process(state)

# process state.arrivals and state.completions, find average time spent
# in the system, and compare it with the theoretical value of 1 / (1 - LAMBDA)
