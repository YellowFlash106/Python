def calculater(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f'taotal : ${final_price}')

calculater(tax_rate=0.08, price=100.0, discount=10)
# calculater(100, 0.08, 10)



def add(a,b):
    print(a+b)
res = add(5,6)

print(res)


def add_return(a,b):
    return a+b
result = add_return(5,6) + 2

print(result)


#Area 
def cal_area(w, h):
    area = w*h
    return area 

room_area = cal_area(10,12)
print(f'Room size:{room_area} sq ft');



#Double 
def double(n):
    return n * 2

result = double(5)
print(result) 
total = double(5) + double(3)

print(total) 

if double(7) > 10:
    print('Big number')




def simple():
    n = [ 1, 2, 3, 4]
    first = n[0]
    last = n[-1]
    return first, last
f , l = simple()

print(f)
print(l)
print(simple())
