""""
# Problem Statement

Let's write some code to track driving history for people.

The code will process an input file. You can either choose to accept the input via stdin (e.g. if you're using Ruby `cat input.txt | ruby yourcode.rb`), or as a file name given on the command line (e.g. `ruby yourcode.rb input.txt`). You can use any programming language that you want. Please choose a language that allows you to best demonstrate your programming ability.

Each line in the input file will start with a command. There are two possible commands.

The first command is Driver, which will register a new Driver in the app. Example:

Driver Dan

The second command is Trip, which will record a trip attributed to a driver. The line will be space delimited with the following fields: the command (Trip), driver name, start time, stop time, miles driven. Times will be given in the format of hours:minutes. We'll use a 24-hour clock and will assume that drivers never drive past midnight (the start time will always be before the end time). Example:

Trip Dan 07:15 07:45 17.3

Discard any trips that average a speed of less than 5 mph or greater than 100 mph.

Generate a report containing each driver with total miles driven and average speed. Sort the output by most miles driven to least. Round miles and miles per hour to the nearest integer.

Example input:


Driver Dan
Driver Lauren
Driver Kumi
Trip Dan 07:15 07:45 17.3
Trip Dan 06:12 06:32 21.8
Trip Lauren 12:01 13:16 42.0


Expected output:


Lauren: 42 miles @ 34 mph
Dan: 39 miles @ 47 mph
Kumi: 0 miles
"""
import csv
import sys

class Driver:
    def __init__(self, name):
        self.name = name
        self.trips = []
    def add_trip(self, trip):
        self.trips.append(trip)
    def __str__(self):
        return self.name
    def report(self):
        return 0,0


class Trip:
    #def __init__(self, start_time, end_time, dist):
        #self.start_time = start_time
        #self.end_time = end_time
        #self.dist = dist
    def __init__(self, diff_time, dist):
        self.diff_time = diff_time
        self.dist = dist
    def __str__(self):
        return self
    def __repr__(self):
            if 5 < (self.dist / self.diff_time) < 100:
                return f'< Trip: {self.dist} miles, {self.dist/self.diff_time} mph>'



def get_time_difference(start_time, end_time):
    """
    """
    s_hour, s_min = start_time.split(':')
    e_hour, e_min = end_time.split(':')
    s_time = int(s_hour) + int(s_min) / 60
    e_time = int(e_hour) + int(e_min) / 60
    time_diff = (e_time - s_time)
    return time_diff


def main(lines):
    """
    >>> main([])
    []
    >>> main([''])
    []
    >>> main(['foo', 'bar'])
    []
    >>> main(['Driver Kumi'])
    ['Kumi: 0 miles']
    >>> main(['Driver Ivan Vladimirovich'])
    ['Ivan Vladimirovich: 0 miles']
    >>> main(['Driverless'])
    []
    >>> main(['Driver Lauren', 'Trip Lauren 12:01 13:16 42.0'])
    ['Lauren: 42 miles @ 34 mph']
    >>> main(['Driver Nik', 'Trip Kumi 12:01 13:16 32.0'])
    ['Nik: 0 miles', Kumi: 42 miles @ 34 mph']
    """
    if not lines:
        return []

    driver_by_name = {}
    print(lines)
    for l in lines:
        print(l)
        if l.startswith('Driver '):
            _, name = l.split(' ', 1)
            name = name.strip('\n')
            driver = Driver(name)
            driver_by_name[name] = driver
        if l.startswith('Trip '):
            _, name, s_time, e_time, dist  = l.split(' ')
            if name not in driver_by_name:
                continue
            dist = float(dist)
            time_diff = get_time_difference(s_time, e_time)
            trip = Trip(time_diff, dist)
            driver = driver_by_name[name]
            driver.add_trip(trip)
            print(trip)
        return driver.report()

    for name in distance_by_driver.keys():
        parameters = []
        parameter_by_name[name] = parameters
        dist = distance_by_driver[name]
        time = time_by_driver[name]
        if dist != 0 and time != 0:
            speed = round(dist / time)
            dist = round(dist)
            if 5 < speed < 100:
                parameters.append(dist)
                parameters.append(speed)
                result.append("{}: {} miles, {} mph".format(name, dist, speed))
        else:
            result.append("{}: {} miles".format(name, dist))
    for name in driver_by_name:
        driver = driver_by_name[name]
        print(driver[0])



#print(main(open('trips.csv')))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Specify a filename to read!")
        sys.exit(1)

    filename = sys.argv[1]
    with open(filename) as fo:
        result = main(fo.readlines())
        print("\n".join(result))
