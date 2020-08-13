from datetime import datetime as dt
import calc


print("Hello world")
assert 5 == calc.add(2, 3)

start_date = dt.today()

print("goodbye world ", start_date.strftime("%c"))