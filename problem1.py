import sys 

#Running in Circles
def main ():
    T = int(sys.stdin.readline().rstrip())
    case = 0
    while (case < T):
        case += 1
        L, N = sys.stdin.readline().rstrip().split(' ')
        A = 0
        total = 0
        direction = ['C']
        for i in range(int(N)):
            D, C = sys.stdin.readline().rstrip().split(' ')
            prev = direction.pop()

            if (C == prev):
                A += int(D)
            else:
                A = abs(A - int(D))
          
            if (A >= int(L)):
                total += A // int(L)
                A = A % int(L)

            direction.append(C)
           
        print(f'Case #{case}: {total}')

if __name__ == '__main__':
    main()
