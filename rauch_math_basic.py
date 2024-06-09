# Basic calculation used in the basic math explanation

def sum (values):
    values_sum = 0

    for v in values:
        values_sum = values_sum + v
    
    return values_sum


def average (values):
    #getting the length of values, the number of items.
    number = values.__len__()
    return sum(values) / number


def deviations(values):
    avg = average(values)
    c_deviations = []
    
    #determining the difference between the item from the mean (deviation)
    for v in values:
        c_deviations.append(v - avg)

    return c_deviations


def sqr_deviations(values):
    c_deviations = deviations(values)
    sqr_deviations = []
    for d in c_deviations:
        sqr_deviations.append(d**2)

    return sqr_deviations


def sum_sqr_deviations(values):
    return sum(sqr_deviations(values))


def variance(values):
    number = values.__len__()
    return sum_sqr_deviations(values) / number


def variance_sample(values):
    number = values.__len__() - 1
    return sum_sqr_deviations(values) / number


def standard_deviation(values):
    return variance(values) ** 0.5


def standard_deviation_sample(values):
    return variance_sample(values) ** 0.5