def fcfs(requests, head):
    path = [head]          # list of positions the head visits
    total_seek = 0         # total distance moved
    current = head         # where the head is right now

    for r in requests:     # go through requests in arrival order
        total_seek = total_seek + abs(current - r)
        current = r        # head moves to this request
        path.append(r)     # remember the position

    return {"order": requests, "path": path, "total_seek": total_seek}

def sstf(requests, head):
    pending = list(requests)
    path = [head]
    order = []
    total_seek = 0
    current = head

    while len(pending) > 0:
        closest = min(pending, key=lambda r: abs(current - r))
        total_seek = total_seek + abs(current - closest)
        current = closest
        path.append(closest)
        order.append(closest)
        pending.remove(closest)

    return {"order": order, "path": path, "total_seek": total_seek}