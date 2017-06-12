# Threading Tools
[![Build Status](https://travis-ci.org/mnpatil17/threading-tools.svg?branch=master)](https://travis-ci.org/mnpatil17/threading-tools)

## Installation

Currently, this package isn't available on pip. Information about pip installation will be available shortly; please check back for more updates soon.

## Usage

### `SynchronizedNumber`
The `SynchronizedNumber` object is a threadsafe number that can be incremented and decremented atomically. Incrementation and decrementation can also be done only after a user-specified condition is passed. Here are a list of available methods for the class.

##### Math Operators
Basic mathematical operators such as `+`, `-`, `/`, `*`, `**`, `%` all work as expected for `SynchronizedNumber` objects. Note that **these operators return new `SynchronizedNumber`objects; they do not mutate the original(s)**. Here is an example.

    >>> sync_number = SynchronizedNumber(15.0)
    >>> new_sync_num = sync_number + 5.0  # Returns a new SynchronizedNumber object with value 20.0
    >>> new_sync_num
    20.0
    >>> sync_number  # Original SynchronizedNumber was NOT modified
    15.0

These operations are not particularly useful in a multithreading context, but exist for the completeness of the datastructure itself.

##### Augmented Assignment Operators
Augmented Assignment operators such as `+=`, `-=`, `/=`, `*=` also work as expected for `SynchronizedNumber` and are threadsafe, atomic operations. These operations **change the value of the existing `SynchronizedNumber`**; they do not create a new object. Here is an example.

    >>> sync_number = SynchronizedNumber(15.0)
    >>> sync_number += 5.0
    >>> sync_number  # Original SynchronizedNumber WAS modified in a threadsafe manner
    20.0

##### `increment(self, incr_value)`
The `increment` method simply increments the value of the `SynchronizedNumber` by `incr_value`. Returns whether incrementation was successful or not. This behavior is very similar to the `+=` Augmented Assignment operator, except for the fact that this method returns success or failure.

    >>> sync_number = SynchronizedNumber(15.0)
    >>> sync_number.increment(10.0)
    True
    >>> sync_number.value
    25.0

##### `decrement(self, decr_value)`
The `decrement` method simply decrements the value of the `SynchronizedNumber` by `decr_value`. Returns whether incrementation was successful or not. This behavior is very similar to the `-=` Augmented Assignment operator, except for the fact that this method returns success or failure.

    >>> sync_number = SynchronizedNumber(15.0)
    >>> sync_number.decrement(10.0)
    True
    >>> sync_number.value
    5.0

##### `increment_if_less_than(self, incr_value, limit, eq_ok=False)`
The `increment_if_less_than` method increments the value of the `SynchronizedNumber` by `incr_value` if the value of the `SynchronizedNumber` is less than `limit`, or if `eq_ok` is `True`and the `SynchronizedNumber`'s value is equal to `limit`.

Here's an example where incrementation fails because the limit is reached.

    >>> sync_number = SynchronizedNumber(15.0)
    >>> sync_number.increment_if_less_than(10.0, 15.0)
    False
    >>> sync_number.value
    15.0
    
Here's an example where incrementation succeeds because the limit is not reached.

    >>> sync_number = SynchronizedNumber(15.0)
    >>> sync_number.increment_if_less_than(10.0, 15.0, eq_ok=True)
    True
    >>> sync_number.value
    25.0
   
##### `decrement_if_greater_than(self, decr_value, limit, eq_ok=False)`
The `decrement_if_greater_than` method decrements the value of the `SynchronizedNumber` by `decr_value` if the value of the `SynchronizedNumber` is greater than `limit`, or if `eq_ok` is `True`and the `SynchronizedNumber`'s value is equal to `limit`.

Here's an example where decrementation fails because the limit is reached.

    >>> sync_number = SynchronizedNumber(15.0)
    >>> sync_number.decrement_if_greater_than(10.0, 15.0)
    False
    >>> sync_number.value
    15.0
    
Here's an example where incrementation succeeds because the limit is not reached.

    >>> sync_number = SynchronizedNumber(15.0)
    >>> sync_number.decrement_if_greater_than(10.0, 15.0, eq_ok=True)
    True
    >>> sync_number.value
    5.0


##### `increment_if_satisfies_condition(self, incr_value, satisfaction_condition)`
The `increment_if_satisfies_condition` method increments the value of the `SynchronizedNumber` by `incr_value` if the `satisfaction_condition` is met. `satisfaction_condition` is a method that takes in the value of the `SynchronizedNumber` and returns `True` or `False` based on conditions determined by the user.

    >>> sync_number = SynchronizedNumber(15.0)
    >>> condition_func = lambda x: 10 < x < 20
    >>> sync_number.increment_if_satisfies_condition(10.0, condition_func)  # condition is satisfied, since 10 < 15.0 < 20 is True
    True
    >>> sync_number.value
    25.0
    >>> sync_number.increment_if_satisfies_condition(10.0, condition_func)  # condition is NOT satisfied, since 10 < 25.0 < 20 is False
    False
    >>> sync_number.value
    25.0
    
##### `decrement_if_satisfies_condition(self, decr_value, satisfaction_condition)`
The `decrement_if_satisfies_condition` method decrements the value of the `SynchronizedNumber` by `decr_value` if the `satisfaction_condition` is met. `satisfaction_condition` is a method that takes in the value of the `SynchronizedNumber` and returns `True` or `False` based on conditions determined by the user.

    >>> sync_number = SynchronizedNumber(15.0)
    >>> condition_func = lambda x: 10 < x < 20
    >>> sync_number.decrement_if_satisfies_condition(10.0, condition_func)  # condition is satisfied, since 10 < 15.0 < 20 is True
    True
    >>> sync_number.value
    5.0
    >>> sync_number.decrement_if_satisfies_condition(10.0, condition_func)  # condition is NOT satisfied, since 10 < 25.0 < 20 is False
    False
    >>> sync_number.value
    5.0
    
##### `imultiply_if_satisfies_condition(self, mul_value, satisfaction_condition)`
The `imultiply_if_satisfies_condition` method increments the value of the `SynchronizedNumber` by `mul_value` if the `satisfaction_condition` is met. `satisfaction_condition` is a method that takes in the value of the `SynchronizedNumber` and returns `True` or `False` based on conditions determined by the user.

    >>> sync_number = SynchronizedNumber(15.0)
    >>> condition_func = lambda x: 10 < x < 20
    >>> sync_number.imultiply_if_satisfies_condition(2.0, condition_func)  # condition is satisfied, since 10 < 15.0 < 20 is True
    True
    >>> sync_number.value
    30.0
    >>> sync_number.imultiply_if_satisfies_condition(2.0, condition_func)  # condition is NOT satisfied, since 10 < 30.0 < 20 is False
    False
    >>> sync_number.value
    30.0

##### `idivide_if_satisfies_condition(self, div_value, satisfaction_condition)`
The `idivide_if_satisfies_condition` method increments the value of the `SynchronizedNumber` by `div_value` if the `satisfaction_condition` is met. `satisfaction_condition` is a method that takes in the value of the `SynchronizedNumber` and returns `True` or `False` based on conditions determined by the user.

    >>> sync_number = SynchronizedNumber(15.0)
    >>> condition_func = lambda x: 10 < x < 20
    >>> sync_number.idivide_if_satisfies_condition(3.0, condition_func)  # condition is satisfied, since 10 < 15.0 < 20 is True
    True
    >>> sync_number.value
    5.0
    >>> sync_number.idivide_if_satisfies_condition(3.0, condition_func)  # condition is NOT satisfied, since 10 < 5.0 < 20 is False
    False
    >>> sync_number.value
    5.0
