# for(int i = 0; i < 5; i++) { DO CRAP }
#
# int i = 0;
# while(i < 5) {
#    DO CRAP
#    i++;
# }

cnt = 1
while cnt <= 20:
    #cnt += 1
    #cnt = cnt + 1
    print(cnt)
    cnt += 1

cnt = 20
while cnt >= 0:
    #cnt += 1
    #cnt = cnt + 1
    if (cnt > 0):
        print(cnt)
    else:
        print('IGNITION!')
        print('LIFT OFF!!!')
    cnt -= 1

for x in range(10):
    print(x)

for y in 'hello':
    print(y)
    