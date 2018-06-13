str = raw_input()
i = map(int,str.strip().split())
n = i[0]
m = i[1]
a = i[2]
b = i[3]

if n%m == 0:
    print(0)
else:
        if n > m:
            diff = abs(m - n)
            cost_b = diff*b
            cost_c = n * b
            new_m = (int(n/m) + 1)*m -n
            cost_a = new_m*a
            cost_a_1 = (n - int(n/m)*m) * b
        else:
            diff = abs(m - n)
            cost_b = diff*a
            cost_c = n * b
            new_m = (int(n/m) + 1)*m -n
            cost_a = new_m*a
            cost_a_1 = (n - int(n/m)*m) * b

        #print([cost_a, cost_a_1, cost_b, cost_c])
        print(min([cost_a,cost_a_1,cost_b,cost_c]))




