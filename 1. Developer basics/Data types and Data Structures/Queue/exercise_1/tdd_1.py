import pytest
from queue import Queue
import exercise_1

def test__add_new_client__return_queue__when_input_is_a_int():
    client = 1
    queue_client = Queue()
    queue_client.put(client)
    queue_client_expected = exercise_1.add_new_client(client)
    assert queue_client_expected == queue_client