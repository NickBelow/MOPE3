import numpy as np

array = np.array([[20, -20, 70, 225, 248, 256],
                  [20, 40, 80, 230, 259, 243],
                  [70, -20, 80, 241, 244, 232],
                  [70, 40, 70, 240, 239, 246]])
x1min = 20
x1max = 70
x2min = -20
x2max = 40
x3min = 70
x3max = 80
ymin = 223.3
ymax = 263.3

def average_y(i):
    total = 0
    for j in range(3, 6):
        total += array[i][j]
    return total/3

def average_x(i):
    total = 0
    for j in range(0, 4):
        total += array[j][i]
    return total/4

y1_average = average_y(0)
y2_average = average_y(1)
y3_average = average_y(2)
y4_average = average_y(3)
#cредние факторы
mx1 = average_x(0)
mx2 = average_x(1)
mx3 = average_x(2)
my = np.sum(np.array([y1_average,y2_average,y3_average,y4_average]))/4
a1 = (array[0][0]*y1_average + array[1][0] * y2_average + array[2][0] * y3_average + array[3][0] * y4_average)/4
a2 = (array[0][1]*y1_average + array[1][1] * y2_average + array[2][1] * y3_average + array[3][1] * y4_average)/4
a3 = (array[0][2]*y1_average + array[1][2] * y2_average + array[2][2] * y3_average + array[3][2] * y4_average)/4
a11 = (array[0][0] * array[0][0] + array[1][0] * array[1][0] + array[2][0] * array[2][0] + array[3][0] * array[3][0])/4
a22 = (array[0][1] * array[0][1] + array[1][1] * array[1][1] + array[2][1] * array[2][1] + array[3][1] * array[3][1])/4
a33 = (array[0][2] * array[0][2] + array[1][2] * array[1][2] + array[2][2] * array[2][2] + array[3][2] * array[3][2])/4
a12 = a21 = (array[0][0] * array[0][1] + array[1][0] * array[1][1] + array[2][0] * array[2][1] + array[3][0] * array[3][1])/4
a13 = a31 = (array[0][0] * array[0][2] + array[1][0] * array[1][2] + array[2][0] * array[2][2] + array[3][0] * array[3][2])/4
a32 = a23 = (array[0][1] * array[0][2] + array[1][1] * array[1][2] + array[2][1] * array[2][2] + array[3][1] * array[3][2])/4

b0 = np.linalg.det(np.array([
    [my, mx1, mx2, mx3],
    [a1, a11, a12, a13],
    [a2, a12, a22, a32],
    [a3, a13, a23, a33]]))/np.linalg.det(np.array([
    [1, mx1, mx2, mx3],
    [mx1, a11, a12,a13],
    [mx2, a12, a22, a32],
    [mx3, a13, a23, a33]]))

b1 = np.linalg.det(np.array([
    [1, my, mx2, mx3],
    [mx1, a1, a12, a13],
    [mx2, a2, a22, a32],
    [mx3, a3, a23, a33]]))/np.linalg.det(np.array([
    [1, mx1, mx2, mx3],
    [mx1, a11, a12,a13],
    [mx2, a12, a22, a32],
    [mx3, a13, a23, a33]]))

b2 = np.linalg.det(np.array([
    [1, mx1, my, mx3],
    [mx1, a11, a1, a13],
    [mx2, a12, a2, a32],
    [mx3, a13, a3, a33]]))/np.linalg.det(np.array([
    [1, mx1, mx2, mx3],
    [mx1, a11, a12,a13],
    [mx2, a12, a22, a32],
    [mx3, a13, a23, a33]]))

b3 = np.linalg.det(np.array([
    [1, mx1, mx2, my],
    [mx1, a11, a12, a1],
    [mx2, a12, a22, a2],
    [mx3, a13, a23, a3]]))/np.linalg.det(np.array([
    [1, mx1, mx2, mx3],
    [mx1, a11, a12, a13],
    [mx2, a12, a22, a32],
    [mx3, a13, a23, a33]]))

print(f"equation\ty = {round(b0,2)} + {round(b1,4)} * x1 + {round(b2,2)} * x2 + {round(b3,2)} * x3")

#Критерий Кохрена
def dispersion(line, average):
    total =0
    for i in range(3,6):
        total += (array[line][i]-average)**2
    return total/3
s_y1 = dispersion(0, y1_average)
s_y2 = dispersion(1, y2_average)
s_y3 = dispersion(2, y3_average)
s_y4 = dispersion(3, y4_average)
Gp = np.max(np.array([s_y1, s_y2, s_y3, s_y4]))/np.sum(np.array([s_y1, s_y2, s_y3, s_y4]))
N = 4
m =3 #кол-во повторений
f1 = 2  #f1 = m-1
f2 = 4  #f2 = N
print(f"Kohren \tGp({round(Gp,4)}) < Gт(0.7679) => the number of repetitions is adequate")
naturalArray = np.array([[1, -1, -1, -1, 15,  18, 16],
                  [1, -1, 1, 1, 10, 19, 13],
                  [1, 1, -1, 1, 11, 14, 12],
                  [1, 1, 1, -1, 16, 19, 16]])
# Стьюдент
S_B = np.sum(np.array([s_y1, s_y2, s_y3, s_y4]))/N
S_bb = S_B / N / m
S_b = np.sqrt(S_bb)
def studentKoeff(column):
    total = 0
    for i in range(0, 4):
        total += eval("naturalArray[i][column] * y"+str(i+1)+"_average")
    return total/4
b_0 = studentKoeff(0)
b_1 = studentKoeff(1)
b_2 = studentKoeff(2)
b_3 = studentKoeff(3)

t0 = np.abs(b_0)/S_b
t1 = np.abs(b_1)/S_b
t2 = np.abs(b_2)/S_b
t3 = np.abs(b_3)/S_b
tt = 2.306
f3 = f1 * f2
print(f"Student\todds: t0 = {round(t0,2)} t1={round(t1,2)} t2={round(t2,2)} t3={round(t3,2)} tt={round(tt,2)} \t=> b1 and b2 and b3 can be omitted")
print(f"equation\ty = {round(b0,2)}")
Y1 = b0 + b3 * array[0][2]
Y2 = b0 + b3 * array[1][2]
Y3 = b0 + b3 * array[2][2]
Y4 = b0 + b3 * array[3][2]
#Фишера
d = 2 #кол-во новых значимых коэффицентов
f4 = N - d
adequateDispersion = (m/(N-d)) * ((Y1-y1_average)**2 + (Y2-y2_average)**2 + (Y3-y3_average)**2 + (Y4-y4_average)**2)
Fp = adequateDispersion/S_bb
Ft = 4.5
print(f"Fisher\tFp({round(Fp,2)}) > Ft({round(Ft,2)}) => new equation is not adequate if accurate equals 0.95")