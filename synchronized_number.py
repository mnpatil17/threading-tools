#
# synchronized_number.py
# An implementation of a thread-safe number in Python
#

import threading


class SynchronizedNumber:
    """
    An implementation of a threadsafe, synchronized number in Python
    """

    def __init__(self, initial_value, should_block_thread=True):
        self.should_block_thread = should_block_thread
        self._lock = threading.Lock()
        self.value = 0
        self.set_value(initial_value)

    def set_value(self, new_value):
        """
        Sets the value of this number.

        :param: new_value - The value to set
        :return: True if value is successfully set, False if not.
        """
        if self._lock.acquire(self.should_block_thread):
            try:
                self.value = new_value
                return True
            finally:
                self._lock.release()

        return False

    def increment(self, incr_value):
        """
        Increments the value of this number.

        :param: incr_value - The value to increment by
        :return: True if value is increment successfully set, False if not.
        """
        return self.increment_if_satisfies_condition(incr_value, lambda x: True)

    def decrement(self, decr_value):
        """
        Decrements the value of this number.

        :param: decr_value - The value to decremented by
        :return: True if value is decremented successfully set, False if not.
        """
        return self.increment(-decr_value)

    def increment_if_less_than(self, incr_value, limit, eq_ok=False):
        """
        Increments the value of this number only if this number is less than `limit`.

        :param: incr_value - The value to increment by
        :param: eq_ok [optional] - If set to True, the function also allows incrementation if this
                                   number was equal to the `limit`
        :return: True if value is increment successfully set, False if not.
        """

        def does_satisfy(val):
            return val < limit or (eq_ok and val == limit)

        return self.increment_if_satisfies_condition(incr_value, does_satisfy)

    def decrement_if_greater_than(self, decr_value, limit, eq_ok=False):
        """
        Increments the value of this number only if this number is greater than `limit`.

        :param: decr_value - The value to increment by
        :param: eq_ok [optional] - If set to True, the function also allows incrementation if this
                                   number was equal to the `limit`
        :return: True if value is increment successfully set, False if not.
        """

        def does_satisfy(val):
            return val > limit or (eq_ok and val == limit)

        return self.decrement_if_satisfies_condition(decr_value, does_satisfy)

    def increment_if_satisfies_condition(self, incr_value, satisfaction_condition):
        """
        Increments the value of this number only if this number satisfies `satisfaction_condition`.

        :param: incr_value - The value to increment by
        :param: satisfaction_condition - A function that takes in the current value and returns
                                         True if the condition you want is satisfied, and False
                                         otherwise

        :return: True if value is increment successfully set, False if not.
        """
        if self._lock.acquire(self.should_block_thread):
            try:
                if satisfaction_condition(self.value):
                    self.value += incr_value
                    return True
                else:
                    return False
            finally:
                self._lock.release()

        return False

    def decrement_if_satisfies_condition(self, decr_value, satisfaction_condition):
        """
        Decrements the value of this number only if this number satisfies `satisfaction_condition`.

        :param: decr_value - The value to decrement by
        :param: satisfaction_condition - A function that takes in the current value and returns
                                         True if the condition you want is satisfied, and False
                                         otherwise

        :return: True if value is decrements successfully set, False if not.
        """
        return self.increment_if_satisfies_condition(-decr_value, satisfaction_condition)

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        if isinstance(other, SynchronizedNumber):
            return self.value == other.value
        else:
            return self.value == other
