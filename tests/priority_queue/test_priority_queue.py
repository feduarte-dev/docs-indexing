from ting_file_management.priority_queue import PriorityQueue
import pytest

mock1 = {
    "nome_do_arquivo": "mock1",
    "qtd_linhas": 6,
    "linhas_do_arquivo": "data1",
}

mock2 = {
    "nome_do_arquivo": "mock2",
    "qtd_linhas": 3,
    "linhas_do_arquivo": "data2",
}

mock3 = {
    "nome_do_arquivo": "mock3",
    "qtd_linhas": 10,
    "linhas_do_arquivo": "data3",
}

mock4 = {
    "nome_do_arquivo": "mock4",
    "qtd_linhas": 1,
    "linhas_do_arquivo": "data4",
}


def test_basic_priority_queueing():
    priority_queue = PriorityQueue()

    priority_queue.enqueue(mock1)
    priority_queue.enqueue(mock2)
    priority_queue.enqueue(mock3)
    priority_queue.enqueue(mock4)

    assert len(priority_queue) == 4
    assert len(priority_queue.high_priority) == 2
    assert len(priority_queue.regular_priority) == 2

    priority_queue.dequeue()
    assert len(priority_queue) == 3

    data_search = priority_queue.search(1)
    assert data_search["qtd_linhas"] == 6

    with pytest.raises(IndexError, match="Índice Inválido ou Inexistente"):
        priority_queue.search(10)
