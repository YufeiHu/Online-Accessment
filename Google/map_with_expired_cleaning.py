# http://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=444336&highlight=%B9%B7%2B%C3%E6


from heapq import heappop, heappush


class lightMap(object):

    def __init__(self):
        self.memo = dict()
        self.records = list()


    def get(self, key, curTime):
        # update memo and records
        self.cleanUp(curTime)

        # return result
        return self.memo.get(key, None)


    def put(self, key, value, timing, curTime):
        # update memo and records
        self.cleanUp(curTime)

        # delete the record if necessary
        if key in self.memo:
            for i, record in enumerate(self.records):
                if record[0] == key:
                    del self.records[i]
                    break

        # update the records and memo
        heappush(self.records, (key, curTime + timing))
        self.memo[key] = value


    def cleanUp(self, curTime):
        while self.records:
            if self.records[0][1] <= curTime:
                key = self.records[0][0]
                del self.memo[key]
                heappop(self.records)
            else:
                break



myLightMap = lightMap()
myLightMap.put(key=1, value=2, timing=4, curTime=0)
print(myLightMap.get(key=1, curTime=2))
myLightMap.put(key=3, value=9, timing=8, curTime=2)
print(myLightMap.get(key=1, curTime=3))
myLightMap.put(key=1, value=5, timing=2.5, curTime=3)
print(myLightMap.get(key=1, curTime=5))