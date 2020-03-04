
# nc is " Income "
# mv(xx) is " VAT "

nc = int(input('กรุณาใส่จำนวนรายได้ของท่าน : '))

if nc <= 150000: #หมายถึงรายรับไม่ถึง 150000 จะได้รับการยกเว้นภาษี
    print("ละเส้นภาษี")

elif nc >= 150001 <= 300000:
    mvfive = nc * 0.05
    print("ภาษีของท่านคือ")
    print("===================")
    print(int(mvfive))
    print("===================")

elif nc >= 300001 <= 500000:
    mvten = nc * 0.10
    print("ภาษีของท่านคือ")
    print("===================")
    print(int(mvten))
    print("===================")

elif nc >= 500001 <= 750000:
    mvfifteen = nc * 0.15
    print("ภาษีของท่านคือ")
    print("===================")
    print(int(mvfifteen))
    print("===================")

elif nc >= 750001 <= 1000000:
    mvtw = nc * 0.20
    print("ภาษีของท่านคือ")
    print("===================")
    print(int(mvtw))
    print("===================")

elif nc >= 1000001 <= 200000:
    mvtwfive = nc * 0.25
    print("ภาษีของท่านคือ")
    print("===================")
    print(int(mvtwfive))
    print("===================")

elif nc >= 2000001 <= 5000000:
    mvth = nc * 0.30
    print("ภาษีของท่านคือ")
    print("===================")
    print(int(mvth))
    print("===================")

elif nc >= 5000001:
    mvthfive = nc * 0.35
    print("ภาษีของท่านคือ")
    print("===================")
    print(int(mvthfive))
    print("===================")