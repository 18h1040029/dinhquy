n=int(input("nhap so phan tu của chuoi="))
b=[]
for i in range(0,n):
    q=int(input("nhap so phan tu thu %d " %(i)))
    b.append(q)
print("chuoi da nhap: ")
print(b)
print("chuoi phan tu dao nguoc: ")
print(list(reversed(b)))