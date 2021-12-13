from mysql.models import TotalCount, CountByType, \
    Top10_request_by_count, Top5_4XX_by_size, Top5_users_5XX_by_count


class MySQLBuilder():

    def __init__(self, client, filename):
        self.client = client
        self.requests = self.get_data(filename)

    def get_data(self, filename):
        with open(filename, 'r')as f:
            requests = f.readlines()
            requests = [request.split() for request in requests]
            return requests

    def total_count(self):
        row = TotalCount(count=len(self.requests))
        self.client.session.add(row)
        self.client.session.commit()
        return row

    def get_types_count(self):
        data = {}
        for request in self.requests:
            type = request[5][1:]
            
            if type in data:
                data[type] += 1
            elif (len(type) < 10):
                data[type] = 1

        return data

    def count_by_type(self):
        data = self.get_types_count()
    
        rows = []
        for type, count in data.items():
            row = CountByType(count=int(count), type=type)
            self.client.session.add(row)
            rows.append(row)

        self.client.session.commit()
        return rows


    def get_url_count(self):
        data = {}
        for request in self.requests:
            url = request[6]
            
            if url in data:
                data[url] += 1
            else:
                data[url] = 1

        return data

    def top10_request_by_count(self):
        data = self.get_url_count()

        rows = []
        for url, count in sorted(data.items(), key=lambda tup: tup[1], reverse=True)[:10]:
            row = Top10_request_by_count(count=int(count), url=url)
            self.client.session.add(row)
            rows.append(row)

        self.client.session.commit()
        return rows

    
    def get_requests(self):
        data = []
        for request in self.requests:
            ip = request[0]
            rc = int(request[8])
            size = request[9]
            url = request[6]

            if rc // 100 == 4:
                item = (ip, rc, int(size), url)
                data.append(item)
            
        return data

    def top5_4XX_by_size(self):
        data = self.get_requests()

        rows = []
        for ip, rc, size, url in sorted(data, key=lambda tup: tup[2], reverse=True)[:5]:
            row = Top5_4XX_by_size(url=url, rc=rc, size=size, ip=ip)
            self.client.session.add(row)
            rows.append(row)

        self.client.session.commit()
        return rows

    def get_users(self):
        data = {}
        for request in self.requests:
            ip = request[0]
            rc = int(request[8])
            
            if rc // 100 == 5:
                if ip in data:
                    data[ip] += 1
                else:
                    data[ip] = 1

        return data

    def top5_users_5XX_by_count(self):
        data = self.get_users()

        rows = []
        for ip, count in sorted(data.items(), key=lambda tup: tup[1], reverse=True)[:5]:
            row = Top5_users_5XX_by_count(ip=ip, count=count)
            self.client.session.add(row)
            rows.append(row)

        self.client.session.commit()
        return rows
