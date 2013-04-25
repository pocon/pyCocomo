import math

def cocomo(sloc, project_class='O', eaf=1):
    ''' COCOMO II analysis based on: http://en.wikipedia.org/wiki/COCOMO '''

    coefficients = {
        'O': {'a': 2.4,
              'b': 1.05,
              'c': 2.5,
              'd': 0.38,
              },
        'S': {'a': 3.0,
              'b': 1.12,
              'c': 2.5,
              'd': 0.35,
              },
        'E': {'a': 3.6,
              'b': 1.20,
              'c': 2.5,
              'd': 0.32,
              },
        }

    result = {'E': coefficients[project_class]['a'] * math.pow(sloc/1000.0, coefficients[project_class]['b']) * eaf}
    result['D'] = coefficients[project_class]['c'] * math.pow(result['E'], coefficients[project_class]['d'])
    result['P'] = result['E'] / result['D']

    return result
