"""This module provides a class for constructing a constraint
satisfaction problem (CSP) object. This is module is specifically
written for COSC367 lab quizzes and exercises.

Author: Kourosh Neshatian
Last modified: 13 Aug 2014
"""

from collections import namedtuple
from collections.abc import Iterable
import itertools


def scope(constraint):
    """Takes a constraint in the form of a function (or lambda expression)
    and returns the set of formal parameter names (i.e. the name of
    the variables that are used) in the function.

    """
    return set(constraint.__code__.co_varnames[
        :constraint.__code__.co_argcount])
    

class CSP(namedtuple("CSP", "domains, constraints")):
    """The CSP class represents a constraint satisfaction problem. It is
    instantiated by specifying a dictionary, domains, of the form
    "var_name": list_of_values, and a collection of constraints where
    each constraint is a function (predicate) that takes an assignment
    to some variables and returns either true or false. The csp
    variables are implicitly specified by the domains dictionary and
    are accessible through csp.variables.

    """

    def __init__(self, domains, constraints):
        assert type(domains) is dict
        assert all(type(var_name) is str for var_name in domains)
        assert all(isinstance(domain, Iterable) 
                   for domain in domains.values())
        assert isinstance(constraints, Iterable)
        assert all(callable(c) for c in constraints)
        self.variables = set(domains.keys())
        assert set.union(*[scope(c) for c in constraints]) <= self.variables,\
            """Constraint parameters must be in variables."""


