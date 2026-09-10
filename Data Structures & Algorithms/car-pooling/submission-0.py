class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip_heap = []
        for kitne, kaha_se, kaha_ko in trips:
            trip_heap.append([kaha_se, kaha_ko, kitne])

        heapq.heapify(trip_heap)
        dest = []
        cur_loc = trip_heap[0][0]
        cur_cap = 0

        while trip_heap or dest:
            # drop passengers
            while dest and cur_cap != 0 and cur_loc == dest[0][0]:
                _, kitne = heapq.heappop(dest)
                cur_cap -= kitne
            
            # pick passengers
            while trip_heap and cur_loc == trip_heap[0][0]:
                _, kaha_ko, kitne = heapq.heappop(trip_heap)
                cur_cap += kitne
                if cur_cap > capacity:
                    return False

                heapq.heappush(dest, [kaha_ko, kitne])

            cur_loc += 1

            # print(trip_heap)
            # print(dest)

        return True