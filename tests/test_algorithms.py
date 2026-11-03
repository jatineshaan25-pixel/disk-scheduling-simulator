from algorithms import fcfs, sstf

def test_fcfs_example():
    result = fcfs([98, 183, 37, 122, 14, 124, 65, 67], 53)
    assert result["total_seek"] == 640

def test_sstf_example():
    result = sstf([98, 183, 37, 122, 14, 124, 65, 67], 53)
    assert result["total_seek"] == 236