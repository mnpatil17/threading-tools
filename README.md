# Threading Tools
Datatypes and decorators for threading in Python

### Installation

Currently, this package isn't available on pip. Information about pip installation will be available shortly; please check back for more updates soon.

### Usage

#### `SynchronizedNumber`
The `SynchronizedNumber` object is a threadsafe number that can be incremented and decremented atomically. Incrementation and decrementation can also be done only after a user-specified condition is passed. Here are a list of available methods for the class.

##### `increment(self, incr_value)`
The `increment` method simply increments the value of the `SynchronizedNumber` by `incr_value`. Returns whether incrementation was successful or not.

    >>> sync_number = SynchronizedNumber(15.0)
    >>> sync_number.increment(10.0)
    True
    >>> sync_number.value
    25.0

##### `decrement(self, decr_value)`
The `decrement` method simply decrements the value of the `SynchronizedNumber` by `decr_value`. Returns whether incrementation was successful or not.

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
