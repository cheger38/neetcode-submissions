class TimeMap:
    def __init__(self):
        self.data = dict()
        self.timestamps = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = dict()
            self.timestamps[key] = list()

        self.data[key][timestamp] = value
        self.timestamps[key].append(timestamp)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        if timestamp in self.data[key]:
            return self.data[key][timestamp]

        times = self.timestamps[key]
        lo = 0
        hi = len(times) - 1
        answer = None

        while lo <= hi:
            mid = (lo + hi) // 2

            if times[mid] <= timestamp:
                answer = times[mid]
                lo = mid + 1
            else:
                hi = mid - 1

        if answer:
            return self.data[key][answer]
        else:
            return ""