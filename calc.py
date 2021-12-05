def calc(msg):
    msg = msg[:0:-1]
    tabl = {

    }
    for j, i in enumerate(msg):
        if msg.index(i) % 2 == 0:
            try:
                tabl[i.lower()] = tabl.get(i.lower(), 0) + int(msg[j + 1])
            except Exception:
                return 'error input'
    n1 = ''
    n2 = 0
    for i, j in tabl.items():
        n1 = n1 + '    ' + str(i) + ' x' + str(j) + '\n'
        if i == '1m':
            n2 += j
        elif i == '5m':
            n2 += j * 5
        elif i == '1h':
            n2 += j * 60
        elif i == '3h':
            n2 += j * 60 * 3
        elif i == '8h':
            n2 += j * 60 * 8

    day = n2 // 60 // 24
    hour = (n2 - (day * 24 * 60)) // 60
    minut = (n2 - (day * 24 * 60) - hour * 60)
    soft_800 = 800 * n2
    soft_1500 = 1500 * n2
    SVS = 30 * n2

    return f'''\'\'\'
    Calculator - Speedup 
    Speedups:
    
{n1}

Time Sped Up: {day} Days, {hour} Hours, {minut} Minutes
Total Minutes: {n2}

Total Event Points:
SOTF 800 points for 1m speedup - {soft_800}
SOTF 1500 points for 1m speedup - {soft_1500}
SVS 30 points for 1m speedup - {SVS}
\'\'\'
    '''