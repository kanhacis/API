from datetime import datetime, timedelta


start_date = datetime.now().date()
end_date = start_date + timedelta(days=30)

print(start_date, end_date) 

curr_date = datetime.now().date()
ans = end_date - curr_date
ans = str(ans).split(" ")[0]
print(ans)
