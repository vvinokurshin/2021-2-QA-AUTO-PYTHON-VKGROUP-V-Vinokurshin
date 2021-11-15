import sys

def in_array(element, array):
    for i in range(len(array)):
        if array[i] == element:
            return i

    return -1

file_log_name = sys.argv[1]

with open('res_python.txt', 'w') as f_out:
    f_out.write('Общее количество запросов:\n')
    count = sum(1 for line in open(file_log_name, 'r')) 
    f_out.write(str(count))


    f_out.write('\n\nКоличество запросов каждого типа:\n')
    methods = []
    count_methods = []

    with open(file_log_name, 'r') as f_in:
        for i in range(count):
            line = f_in.readline().split()[5:6][0].strip("\"")
            
            if len(line) >= 10:
                continue

            ind = in_array(line, methods)
            
            if ind >= 0:
                count_methods[ind] += 1
            else:
                methods.append(line)
                count_methods.append(1)

    res = zip(count_methods, methods)
    sorted_res = sorted(res, key=lambda tup: tup[0])

    for i in range(len(methods)):
        f_out.write(str(sorted_res[i][0]) + ' ' + sorted_res[i][1] + '\n')  

    
    f_out.write('\nТоп 10 самых частых запросов:\n')

    url = []
    count_url = []

    with open(file_log_name, 'r') as f_in:
        for i in range(count):
            line = f_in.readline().split()[6:7][0]

            ind = in_array(line, url)
            
            if ind >= 0:
                count_url[ind] += 1
            else:
                url.append(line)
                count_url.append(1)

    res = zip(count_url, url)
    sorted_res = sorted(res, key=lambda tup: tup[0], reverse=True)

    for i in range(10):
        f_out.write(str(sorted_res[i][0]) + ' ' + str(sorted_res[i][1]) + '\n')


    f_out.write('\nТоп 5 самых больших по размеру запросов, которые завершились клиентской (4ХХ) ошибкой:\n')
    
    ip = []
    url = []
    code = []
    size = []

    with open(file_log_name, 'r') as f_in:
        for i in range(count):
            line = f_in.readline().split()

            if int(line[8]) // 100 == 4:
                ip.append(line[0])
                url.append(line[6])
                code.append(int(line[8]))
                size.append(int(line[9]))

    res = zip(ip, code, size, url)
    sorted_res = sorted(res, key=lambda tup: tup[2], reverse=True)

    for i in range(5):
        f_out.write(str(sorted_res[i][0]) + ' ' + str(sorted_res[i][1]) + ' ' + str(sorted_res[i][2]) + ' ' + str(sorted_res[i][3]) + '\n')


    f_out.write('\nТоп 5 пользователей по количеству запросов, которые завершились серверной (5ХХ) ошибкой\n')

    ip = []
    count_requests = []

    with open(file_log_name, 'r') as f_in:
        for i in range(count):
            line = f_in.readline().split()

            if int(line[8]) // 100 == 5:
                ind = in_array(line[0], ip)
            
                if ind >= 0:
                    count_requests[ind] += 1
                else:
                    ip.append(line[0])
                    count_requests.append(1)

    res = zip(count_requests, ip)
    sorted_res = sorted(res, key=lambda tup: tup[0], reverse=True)

    for i in range(5):
        f_out.write(str(sorted_res[i][0]) + ' ' + str(sorted_res[i][1]) + '\n')
