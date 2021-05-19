from queue import PriorityQueue
class Solution:
    def scheduleCourse(self,courses):
        q= PriorityQueue()
        # courses.sort()
        courses.sort(key=lambda x: x[1])
        time = 0
        cnt = 0
        size = 0
        # print(courses)
        for k in courses:
            if time + k[0] <= k[1]:
                time += k[0]
                q.put(-1* k[0])
                size += 1
                # print(k," #### put   ####", time)
            else:
                if size > 0:
                    w = q.get()
                    # print(w, k)
                    if -1 * w > k[0]:
                        time += k[0] + w
                        q.put(-1 * k[0])
                        # print(time)
                    else:
                        q.put(w)
        return size

#
#https://leetcode.com/problems/course-schedule/
#