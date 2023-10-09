Outlet1Sales = [10, 12,15,10]
Outlet2Sales = [5,8,3,6]
Outlet3Sales = [10,12,15,10]


# MAX = len(Outlet1Sales) + len(Outlet2Sales) + len(Outlet3Sales)
# overall = ['' for _ in range(MAX)]

# for i in range(len(Outlet1Sales)):
#     overall[i] = Outlet1Sales[i]
# for i in range(len(Outlet2Sales)):
#     overall[i+ len(Outlet1Sales)-1] = Outlet2Sales[i]

overall_1 = Outlet1Sales[0] + Outlet1Sales[1] + Outlet1Sales[2]

overall_2 = Outlet1Sales[3] + Outlet2Sales[0] + Outlet2Sales[1]

overall_3 = Outlet2Sales[2] + Outlet2Sales[3] + Outlet3Sales[0]

overall_4 = Outlet3Sales[1] + Outlet3Sales[2] + Outlet3Sales[3]

print(f'Total for quarter 1 {overall_1}')
print(f'Total for quarter 2 {overall_2}')
print(f'Total for quarter 3 {overall_3}')
print(f'Total for quarter 4 {overall_4}')