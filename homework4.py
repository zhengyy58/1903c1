import sqlite3

a = sqlite3.connect("1903c.db")
b= a.cursor()
# c =b.execute("create table goods(id integer primary key autoincrement,"
#              "gname char(5) not null,"
#              "price integer ,"
#              "num integer )")

class Market():
    def menu(self):
        print("="*20)
        print("超市购物系统")
        print("1 进货")
        print("2 展示商品")
        print("3 搜索商品")
        print("4 购买商品")
        print("5 退出系统")
        print("="*20)

    def adds(self):
        m1 = input("请输入商品名称：")
        m2 = int(input("请输入商品价格："))
        m3 = int(input("请输入商品数量："))
        b.execute("insert into goods(gname,price,num) values (?,?,?)",(m1,m2,m3))
        a.commit()
    def info(self):
        e = b.execute("select * from goods")
        print(e.fetchall())
        a.commit()
    def buy(self):
        gid = int(input("请输入要购买的商品id："))
        ber = int(input("请输入要购买的商品数量："))
        f = b.execute("select num from goods where id=?",(gid,))
        g = f.fetchone()[0]
        if ber<g:
            gnum = g - ber
            b.execute("update goods set num=? where id=?",(gnum,gid))
        elif ber == g:
            b.execute("delete from goods where id=?",(gid,))
        else:
            print("库存不足")
        a.commit()

    def search(self):
        gid = int(input("请输入要查找的商品id："))
        ff = b.execute("select * from goods where id=?",(gid,))
        print(ff.fetchone())
        a.commit()

    def exit(self):
        print("退出系统")
        exit()
        a.close()

market = Market()
market.menu()

while True:
    choice = int(input("请输入要选择的功能："))
    if choice == 1:
        market.adds()
    elif choice == 2:
        market.info()
    elif choice == 3:
        market.buy()
    elif choice == 4:
        market.search()
    elif choice == 5:
        market.exit()
    else:
        print("输入有误")





