

# history,TX00,36458,20200603,94512,322000,1124600,1124700,1124700,7,0,+7


def convertToTrend(target, ext='大台', big=20, little=5):
    last_minute = 0
    kmin = {}
    out_file = 'data/' + ext + '/morning/' + target + '_trend.csv'
    print('write: ' + out_file)
    with open(out_file, 'w') as fout:
        read_file = 'data/' + ext + '/morning/' + target + '_converted.csv'
        print('read: ' + read_file)
        with open(read_file) as f:
            l = f.readline()

            fout.write('\ufeff時間,大單,散單,指數\n')

            for l in f.readlines():
                x = l.split(',')

                if x[4] < '08:45:00':
                    continue


                #print(x)
                if x[11][0] == '#':
                    vol = 0
                    ext_vol = int(x[11][1:]) * -1
                else:
                    vol = int(x[11])
                    ext_vol = 0

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

                #print(time)

                if abs(vol) > big:
                    kmin[time][0] = kmin[time][0] + vol + ext_vol

                if abs(vol) < little:
                    kmin[time][1] = kmin[time][1] + vol

                kmin[time][2] = x[8]


        last_k = ''
        for k in sorted(kmin.keys()):
            if kmin[k][2] == 0:
                kmin[k] = kmin[last_k]
                print('set to last k: ' + last_k)
            fout.write('%s, %d, %d, %s\n' % (k, kmin[k][0], kmin[k][1], kmin[k][2]))
            last_k = k


target = '20200603'

convertToTrend(target, little=2)
convertToTrend(target, ext='小台', big=80, little=8)
