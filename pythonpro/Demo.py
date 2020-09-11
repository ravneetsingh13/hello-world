from datetime import datetime


class Solution:
    def solve(self, A, B, C):
        days = ['monday', 'tuesday', 'wednesday',
                'thursday', 'friday', 'saturday', 'sunday']
        date = str(A) + ' ' + str(B) + ' ' + str(C)
        day_num = datetime.strptime(date, '%d %m %Y').weekday()
        return days[day_num]


s1 = Solution()
print(s1.solve(3, 2, 2019))
