from algorithms import fcfs

def test_fcfs_example():
    result = fcfs([98, 183, 37, 122, 14, 124, 65, 67], 53)
    assert result["total_seek"] == 640