n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

k = int(input())
x = int(input())

def array(a,k,x):
    a.insert(k,x)
    return a
b = array(a, k,x)

for i in range(len(b)):
    print(b[i],end =" ")

# Tạo một folder mới tên new_local tại folder buoi_6
# B1: Truy cập tới folder buoi_6
# B2: mkdir <tên file>

# Tạo một cây thư mục
# mkdir <tên folder_1>/<tên folder_2>
# Chú ý: nếu folder chưa được tạo thì nó sẽ được tạo 

# cd .. quay lại một folder
# cd ../.. quay lại 2 folder


#del <tên folder>  được sử dụng để xóa folder