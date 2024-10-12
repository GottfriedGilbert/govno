
pi = 3.14159265358979323846264338
e = 2.71828182845904523536
gamma = 0.57721566490153286060
phi = 1.61803398874989484820

def roud(a): # Не нужно
	for i in range(len(a)):
		for j in range(len(a[i])):
			a[i][j] = round(a[i][j], 4)
	return a

def intfloat(x): # Не нужно
	if x % 1 == 0:
		x = int(x)
	return x

def dowith(a): # Не нужно
	for i in range(len(a)):
		for j in range(len(a[i])):
			a[i][j] = intfloat(a[i][j])
	return a

def mget(): # Получение матрицы от пользователя
	print("Элементы вводить через пробел!")
	t = int(input("Кол-во строк: "))
	if t == -1:
		return False
	r = []

	for _ in range(t):
		l = list(map(float, input().split()))
		r.append(l)
	r = dowith(r)
	return r

def ooooo(a, b): # Не нужно
	c = 0
	for i in range(len(a)):	
		c += a[i] * b[i]
	return c

def mprint(a): # Вывод матрицы...
	t = 0
	b = deepcopy(a)
	if b == False:
		return False

	for i in range(len(b)):
		for j in range(len(b[i])):
			if t < len(str(b[i][j])):
				t = len(str(b[i][j]))

	for i in range(len(b)):
		for j in range(len(b[i])):
			b[i][j] = str(b[i][j])
			p = (t - len(b[i][j])) // 2
			b[i][j] = (t - len(b[i][j]) - p) * " " + b[i][j] + p * " "

	for i in range(len(b)):
		o="[ "
		for j in range(len(b[i])):
			o+=b[i][j]
			o+=" "
		o+="]"
		print(o)


def mT(a): #Транспонирование матрицы
	b = [[0 for m in range(len(a))] for n in range(len(a[0]))]
	for i in range(len(a)):
		for j in range(len(a[i])):
			b[j][i] = a[i][j]
	b = roud(dowith(b))
	return b


def madd(a, b): #Сумма матриц
	c = deepcopy(a)
	for i in range(len(a)):
		for j in range(len(b[i])):
			c[i][j] = a[i][j]+b[i][j]
	c = roud(dowith(c))
	return c


def msub(a, b): #Вычитание матриц
	c = deepcopy(a)
	for i in range(len(a)):
		for j in range(len(b[i])):
			c[i][j] = a[i][j] - b[i][j]
	c = roud(dowith(c))
	return c


def mmul(a, b): #Умножение матриц
	c = deepcopy(a)
	d = deepcopy(b)
	d = T(d)
	e = [[0 for m in range(len(c))] for n in range(len(d))]

	for i in range(len(c)):
		for j in range(len(d)):
			e[i][j] = ooooo(c[i], d[j])
	e = roud(dowith(e))
	return e


def mmulc(b,C): #Умножение на константу
	a = deepcopy(b)
	for i in range(len(a)):
		for j in range(len(a[i])):
			a[i][j] = a[i][j] * C
	a = roud(dowith(a))
	return a


def M(b, i, j): #Не нужно
	a = deepcopy(b)
	for t in range(len(a)):
		a[t].pop(j)
	a.pop(i)
	return a


def mdet(a): #Определитель
	n = 0
	if len(a) != len(a[0]):
		return False

	if len(a) == 2:
		return a[0][0] * a[1][1] - a[0][1] * a[1][0]

	elif len(a) > 2:
		for j in range(len(a[0])):
			n += (-1) ** (j) * a[0][j] * det(M(a, 0, j))
	return round(n, 6)

def something(a): #Не нужно
	g = deepcopy(a)
	for i in range(len(a)):
		for j in range(len(a[i])):
			g[i][j] = (-1) ** (i + j) * det(M(a, i, j))
	return g


def mrev(a): #Обратная матрица
	if len(a) == 2:
		d = [[a[1][1], -a[0][1]], [-a[1][0], a[0][0]]]
		return dowith(multipc(d, 1 / (det(a))))
	return dowith(multipc(T(something(a)), 1 / (det(a)))) if det(a) != 0 else False


def quadsolve(a,b,c):
	return [(-b + (b ** 2 - 4 * a * c) ** 0.5) / 2, (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2]


def sort(b): #Не нужно
    a = deepcopy(b)
    for _ in range(len(a)):
        for i in range(len(a)-1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    return a


def mid(a): #Медиана
    d = sort(a)
    l = len(d)
    if l % 2 == 1:
        return d[l // 2]
    return (d[l//2]+d[l//2-1])/2


def G(a): #Среднее геометрическое
    h = 1
    for i in a:
        h *= i
    return h ** (1 / len(a))


def H(a): #Среднее гармоническое
    h = 0
    for i in a:
        h += 1 / i
    h = len(a)/h
    return h


def sigma(a): #Среднее квадратическое
    h = 0
    for i in a:
        h += i ** 2
    return (h / len(a)) ** 0.5


def ln(a): #Натуральный логарифм
    return math.log(a)


def lg(a): #Десятичный логарифм
    return math.log(a) / math.log(10)


def log(a, b): #Логарифм
 return math.log(b) / math.log(a)


def AML(a): #Среднее логарифмическое
    h = 0
    for i in a:
        h += log(i)
    return h / len(a)


def gcdtwo(a, b): #Не нужно
    while b:
        a, b = b, a % b
    return a


def lcm(nums): #НОК
    if not nums:
        return None

    res = nums[0]
    for num in nums[1:]:
        nres = abs(num * res // gcdtwo(abs(num), abs(res)))
        res = nres
    return res


def gcd(nums): #НОД
    gon = gcdtwo(nums[0], nums[1])
    for num in nums[2:]:
        gon = gcdtwo(gon, num)
    return gon


def sin(x):
	return math.sin(x)


def cos(x):
	return math.cos(x)


def tan(x):
	return math.tan(x)


def arcsin(x):
	return math.asin(x)


def arccos(x):
	return math.acos(x)


def arctan(x):
	return math.atan(x)


def sinh(x):
	return math.sinh(x)


def cosh(x):
	return math.cosh(x)


def tanh(x):
	return math.tanh(x)


def arcsinh(x):
	return math.asinh(x)


def arccosh(x):
	return math.acosh(x)


def arctanh(x):
	return math.atanh(x)


def factorial(a):
    i = 1
    for h in range(1, a + 1):
        i *= h
    return i


def subfactorial(n):
    a = 1
    for i in range(1, n + 1):
        a += (-1) ** i / factorial(i)
    a *= factorial(n)
    return a


def arithm_mean(array): # среднее арифметическое
    res = 0
    for num in array:
        res += num
    res /= len(array)
    return res


def sqrtn(a, n): # корень степени n
    return a ** 1 / n


def sign(n): # знак числа n
    if n > 0:
        return 1
    elif n < 0:
        return -1
    else:
        return 0


def isprime(n): # проверка на простоту числа n
    fl = True
    for i in range(2, sqrt(n)):
        if n % i != 0:
            fl = False
            break
    if fl:
        return True
    return False


def solvelin(a, b): # решает линейные уравнения ах+b=0
    return -b / a if a != 0 else 0


def hyperfactorial(a):
	n = 1
	for i in range(1, a + 1):
		n *= i ** i
	return n


def primorial(a):
	n = 1
	for i in range(1, a + 1):
		if isprime(i):
			n *= i
	return n


def nfactorial(a, n):
	k = 1
	for i in range(a, 0, -n):
		k *= i
	return k


def isvprime(a, b):
	return gcdtwo(a, b) == 1


def eulerf(a):
	u = [i for i in range(1, a)]
	for x in u:
		if isvprime(a, x):
			u.remove(x)
	return len(u)


def Gammaf(x):
	return math.gamma(x)


def Betaf(x,y):
	return Gammaf(x) * Gammaf(y) / Gammaf(x * y) if Gammaf(x * y) != 0 else 0


def solve(a):
	return eval(a)


def zabs(a,b):
	return (a * 2 + b ** 2) ** 0.5


def zarg(a,b):
	if a > 0 and b >= 0:
		return arctan(b / a)

	elif a < 0 and b >= 0:
		return pi - arctan(b / a)

	elif a < 0 and b < 0:
		return pi + arctan(b / a)

	elif a > 0 and b < 0:
		return 2 *pi - arctan(b / a)

	elif a == 0 and b > 0:
		return pi / 2

	elif a == 0 and b < 0:
		return 3 * pi / 2

	else:
		return 0


def degrees(a):
	return math.degrees(a)


def radians(a):
	return math.radians(a)


def Re(a, b):
	return a


def Im(a, b):
	return b * (-1) ** 0.5


def zexp(a,b):
	s = str(zabs(a, b)) + "e^(i" + str(zarg(a, b)) + ")"
	return s


def ztrig(a,b):
	s = str(zabs(a, b)) + "(cos(" + str(zarg(a, b)) + ")+isin(" + str(zarg(a, b)) + "))"
	return s
    