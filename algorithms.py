def fcfs(requests, head):
    path = [head]          # list of positions the head visits
    total_seek = 0         # total distance moved
    current = head         # where the head is right now

    for r in requests:     # go through requests in arrival order
        total_seek = total_seek + abs(current - r)
        current = r        # head moves to this request
        path.append(r)     # remember the position

    return {"order": requests, "path": path, "total_seek": total_seek}