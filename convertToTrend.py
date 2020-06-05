

# history,TX00,36458,20200603,94512,322000,1124600,1124700,1124700,7,0,+7


def convertToTrend(target, ext='大台'):
    last_minute = 0
    kmin = {}
    with open('data/' + ext + '/morning/' + target + '_trend.csv', 'w') as fout:
        with open('data/' + ext + '/morning/' + target + '_converted.csv') as f:
            l = f.readline()

            fout.write('\ufeff時間,大單,散單\n')

            for l in f.readlines():
                x = l.split(',')

                if x[4] < '08:45:00':
                    continue

                x[6] = str(float(x[6])/100)
                x[7] = str(float(x[7])/100)
                x[8] = str(float(x[8])/100)

                #print(x)
                if x[11][0] == '#':
                    vol = int(x[11][1:])
                    vol = vol * -1

                else:
                    vol = int(x[11])

                minute = x[4][0:5]


                if minute != last_minute:
                    kmin[minute + ':00'] = [0, 0, 0]
                    kmin[minute + ':10'] = [0, 0, 0]
                    kmin[minute + ':20'] = [0, 0, 0]
                    kmin[minute + ':30'] = [0, 0, 0]
                    kmin[minute + ':40'] = [0, 0, 0]
                    kmin[minute + ':50'] = [0, 0, 0]

                    last_minute = minute

                time = x[4][0:-1] + '0'

                print(time)

                if abs(vol) > big:
                    kmin[time][0] = kmin[time][0] + vol
                if abs(vol) < 5:
                    kmin[time][1] = kmin[time][1] + vol


        for k in sorted(kmin.keys()):
            fout.write('%s, %d, %d\n' % (k, kmin[k][0], kmin[k][1]))


target = '20200603'
big = 20

convertToTrend(target)
convertToTrend(target, ext='小台')
