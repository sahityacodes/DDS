import random
import datetime


class Customer:
    def __init__(self, arrival_time, service_start_time, service_time):
        self.arrival_time = arrival_time
        self.service_start_time = service_start_time
        self.service_time = service_time
        self.service_end_date = self.service_start_time+self.service_time
        self.wait = self.service_start_time-self.arrival_time


def generateOrderTime(lambd):
    return random.expovariate(lambd)


def Simulation(lambd=False, mu=False, simulation_time=False):
    if not lambd:
        lambd = input('Inter arrival rate: ')
    if not mu:
        mu = input('Service rate: ')
    if not simulation_time:
        simulation_time = input('Total simulation time: ')
    t = 0
    Customers = []
    while t < simulation_time:
        if len(Customers) == 0:
            arrival_time = generateOrderTime(lambd)
            service_start_time = arrival_time
        else:
            arrival_time += generateOrderTime(lambd)
            service_start_time = max(
                arrival_time, Customers[-1].service_end_date)
        service_time = generateOrderTime(mu)
        Customers.append(Customer(arrival_time, service_start_time, service_time))
        print("Customer Number", len(Customers))
        print("Customer Wait Time {} ".format(service_start_time-arrival_time))
        print("Customer Arrived At : {}".format(service_start_time))
        print("Service Time : {} ".format(service_time))
        print("")
        t = arrival_time
    return Customers
