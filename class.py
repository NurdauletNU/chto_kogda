a=[
   {"name":"Zhibek", "age":25, "sex":"woman"},
   {"name":"Nurjan", "age":56, "sex":"men"},
   {"name":"Assem", "age":28, "sex":"woman"},
   {"name":"Rumiya", "age":2, "sex":"woman"}
   ]
print(sorted(a,key=lambda x: x["name"], reverse=True))




b={"name":"Nurik", "age":29.5}
def get_age(dict1):
    return dict1["age"]

print(get_age(b))
print(sorted(a,key=get_age))


peoples=[
         [2,5,8],
         [0,"joe",-5],
         [1,1,-1]
         ]

print(*sorted(peoples,key=lambda x:x[-1]))


a=["a","y", "e","i","o", "u"]
b="Python is awesome!"
count=0
for i in b:
    if i in a:
        count+=1
print(count)


def is_prime(file,cd=4):
    if file<cd:
        return False
    return True


x=is_prime(6)
print(x)

print()
print()



import sqlite3

def fetsc_data():
    conn=sqlite3.connect("database.db")
    c=conn.cursor()
    c.execute("SELECT name, FROM DATA")
    data=c.fetchall()
    conn.close()
    return data


