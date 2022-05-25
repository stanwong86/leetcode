def freeTime(schedule):
    cur = "07:00"
    res = []
    for s, e in sorted((s.zfill(5), e.zfill(5)) for s, e in schedule):
        print(s, e)
        if cur < s:
            cur = cur[1:] if cur[0] == "0" else cur
            s = s[1:] if s[0] == "0" else s
            res.append([cur, s])
        cur = e
    return res

schedule = [["16:00", "16:30"], ["6:00", "7:30"], ["8:30", "9:20"], ["8:00", "9:00"], ["17:30", "19:20"]]
print(freeTime(schedule))
schedule = [["12:00", "17:30"], ["8:00", "10:00"], ["10:00", "11:30"]]
print(freeTime(schedule))

schedule1 = [["10:00", "11:00"], ["11:15", "12:30"]]
schedule2 = [["9:00", "11:30"]]