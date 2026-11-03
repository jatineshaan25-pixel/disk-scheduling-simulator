from algorithms import fcfs, sstf

def test_fcfs_example():
    result = fcfs([98, 183, 37, 122, 14, 124, 65, 67], 53)
    assert result["total_seek"] == 640

def test_sstf_example():
    result = sstf([98, 183, 37, 122, 14, 124, 65, 67], 53)
    assert result["total_seek"] == 236

def scan(requests, head, disk_size, direction="up"):
    lower = sorted([r for r in requests if r < head])    # requests below the head
    upper = sorted([r for r in requests if r >= head])   # requests at or above the head

    if direction == "up":
        sequence = upper + [disk_size - 1] + lower[::-1]
    else:
        sequence = lower[::-1] + [0] + upper

    path = [head]
    order = []
    total_seek = 0
    current = head

    for pos in sequence:
         add abs(current - pos) to total_seek
         current = pos, and add pos to path
         if pos is one of the original requests, add it to order
        

    return {"order": order, "path": path, "total_seek": total_seek}