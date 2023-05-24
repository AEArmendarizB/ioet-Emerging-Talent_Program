import pytest
from queue import Queue
import exercise_1

#It help for comparate the content of the queue and not the references
class QueueWithContentComparison(Queue):
    def __eq__(self, other):
        if isinstance(other, QueueWithContentComparison):
            return list(self.queue) == list(other.queue)
        return False

def test__add_new_client__return_queue__when_input_are_queue_and_int():
    client = 1
    supermarket = QueueWithContentComparison()
    supermarket_client_expected = QueueWithContentComparison()
    supermarket_client_expected.put(client)
    supermarket_client = exercise_1.add_new_client(supermarket, client)
    assert supermarket_client_expected == supermarket_client

def test__attend_client__return_queue__when_input_is_queue():
    supermarket = QueueWithContentComparison()
    supermarket.put(2)
    supermarket_client_expected = QueueWithContentComparison()
    supermarket_client = exercise_1.attend_client(supermarket)
    assert supermarket_client_expected == supermarket_client






