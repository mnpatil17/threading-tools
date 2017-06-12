import unittest
import threading
from synchronized_number import SynchronizedNumber

NUM_TRIALS = 2500


class TestSynchronizedNumber(unittest.TestCase):

    def test_increment(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(0.0)

            thread1_incr_amt = 50
            thread2_incr_amt = 100

            thread1 = threading.Thread(target=sync_num.increment, args=(thread1_incr_amt, ))
            thread2 = threading.Thread(target=sync_num.increment, args=(thread2_incr_amt, ))

            # Start the threads
            thread1.start()
            thread2.start()

            # Wait on the threads
            thread1.join()
            thread2.join()

            assert sync_num == 150, 'Trial {0}: sync_num is {1} but must be 150'.format(i, sync_num)

    def test_decrement(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(150.0)

            thread1_decr_amt = 50
            thread2_decr_amt = 100

            thread1 = threading.Thread(target=sync_num.decrement, args=(thread1_decr_amt, ))
            thread2 = threading.Thread(target=sync_num.decrement, args=(thread2_decr_amt, ))

            # Start the threads
            thread1.start()
            thread2.start()

            # Wait on the threads
            thread1.join()
            thread2.join()

            assert sync_num == 0, 'Trial {0}: sync_num is {1} but must be 0'.format(i, sync_num)

    def test_strict_increment_if_less_than(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(0.0)

            thread1_incr_amt = 100
            thread2_incr_amt = 100
            limit = 100

            thread1 = threading.Thread(
                target=sync_num.increment_if_less_than, args=(thread1_incr_amt, limit))
            thread2 = threading.Thread(
                target=sync_num.increment_if_less_than, args=(thread2_incr_amt, limit))

            # Start the threads
            thread1.start()
            thread2.start()

            # Wait on the threads
            thread1.join()
            thread2.join()

            assert sync_num == 100, 'Trial {0}: sync_num is {1} but must be 100'.format(i, sync_num)

    def test_eq_ok_increment_if_less_than(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(0.0)

            thread1_incr_amt = 100
            thread2_incr_amt = 100
            limit = 100

            thread1 = threading.Thread(
                target=sync_num.increment_if_less_than, args=(thread1_incr_amt, limit, True))
            thread2 = threading.Thread(
                target=sync_num.increment_if_less_than, args=(thread2_incr_amt, limit, True))

            # Start the threads
            thread1.start()
            thread2.start()

            # Wait on the threads
            thread1.join()
            thread2.join()

            assert sync_num == 200, 'Trial {0}: sync_num is {1} but must be 200'.format(i, sync_num)

    def test_strict_decrement_if_greater_than(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(200.0)

            thread1_decr_amt = 100
            thread2_decr_amt = 100
            limit = 100

            thread1 = threading.Thread(
                target=sync_num.decrement_if_greater_than, args=(thread1_decr_amt, limit))
            thread2 = threading.Thread(
                target=sync_num.decrement_if_greater_than, args=(thread2_decr_amt, limit))

            # Start the threads
            thread1.start()
            thread2.start()

            # Wait on the threads
            thread1.join()
            thread2.join()

            assert sync_num == 100, 'Trial {0}: sync_num is {1} but must be 100'.format(i, sync_num)

    def test_eq_ok_decrement_if_greater_than(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(200.0)

            thread1_decr_amt = 100
            thread2_decr_amt = 100
            limit = 100

            thread1 = threading.Thread(
                target=sync_num.decrement_if_greater_than, args=(thread1_decr_amt, limit, True))
            thread2 = threading.Thread(
                target=sync_num.decrement_if_greater_than, args=(thread2_decr_amt, limit, True))

            # Start the threads
            thread1.start()
            thread2.start()

            # Wait on the threads
            thread1.join()
            thread2.join()

            assert sync_num == 0, 'Trial {0}: sync_num is {1} but must be 0'.format(i, sync_num)

    def test_increment_if_satisfies_condition(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(51.0)

            thread1_incr_amt = 40
            thread2_incr_amt = 40
            thread3_incr_amt = 40

            def condition(x):
                return 50 < x < 100

            thread1 = threading.Thread(
                target=sync_num.increment_if_satisfies_condition,
                args=(thread1_incr_amt, condition))
            thread2 = threading.Thread(
                target=sync_num.increment_if_satisfies_condition,
                args=(thread2_incr_amt, condition))
            thread3 = threading.Thread(
                target=sync_num.increment_if_satisfies_condition,
                args=(thread3_incr_amt, condition))

            # Start the threads
            thread1.start()
            thread2.start()
            thread3.start()

            # Wait on the threads
            thread1.join()
            thread2.join()
            thread3.join()

            assert sync_num == 131, 'Trial {0}: sync_num is {1} but must be 131'.format(i, sync_num)

    def test_decrement_if_satisfies_condition(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(99.0)

            thread1_decr_amt = 40
            thread2_decr_amt = 40
            thread3_decr_amt = 40

            def condition(x):
                return 50 < x < 100

            thread1 = threading.Thread(
                target=sync_num.decrement_if_satisfies_condition,
                args=(thread1_decr_amt, condition))
            thread2 = threading.Thread(
                target=sync_num.decrement_if_satisfies_condition,
                args=(thread2_decr_amt, condition))
            thread3 = threading.Thread(
                target=sync_num.decrement_if_satisfies_condition,
                args=(thread3_decr_amt, condition))

            # Start the threads
            thread1.start()
            thread2.start()
            thread3.start()

            # Wait on the threads
            thread1.join()
            thread2.join()
            thread3.join()

            assert sync_num == 19, 'Trial {0}: sync_num is {1} but must be 19'.format(i, sync_num)

    def test_lock_release_on_error(self):

        def condition(x):
            """
            This is an intentionally bad condition that triggers an error
            """
            return 'string' + x

        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(99.0)

            def wrapper_fn():
                try:
                    sync_num.decrement_if_satisfies_condition(40, condition)
                except Exception as e:
                    assert isinstance(e, TypeError), \
                        'The exception should be a TypeError. Instead was a {0}. {1}'.format(
                        type(e), e)

            thread1 = threading.Thread(target=wrapper_fn)
            thread1.start()
            thread1.join()

            assert not sync_num._lock.locked(), 'Trial {0}: The lock should not be locked. It was.'

    def test_set_value(self):
        """
        Note: this is a cursory functionality check. This does NOT test threadsafety.
        """
        sync_num = SynchronizedNumber(0.0)

        thread1_amt = 100
        thread1 = threading.Thread(target=sync_num.set_value, args=(thread1_amt, ))

        # Start the thread
        thread1.start()

        # Wait on the thread
        thread1.join()

        assert sync_num == 100, 'sync_num is {0} but must be 100'.format(sync_num)
