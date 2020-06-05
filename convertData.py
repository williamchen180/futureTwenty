

# history,TX00,36458,20200603,94512,322000,1124600,1124700,1124700,7,0,+7

def converToTrend(target, ext='大台', big=20, little=5):
    kmin = {}
    with open('data/' + ext + '/morning/' + target + '_min.csv', 'w') as fmin:
        with open('data/' + ext + '/morning/' + target + '_converted.csv', 'w') as fout:
            with open('data/' + ext + '/morning/' + target + '.csv') as f:
                l = f.readline()
                fmin.write('\ufeff時間,口差,大單,散單\n')
                fout.write(l)
                for l in f.readlines():
                    x = l.split(',')
                    if len(x[4]) == 5:
                        x[4] = '%2.2d:%s:%s' % (int(x[4][0:1]), x[4][1:3], x[4][3:])
                    else:
                        x[4] = '%s:%s:%s' % (x[4][0:2], x[4][2:4], x[4][4:])

                    if x[4] < '08:45:00':
                        continue

                    x[6] = str(float(x[6])/100)
                    x[7] = str(float(x[7])/100)
                    x[8] = str(float(x[8])/100)

                    #print(x)
                    if x[11][0] == '#':
                        vol = int(x[11][1:])
                    else:
                        vol = int(x[11])

                    fout.write(','.join(x))

                    minute = x[4][0:5]
                    if not minute in kmin.keys():
                        kmin[minute] = [0, 0, 0]

                    if x[11][0] != '#':
                        kmin[minute][0] = kmin[minute][0] + vol

                    if abs(vol) > big:
                        kmin[minute][1] = kmin[minute][1] + vol
                    if abs(vol) < little:
                        kmin[minute][1] = kmin[minute][1] + vol

        for k in sorted(kmin.keys()):
            fmin.write('%s, %d, %d, %d\n' % (k, kmin[k][0], kmin[k][1], kmin[k][2]))



target = '20200603'
converToTrend(target, little=10)
converToTrend(target, ext='小台', big=80, little=40)
