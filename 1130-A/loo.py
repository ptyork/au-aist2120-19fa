# C# while / for (mainly)
# also do-while / foreach
#
# if (CONDINTION IS TRUE) {
#     DO STUFF
# }
# while (CONDITION IS TRUE) {
#     DO STUFF
# }
# for (int i = 0; CONDITION IS TRUE; i++) {
#     DO STUFF
# }
# int i = 0;
# while (CONDITION IS TRUE) {
#     DO STUFF
#     i++;
# }
# foreach (int i in array) {
#     DO STUFF WITH is
# }

cnt = 0
while cnt < 10:
    print(cnt+1)
    #cnt = cnt + 1
    cnt += 1


cnt = 10
while cnt > 0:
    print(cnt)
    cnt -= 1
print('Blastoff!!')

cnt = 10
while cnt >= 0:
    if (cnt > 0):
        print(cnt)
    else:
        print('Blastoff!!')
    cnt -= 1


for x in range(10):
    print(x)

