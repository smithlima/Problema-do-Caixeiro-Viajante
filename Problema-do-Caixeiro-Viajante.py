import sys
import copy


n = int(input())
matrix = []
for j in range(n):
	matrix.append([int(i) for i in input().split()])

g = {}
p = []

def main():
    for x in range(1, n):
        g[x + 1, ()] = matrix[x][0]
    
    cost = get_minimum(1,range(2,n+1))
    
    solution = p.pop()
    a = [1]
    a.append(solution[1][0])

    for x in range(n - 2):
        for new_solution in p:
            if tuple(solution[1]) == new_solution[0]:
                solution = new_solution
                a.append(solution[1][0])
                break
    a.append(1)
   
    
    print("Valor: ",cost)
    print("Circuito: ", a)
    
    return

def get_minimum(k, a):
    if (k, a) in g:
        # Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
        return g[k, a]

    values = []
    all_min = []
    for j in a:
        set_a = copy.deepcopy(list(a))
        set_a.remove(j)
        all_min.append([j, tuple(set_a)])
        result = get_minimum(j, tuple(set_a))
        values.append(matrix[k-1][j-1] + result)

    # get minimun value from set as optimal solution for
    g[k, a] = min(values)
    p.append(((k, a), all_min[values.index(g[k, a])]))

    return g[k, a]


if __name__ == '__main__':
    main()
sys.exit(0) 
