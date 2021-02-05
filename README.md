# Threading Tools
[![Build Status](https://travis-ci.org/mnpatil17/threading-tools.svg?branch=master)](https://travis-ci.org/mnpatil17/threading-tools)
[![Latest Version](https://img.shields.io/pypi/v/threading-tools.svg)](https://pypi.python.org/pypi/threading-tools/)


## Installation

This package uses pip for installation. You can find out more information about pip [here](https://pip.pypa.io/en/stable/quickstart/).

Installation can be done directly through pip, using `pip install threading-tools`.

If this doesn't work, or you prefer having the source code on your machine, you can also execute the
following:

1. `git clone https://github.com/mnpatil17/threading-tools.git`
2. `cd threading_tools`
3. `pip install -e .`

## Usage

### Function Decorator `@threaded_fn`
Just decorate a function of your choice with `@threaded_fn`, and it will run on a separate thread. Additionally, `threaded_fn` returns the `threading.Thread` object that represents the thread that is running your function.

    >>> from threading_tools import threaded_fn
    >>> @threaded_fn
    ... def your_function(arg0, arg1, kwarg0=None, kwarg1=None):
    ...     # your logic here...
    ...
    >>> new_thread = your_function(5, 10, kwarg0=15, kwarg1=20)  # The function is now executing on new_thread

Note: this implementation was inspired by [freakish on StackOverflow](https://stackoverflow.com/questions/19846332/python-threading-inside-a-class?answertab=active#tab-top).

### `SynchronizedNumber`
The `SynchronizedNumber` object is a threadsafe number that can be incremented and decremented atomically. Incrementation and decrementation can also be done only after a user-specified condition is passed. Here are a list of available methods for the class.

##### Math Operators
Basic mathematical operators such as `+`, `-`, `/`, `*`, `**`, `%` all work as expected for `SynchronizedNumber` objects. Note that **these operators return new `SynchronizedNumber`objects; they do not mutate the original(s)**. Here is an example.
 
    >>> from threading_tools import SynchronizedNumber
    >>> sync_number = SynchronizedNumber(15.0)
    >>> new_sync_num = sync_number + 5.0  # Returns a new SynchronizedNumber object with value 20.0
    >>> new_sync_num
    20.0
    >>> sync_number  # Original SynchronizedNumber was NOT modified
    15.0

These operations are not particularly useful in a multithreading context, but exist for the completeness of the datastructure itself.

##### Augmented Assignment Operators
Augmented Assignment operators such as `+=`, `-=`, `/=`, `*=` also work as expected for `SynchronizedNumber` and are threadsafe, atomic operations. These operations **change the value of the existing `SynchronizedNumber`**; they do not create a new object. Here is an example.

    >>> from threading_tools import SynchronizedNumber
    >>> sync_number = SynchronizedNumber(15.0)
    >>> sync_number += 5.0
    >>> sync_number  # Original SynchronizedNumber WAS modified in a threadsafe manner
    20.0

##### `increment(self, incr_value)`
The `increment` method simply increments the value of the `SynchronizedNumber` by `incr_value`. Returns whether incrementation was successful or not. This behavior is very similar to the `+=` Augmented Assignment operator, except for the fact that this method returns success or failure.

    >>> from threading_tools import SynchronizedNumber
    >>> sync_number = SynchronizedNumber(15.0)
    >>> sync_number.increment(10.0)
    True
    >>> sync_number
    25.0

##### `decrement(self, decr_value)`
The `decrement` method simply decrements the value of the `SynchronizedNumber` by `decr_value`. Returns whether incrementation was successful or not. This behavior is very similar to the `-=` Augmented Assignment operator, except for the fact that this method returns success or failure.

    >>> from threading_tools import SynchronizedNumber
    >>> sync_number = SynchronizedNumber(15.0)
    >>> sync_number.decrement(10.0)
    True
    >>> sync_number
    5.0

##### `increment_if_less_than(self, incr_value, limit, eq_ok=False)`
The `increment_if_less_than` method increments the value of the `SynchronizedNumber` by `incr_value` if the value of the `SynchronizedNumber` is less than `limit`, or if `eq_ok` is `True`and the `SynchronizedNumber`'s value is equal to `limit`.

Here's an example where incrementation fails because the limit is reached.

    >>> from threading_tools import SynchronizedNumber
    >>> sync_number = SynchronizedNumber(15.0)
    >>> sync_number.increment_if_less_than(10.0, 15.0)
    False
    >>> sync_number
    15.0

Here's an example where incrementation succeeds because the limit is not reached.

    >>> from threading_tools import SynchronizedNumber
    >>> sync_number = SynchronizedNumber(15.0)
    >>> sync_number.increment_if_less_than(10.0, 15.0, eq_ok=True)
    True
    >>> sync_number
    25.0

##### `decrement_if_greater_than(self, decr_value, limit, eq_ok=False)`
The `decrement_if_greater_than` method decrements the value of the `SynchronizedNumber` by `decr_value` if the value of the `SynchronizedNumber` is greater than `limit`, or if `eq_ok` is `True`and the `SynchronizedNumber`'s value is equal to `limit`.

Here's an example where decrementation fails because the limit is reached.

    >>> from threading_tools import SynchronizedNumber
    >>> sync_number = SynchronizedNumber(15.0)
    >>> sync_number.decrement_if_greater_than(10.0, 15.0)
    False
    >>> sync_number
    15.0

Here's an example where incrementation succeeds because the limit is not reached.

    >>> from threading_tools import SynchronizedNumber
    >>> sync_number = SynchronizedNumber(15.0)
    >>> sync_number.decrement_if_greater_than(10.0, 15.0, eq_ok=True)
    True
    >>> sync_number
    5.0


##### `increment_if_satisfies_condition(self, incr_value, satisfaction_condition)`
The `increment_if_satisfies_condition` method increments the value of the `SynchronizedNumber` by `incr_value` if the `satisfaction_condition` is met. `satisfaction_condition` is a method that takes in the value of the `SynchronizedNumber` and returns `True` or `False` based on conditions determined by the user.

    >>> from threading_tools import SynchronizedNumber
    >>> sync_number = SynchronizedNumber(15.0)
    >>> condition_func = lambda x: 10 < x < 20
    >>> sync_number.increment_if_satisfies_condition(10.0, condition_func)  # condition is satisfied, since 10 < 15.0 < 20 is True
    True
    >>> sync_number
    25.0
    >>> sync_number.increment_if_satisfies_condition(10.0, condition_func)  # condition is NOT satisfied, since 10 < 25.0 < 20 is False
    False
    >>> sync_number
    25.0

##### `decrement_if_satisfies_condition(self, decr_value, satisfaction_condition)`
The `decrement_if_satisfies_condition` method decrements the value of the `SynchronizedNumber` by `decr_value` if the `satisfaction_condition` is met. `satisfaction_condition` is a method that takes in the value of the `SynchronizedNumber` and returns `True` or `False` based on conditions determined by the user.

    >>> from threading_tools import SynchronizedNumber
    >>> sync_number = SynchronizedNumber(15.0)
    >>> condition_func = lambda x: 10 < x < 20
    >>> sync_number.decrement_if_satisfies_condition(10.0, condition_func)  # condition is satisfied, since 10 < 15.0 < 20 is True
    True
    >>> sync_number
    5.0
    >>> sync_number.decrement_if_satisfies_condition(10.0, condition_func)  # condition is NOT satisfied, since 10 < 25.0 < 20 is False
    False
    >>> sync_number
    5.0

##### `imultiply_if_satisfies_condition(self, mul_value, satisfaction_condition)`
The `imultiply_if_satisfies_condition` method increments the value of the `SynchronizedNumber` by `mul_value` if the `satisfaction_condition` is met. `satisfaction_condition` is a method that takes in the value of the `SynchronizedNumber` and returns `True` or `False` based on conditions determined by the user.

    >>> from threading_tools import SynchronizedNumber
    >>> sync_number = SynchronizedNumber(15.0)
    >>> condition_func = lambda x: 10 < x < 20
    >>> sync_number.imultiply_if_satisfies_condition(2.0, condition_func)  # condition is satisfied, since 10 < 15.0 < 20 is True
    True
    >>> sync_number
    30.0
    >>> sync_number.imultiply_if_satisfies_condition(2.0, condition_func)  # condition is NOT satisfied, since 10 < 30.0 < 20 is False
    False
    >>> sync_number
    30.0

##### `idivide_if_satisfies_condition(self, div_value, satisfaction_condition)`
The `idivide_if_satisfies_condition` method increments the value of the `SynchronizedNumber` by `div_value` if the `satisfaction_condition` is met. `satisfaction_condition` is a method that takes in the value of the `SynchronizedNumber` and returns `True` or `False` based on conditions determined by the user.

    >>> from threading_tools import SynchronizedNumber
    >>> sync_number = SynchronizedNumber(15.0)
    >>> condition_func = lambda x: 10 < x < 20
    >>> sync_number.idivide_if_satisfies_condition(3.0, condition_func)  # condition is satisfied, since 10 < 15.0 < 20 is True
    True
    >>> sync_number
    5.0
    >>> sync_number.idivide_if_satisfies_condition(3.0, condition_func)  # condition is NOT satisfied, since 10 < 5.0 < 20 is False
    False
    >>> sync_number
    5.0


## Testing

If you choose, you can clone this repository locally and run the tests yourself.
To run tests, simply run `nosetests` from the `threading_tools/` directory.
