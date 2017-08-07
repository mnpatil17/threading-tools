import unittest
import multiprocessing
from threading_tools import SynchronizedNumber, LockAcquisitionException

NUM_TRIALS = 50


class TestSynchronizedNumberOnProcesses(unittest.TestCase):

    def test_increment(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(0.0, process_sync=True)

            process1_incr_amt = 50
            process2_incr_amt = 100

            process1 = multiprocessing.Process(
                target=sync_num.increment, args=(process1_incr_amt, ))
            process2 = multiprocessing.Process(
                target=sync_num.increment, args=(process2_incr_amt, ))

            # Start the processes
            process1.start()
            process2.start()

            # Wait on the processes
            process1.join()
            process2.join()

            assert sync_num == 150, 'Trial {0}: sync_num is {1} but must be 150'.format(i, sync_num)

    def test_decrement(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(150.0, process_sync=True)

            process1_decr_amt = 50
            process2_decr_amt = 100

            process1 = multiprocessing.Process(
                target=sync_num.decrement, args=(process1_decr_amt, ))
            process2 = multiprocessing.Process(
                target=sync_num.decrement, args=(process2_decr_amt, ))

            # Start the processes
            process1.start()
            process2.start()

            # Wait on the processes
            process1.join()
            process2.join()

            assert sync_num == 0, 'Trial {0}: sync_num is {1} but must be 0'.format(i, sync_num)

    def test_strict_increment_if_less_than(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(0.0, process_sync=True)

            process1_incr_amt = 100
            process2_incr_amt = 100
            limit = 100

            process1 = multiprocessing.Process(
                target=sync_num.increment_if_less_than, args=(process1_incr_amt, limit))
            process2 = multiprocessing.Process(
                target=sync_num.increment_if_less_than, args=(process2_incr_amt, limit))

            # Start the processes
            process1.start()
            process2.start()

            # Wait on the processes
            process1.join()
            process2.join()

            assert sync_num == 100, 'Trial {0}: sync_num is {1} but must be 100'.format(i, sync_num)

    def test_eq_ok_increment_if_less_than(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(0.0, process_sync=True)

            process1_incr_amt = 100
            process2_incr_amt = 100
            limit = 100

            process1 = multiprocessing.Process(
                target=sync_num.increment_if_less_than, args=(process1_incr_amt, limit, True))
            process2 = multiprocessing.Process(
                target=sync_num.increment_if_less_than, args=(process2_incr_amt, limit, True))

            # Start the processes
            process1.start()
            process2.start()

            # Wait on the processes
            process1.join()
            process2.join()

            assert sync_num == 200, 'Trial {0}: sync_num is {1} but must be 200'.format(i, sync_num)

    def test_strict_decrement_if_greater_than(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(200.0, process_sync=True)

            process1_decr_amt = 100
            process2_decr_amt = 100
            limit = 100

            process1 = multiprocessing.Process(
                target=sync_num.decrement_if_greater_than, args=(process1_decr_amt, limit))
            process2 = multiprocessing.Process(
                target=sync_num.decrement_if_greater_than, args=(process2_decr_amt, limit))

            # Start the processes
            process1.start()
            process2.start()

            # Wait on the processes
            process1.join()
            process2.join()

            assert sync_num == 100, 'Trial {0}: sync_num is {1} but must be 100'.format(i, sync_num)

    def test_eq_ok_decrement_if_greater_than(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(200.0, process_sync=True)

            process1_decr_amt = 100
            process2_decr_amt = 100
            limit = 100

            process1 = multiprocessing.Process(
                target=sync_num.decrement_if_greater_than, args=(process1_decr_amt, limit, True))
            process2 = multiprocessing.Process(
                target=sync_num.decrement_if_greater_than, args=(process2_decr_amt, limit, True))

            # Start the processes
            process1.start()
            process2.start()

            # Wait on the processes
            process1.join()
            process2.join()

            assert sync_num == 0, 'Trial {0}: sync_num is {1} but must be 0'.format(i, sync_num)

    def test_increment_if_satisfies_condition(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(51.0, process_sync=True)

            process1_incr_amt = 40
            process2_incr_amt = 40
            process3_incr_amt = 40

            def condition(x):
                return 50 < x < 100

            process1 = multiprocessing.Process(
                target=sync_num.increment_if_satisfies_condition,
                args=(process1_incr_amt, condition))
            process2 = multiprocessing.Process(
                target=sync_num.increment_if_satisfies_condition,
                args=(process2_incr_amt, condition))
            process3 = multiprocessing.Process(
                target=sync_num.increment_if_satisfies_condition,
                args=(process3_incr_amt, condition))

            # Start the processes
            process1.start()
            process2.start()
            process3.start()

            # Wait on the processes
            process1.join()
            process2.join()
            process3.join()

            assert sync_num == 131, 'Trial {0}: sync_num is {1} but must be 131'.format(i, sync_num)

    def test_decrement_if_satisfies_condition(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(99.0, process_sync=True)

            process1_decr_amt = 40
            process2_decr_amt = 40
            process3_decr_amt = 40

            def condition(x):
                return 50 < x < 100

            process1 = multiprocessing.Process(
                target=sync_num.decrement_if_satisfies_condition,
                args=(process1_decr_amt, condition))
            process2 = multiprocessing.Process(
                target=sync_num.decrement_if_satisfies_condition,
                args=(process2_decr_amt, condition))
            process3 = multiprocessing.Process(
                target=sync_num.decrement_if_satisfies_condition,
                args=(process3_decr_amt, condition))

            # Start the processes
            process1.start()
            process2.start()
            process3.start()

            # Wait on the processes
            process1.join()
            process2.join()
            process3.join()

            assert sync_num == 19, 'Trial {0}: sync_num is {1} but must be 19'.format(i, sync_num)

    def test_lock_release_on_error(self):

        def condition(x):
            """
            This is an intentionally bad condition that triggers an error
            """
            return 'string' + x

        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(99.0, process_sync=True)

            def wrapper_fn():
                try:
                    sync_num.decrement_if_satisfies_condition(40, condition)
                except Exception as e:
                    assert isinstance(e, TypeError), \
                        'The exception should be a TypeError. Instead was a {0}. {1}'.format(
                        type(e), e)

            process1 = multiprocessing.Process(target=wrapper_fn)
            process1.start()
            process1.join()

            assert not sync_num._lock.locked(), 'Trial {0}: The lock should not be locked. It was.'

    def test_set_value(self):
        """
        Note: this is a cursory functionality check. This does NOT test processesafety.
        """
        sync_num = SynchronizedNumber(0.0, process_sync=True)

        process1_amt = 100
        process1 = multiprocessing.Process(target=sync_num.set_value, args=(process1_amt, ))

        # Start the process
        process1.start()

        # Wait on the process
        process1.join()

        assert sync_num == 100, 'sync_num is {0} but must be 100'.format(sync_num)

    def test_iadd_success(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(0.0, process_sync=True)

            process1_incr_amt = 50
            process2_incr_amt = 100

            def incr_wrapper(sync_num, amt):
                sync_num += amt

            process1 = multiprocessing.Process(
                target=incr_wrapper, args=(sync_num, process1_incr_amt, ))
            process2 = multiprocessing.Process(
                target=incr_wrapper, args=(sync_num, process2_incr_amt, ))

            # Start the processes
            process1.start()
            process2.start()

            # Wait on the processes
            process1.join()
            process2.join()

            assert sync_num == 150, 'Trial {0}: sync_num is {1} but must be 150'.format(i, sync_num)

    def test_isub_success(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(150.0, process_sync=True)

            process1_decr_amt = 50
            process2_decr_amt = 100

            def decr_wrapper(sync_num, amt):
                sync_num -= amt

            process1 = multiprocessing.Process(
                target=decr_wrapper, args=(sync_num, process1_decr_amt, ))
            process2 = multiprocessing.Process(
                target=decr_wrapper, args=(sync_num, process2_decr_amt, ))

            # Start the processes
            process1.start()
            process2.start()

            # Wait on the processes
            process1.join()
            process2.join()

            assert sync_num == 0, 'Trial {0}: sync_num is {1} but must be 0'.format(i, sync_num)

    def test_imul_success(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(1.0, process_sync=True)

            process1_mul_amt = 5
            process2_mul_amt = 10

            def mul_wrapper(sync_num, amt):
                sync_num *= amt

            process1 = multiprocessing.Process(
                target=mul_wrapper, args=(sync_num, process1_mul_amt, ))
            process2 = multiprocessing.Process(
                target=mul_wrapper, args=(sync_num, process2_mul_amt, ))

            # Start the processes
            process1.start()
            process2.start()

            # Wait on the processes
            process1.join()
            process2.join()

            assert sync_num == 50, 'Trial {0}: sync_num is {1} but must be 50'.format(i, sync_num)

    def test_idiv_success(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(50.0, process_sync=True)

            process1_div_amt = 7
            process2_div_amt = 10

            def div_wrapper(sync_num, amt):
                sync_num /= amt

            process1 = multiprocessing.Process(
                target=div_wrapper, args=(sync_num, process1_div_amt, ))
            process2 = multiprocessing.Process(
                target=div_wrapper, args=(sync_num, process2_div_amt, ))

            # Start the processes
            process1.start()
            process2.start()

            # Wait on the processes
            process1.join()
            process2.join()

            assert round(sync_num.value, 4) == 0.7143, \
                'Trial {0}: sync_num is {1} but must be 0.7143'.format(i, sync_num)

    def test_idivide_if_satisfies_condition(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(99.0, process_sync=True)

            process1_idiv_amt = 1.5
            process2_idiv_amt = 1.5
            process3_idiv_amt = 1.5

            def condition(x):
                return 50 < x < 100

            process1 = multiprocessing.Process(
                target=sync_num.idivide_if_satisfies_condition,
                args=(process1_idiv_amt, condition))
            process2 = multiprocessing.Process(
                target=sync_num.idivide_if_satisfies_condition,
                args=(process2_idiv_amt, condition))
            process3 = multiprocessing.Process(
                target=sync_num.idivide_if_satisfies_condition,
                args=(process3_idiv_amt, condition))

            # Start the processes
            process1.start()
            process2.start()
            process3.start()
            # Wait on the processes
            process1.join()
            process2.join()
            process3.join()

            assert sync_num == 44, \
                'Trial {0}: sync_num is {1} but must be 44'.format(i, sync_num)

    def test_imultiply_if_satisfies_condition(self):
        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(51.0, process_sync=True)

            process1_imul_amt = 1.5
            process2_imul_amt = 1.5
            process3_imul_amt = 1.5

            def condition(x):
                return 50 < x < 100

            process1 = multiprocessing.Process(
                target=sync_num.imultiply_if_satisfies_condition,
                args=(process1_imul_amt, condition))
            process2 = multiprocessing.Process(
                target=sync_num.imultiply_if_satisfies_condition,
                args=(process2_imul_amt, condition))
            process3 = multiprocessing.Process(
                target=sync_num.imultiply_if_satisfies_condition,
                args=(process3_imul_amt, condition))

            # Start the processes
            process1.start()
            process2.start()
            process3.start()

            # Wait on the processes
            process1.join()
            process2.join()
            process3.join()

            assert sync_num == 114.75, \
                'Trial {0}: sync_num is {1} but must be 114.75'.format(i, sync_num)

    def test_non_blocking_iadd(self):

        def iadd_wrapper(sync_num):
            try:
                sync_num += 5.0
                assert False, 'Exception was not thrown, but it should have been thrown'
            except Exception as e:
                assert isinstance(e, LockAcquisitionException), \
                    'The exception should be a LockAcquisitionException. Instead was a {0}. {1}' \
                    .format(type(e), e)

        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(10.0, process_sync=True, block_thread_or_process=False)

            sync_num._lock.acquire()  # Acquire lock on main process so others can't acquire it
            process = multiprocessing.Process(target=iadd_wrapper, args=(sync_num, ))
            process.start()

            process.join()
            sync_num._lock.release()

    def test_non_blocking_imul(self):

        def imul_wrapper(sync_num):
            try:
                sync_num *= 5.0
                assert False, 'Exception was not thrown, but it should have been thrown'
            except Exception as e:
                assert isinstance(e, LockAcquisitionException), \
                    'The exception should be a LockAcquisitionException. Instead was a {0}. {1}' \
                    .format(type(e), e)

        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(10.0, process_sync=True, block_thread_or_process=False)

            sync_num._lock.acquire()  # Acquire lock on main process so others can't acquire it
            process = multiprocessing.Process(target=imul_wrapper, args=(sync_num, ))
            process.start()

            process.join()
            sync_num._lock.release()

    def test_non_blocking_idiv(self):

        def idiv_wrapper(sync_num):
            try:
                sync_num /= 5.0
                assert False, 'Exception was not thrown, but it should have been thrown'
            except Exception as e:
                assert isinstance(e, LockAcquisitionException), \
                    'The exception should be a LockAcquisitionException. Instead was a {0}. {1}' \
                    .format(type(e), e)

        for i in range(NUM_TRIALS):
            sync_num = SynchronizedNumber(10.0, process_sync=True, block_thread_or_process=False)

            sync_num._lock.acquire()  # Acquire lock on main process so others can't acquire it
            process = multiprocessing.Process(target=idiv_wrapper, args=(sync_num, ))
            process.start()

            process.join()
            sync_num._lock.release()
