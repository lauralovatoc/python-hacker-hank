# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
from datetime import date

m, d, y = map(int, input().split())

result = calendar.day_name[calendar.weekday(y, m, d)]
result = result.upper()

print(result)