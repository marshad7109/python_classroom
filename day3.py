cpu_hours=int(input("enter number of cpu hours:"))
storage=int(input("enter storage in gb"))
data_transfer=int(input("enter data transfer in gb:"))
cpu_cost=cpu_hours*5
storage_cost=storage*2
data_transfer_cost=data_transfer*1
total_cost=cpu_cost+storage_cost+data_transfer_cost
print("total_amount:",total_cost)
if cpu_hours>100:
      print(total_cost+500)
else:
    print(total_cost)