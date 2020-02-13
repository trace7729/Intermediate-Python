from Fraction import *
from decimal import *
from itertools import count, takewhile
from functools import reduce

# Python II - Lab 4 - Annie Yen

pi50 = Decimal("3.14159265358979323846264338327950288419716939937510")
iterations = 10000000


# Part1
class LeibnizPiIterator:
    '''
    calculates the Leibniz series
    '''
    def __init__(self):
        '''
        Initializer/constructor for LeibnizPiIterator
        '''
        pass

    def __iter__(self):
        '''
        Initializes the values for iterator
        Args:
            self: The Object
        Returns:
            self: Initialized fraction, n, and add_next
        '''
        self.fraction = Fraction(0, 1)
        self.n = 1
        self.add_next = True
        return self

    def __next__(self):
        '''
        Returns the result of Leibniz iterations
        Args:
            self: The Object, fraction
        Returns:
            self.fraction.value: The fraction after calculation
        '''
        if self.add_next:
            self.fraction += Fraction(4, self.n)
        else:
            self.fraction -= Fraction(4, self.n)
        self.add_next = not self.add_next
        self.n += 2
        return self.fraction.value


# Part 2
def NilakanthaPiGenerator():
    '''
    Yield as a generator that calculates the Nilakantha Series
    Args: None
    Yields:
        fraction.value: fraction at the break of iteration
    '''
    fraction = Fraction(3, 1)
    num = 2
    add_next = True
    while 1:
        operand = Fraction(4, (num*(num+1)*(num+2)))
        if add_next:
            fraction += operand
        else:
            fraction -= operand
        add_next = not add_next
        num += 2
        yield fraction.value


# Part 3
def compose(*functions):
    '''
    Form a single function call
    Args:
        *functions
    Returns:
        reduce(): functions reduced to a single call
    '''
    return reduce(lambda f, g: lambda x: g(f(x)), functions)


def milesToYards(value):
    '''
    Convert miles to yards
    Args:
        value: float or integer of miles
    Returns:
        value: float or integer of yards
    '''
    return value*1760


def yardsToMiles(value):
    '''
    Convert miles to yards
    Args:
        value: float or integer of yards
    Returns:
        value: float or integer of miles
    '''
    return value*(1/1760)


def yardsToFeet(value):
    '''
    Convert yards to feet
    Args:
        value: float or integer of yards
    Returns:
        value: float or integer of feet
    '''
    return value*3


def feetToYards(value):
    '''
    Convert feet to yards
    Args:
        value: float or integer of feet
    Returns:
        value: float or integer of yards
    '''
    return value*(1/3)


def feetToInches(value):
    '''
    Convert feet to inches
    Args:
        value: float or integer of feet
    Returns:
        value: float or integer of inches
    '''
    return value*12


def inchesToFeet(value):
    '''
    Convert inches to feet
    Args:
        value: float or integer of inches
    Returns:
        value: float or integer of feet
    '''
    return value*(1/12)


def inchesToCm(value):
    '''
    Convert inches to centimeters
    Args:
        value: float or integer of inches
    Returns:
        value: float or integer of centimeters
    '''
    return value*2.54


def cmToInches(value):
    '''
    Convert centimeters to inches
    Args:
        value: float or integer of centimeters
    Returns:
        value: float or integer of inches
    '''
    return value*(1/2.54)


def metersToCm(value):
    '''
    Convert meters to centimeters
    Args:
        value: float or integer of meters
    Returns:
        value: float or integer of centimeters
    '''
    return value*100


def cmToMeters(value):
    '''
    Convert centimeters to meters
    Args:
        value: float or integer of centimeters
    Returns:
        value: float or integer of meters
    '''
    return value*(1/100)


def kmToMeters(value):
    '''
    Convert kilometers to meters
    Args:
        value: float or integer of kilometers
    Returns:
        value: float or integer of meters
    '''
    return value*1000


def metersToKm(value):
    '''
    Convert meters to kilometers
    Args:
        value: float or integer of meters
    Returns:
        value: float or integer of kilometers
    '''
    return value*(1/1000)


def auToKm(value):
    '''
    Convert astronomical units to kilometers
    Args:
        value: float or integer of astronomical units
    Returns:
        value: float or integer of kilometers
    '''
    return value*149597870.700


def kmToAu(value):
    '''
    Convert kilometers to astronomical units
    Args:
        value: float or integer of kilometers
    Returns:
        value: float or integer of astronomical units
    '''
    return value*(1/149597870.700)


def LyToau(value):
    '''
    Convert light years to astronomical units
    Args:
        value: float or integer of light years
    Returns:
        value: float or integer of astronomical units
    '''
    return value*63241.0770842662802685358


def auToLy(value):
    '''
    Convert astronomical units to light years
    Args:
        value: float or integer of astronomical units
    Returns:
        value: float or integer of light years
    '''
    return value*(1/63241.0770842662802685358)


def cmToMm(value):
    '''
    Convert centimeters to millimeters
    Args:
        value: float or integer of centimeters
    Returns:
        value: float or integer of millimeters
    '''
    return value*10


def mmToCm(value):
    '''
    Convert millimeters to centimeters
    Args:
        value: float or integer of millimeters
    Returns:
        value: float or integer of centimeters
    '''
    return value*(1/10)


def mmToMicro(value):
    '''
    Convert millimeters to micrometers
    Args:
        value: float or integer of millimeters
    Returns:
        value: float or integer of micrometers
    '''
    return value*1000


def microToMm(value):
    '''
    Convert micrometers to millimeters
    Args:
        value: float or integer of micrometers
    Returns:
        value: float or integer of millimeters
    '''
    return value*(1/1000)


def microToAng(value):
    '''
    Convert micrometers to Angstrom
    Args:
        value: float or integer of micrometers
    Returns:
        value: float or integer of Angstrom
    '''
    return value*10000


def angToMicro(value):
    '''
    Convert Angstrom to micrometers
    Args:
        value: float or integer of Angstrom
    Returns:
        value: float or integer of micrometers
    '''
    return value*(1/10000)


def start_my_program():
    # Part 1
    try:
        c1 = count()
        result1 = list(
            takewhile(
                lambda x: next(c1) < round(iterations/100),
                (i for i in LeibnizPiIterator())
            )
        )
        print(f"pi after {round(iterations/100)} iterations: {result1[-1]:.50f}")
        print("Difference: "+"{:.50f}".format(abs(result1[-1]-pi50)))
        c2 = count()
        result2 = list(
            takewhile(
                lambda x: next(c2) < iterations,
                (i for i in LeibnizPiIterator())
            )
        )
        print(f"pi after {iterations} iterations: {result2[-1]:.50f}")
        print("Difference: "+"{:.50f}\n".format(abs(result2[-1]-pi50)))
    except Exception as err:
        print("Error: " + str(err))

    # Part 2
    try:
        c3 = count()
        result3 = list(
            takewhile(
                lambda x: next(c3) < round(iterations/100),
                (i for i in NilakanthaPiGenerator())
            )
        )
        print(f"pi after {round(iterations/100)} iterations: {result3[-1]:.50f}")
        print("Difference: "+"{:.50f}".format(abs(result3[-1]-pi50)))
        c4 = count()
        result4 = list(
            takewhile(
                lambda x: next(c4) < iterations,
                (i for i in NilakanthaPiGenerator())
            )
        )
        print(f"pi after {iterations} iterations: {result4[-1]:.50f}")
        print("Difference: "+"{:.50f}\n".format(abs(result4[-1]-pi50)))
    except Exception as err:
        print("Error: " + str(err))

    # Part 3
    try:
        milesToInches = compose(milesToYards, yardsToFeet, feetToInches)
        print(f"Convert 2 miles to inches: {milesToInches(2):>38} in")
        feetToMeters = compose(feetToInches, inchesToCm, cmToMeters)
        print(f"Convert 5 feet to meters: {feetToMeters(5):>40,.3f} m")
        metersToInches = compose(metersToCm, cmToInches)
        print(f"Convert 1 meter to inches: {metersToInches(1):>38,.12f} in")
        milesToKm = compose(milesToYards, yardsToFeet, feetToMeters, metersToKm)
        print(f"Convert 10 miles to kilometers: {milesToKm(10):>33,.5f} km")
        kmToMiles = compose(kmToMeters, metersToInches, inchesToFeet, feetToYards, yardsToMiles)
        print(f"Convert 1 kilometers to miles: {kmToMiles(1):>33,.16f} mil")
        kmToInches = compose(kmToMeters, metersToInches)
        print(f"Convert 12.7 kilometers to inches: {kmToInches(12.7):>30,.1f} in")
        inchesToKm = compose(inchesToCm, cmToMeters, metersToKm)
        print(f"Convert 500000 inches to kilometers: {inchesToKm(500000):>28,.1f} km")
        metersToLy = compose(metersToKm, kmToAu, auToLy)
        print(f"Convert 9,460,730,472,580,800 meters to light years: {metersToLy(9460730472580800):>12,.0f} ly\n")
        microToCm = compose(microToMm, mmToCm)
        print(f"Convert 100,000 micrometers to centimeters: {microToCm(100000):21} cm")
        cmToAng = compose(cmToMm, mmToMicro, microToAng)
        print(f"Convert 10 centimeters to Angstrom: {cmToAng(10):>23} Angstrom")
        angToCm = compose(angToMicro, microToMm, mmToCm, cmToMeters)
        print(f"Convert 1,000,000,000 Angstrom to meters: {angToCm(1000000000):>24} m")
    except Exception as err:
        print("Error: "+str(err))


if __name__ == "__main__":
    start_my_program()
