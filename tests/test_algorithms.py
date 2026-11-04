from algorithms import fcfs, sstf, scan, c_scan

def test_fcfs_example():
    result = fcfs([98, 183, 37, 122, 14, 124, 65, 67], 53)
    assert result["total_seek"] == 640

def test_sstf_example():
    result = sstf([98, 183, 37, 122, 14, 124, 65, 67], 53)
    assert result["total_seek"] == 236

def test_scan_example():
    result = scan([98, 183, 37, 122, 14, 124, 65, 67], 53, 200, "up")
    assert result["total_seek"] == 331

def test_c_scan_example():
    result = c_scan([98, 183, 37, 122, 14, 124, 65, 67], 53, 200)
    assert result["total_seek"] == 382