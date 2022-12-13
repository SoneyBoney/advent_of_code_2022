
# def cpu_sim(instruction, state):
#     pass

# with open('input.txt','r') as f:
#     data = f.read().split('\n')[:-1]

#     X = 1
#     cycles = 1
#     total = 0
#     for line in data:
#         if line == 'noop':
#             if (cycles-20)%40 == 0 and cycles <= 220:
#                 print(cycles)
#                 total += X * cycles
#             cycles += 1
#         elif 'addx' in line:
#             if (cycles-20)%40 == 0 and cycles <= 220:
#                 print(cycles)
#                 total += X * cycles
#             cycles += 1
#             if (cycles-20)%40 == 0 and cycles <= 220:
#                 print(cycles)
#                 total += X * cycles
#             cycles += 1

#             arg = line.split(' ')[1]
#             X += int(arg)
        

#     print(total)
from pprint import pprint

with open('input.txt','r') as f:
    data = f.read().split('\n')[:-1]

    X = 1
    cycles = 1
    total = 0
    CRT = []
    temp_crt = []
    for line in data:
        if line == 'noop':
            if len(temp_crt) >= 40:
                CRT.append(temp_crt)
                temp_crt = []
            if abs(X-len(temp_crt)) <= 1:
                temp_crt.append('#')
            else:
                temp_crt.append('.')
            cycles += 1
        elif 'addx' in line:
            if len(temp_crt) >= 40:
                CRT.append(temp_crt)
                temp_crt = []
            if abs(X-len(temp_crt)) <= 1:
                temp_crt.append('#')
            else:
                temp_crt.append('.')
            cycles += 1
            if len(temp_crt) >= 40:
                CRT.append(temp_crt)
                temp_crt = []
            if abs(X-len(temp_crt)) <= 1:
                temp_crt.append('#')
            else:
                temp_crt.append('.')
            
            arg = line.split(' ')[1]
            X += int(arg)
            cycles += 1
    CRT.append(temp_crt)

    print(cycles)
    
    print('\n'.join([''.join(x) for x in CRT]))