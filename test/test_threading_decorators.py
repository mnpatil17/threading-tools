import unittest
import threading
from threading_tools import SynchronizedNumber
from threading_tools import threaded_fn


class TestThreadingDecorators(unittest.TestCase):

    def test_threaded_fn(self):
        main_thread = threading.current_thread()

        @threaded_fn
        def function_to_thread(main_thread):
            assert main_thread != threading.current_thread(), \
                'Inside function_to_thread main_thread should NOT be the current thread'

        function_to_thread(main_thread)
        assert main_thread == threading.current_thread(), \
            'Outside function_to_thread, main_thread should be the current thread'
