import sys 

# Problem B: Magical Well Of Lilies
def main ():
    T = int(sys.stdin.readline().rstrip())
    case = 0
    while (case < T):
        case += 1
        L = int(sys.stdin.readline().rstrip())
        Toss = [-1]*(L+2)
        for i in range(0, L+1):
            Toss[i] = i
        for i in range(2, L+1):
            Toss[i+1] = min(Toss[i]+1, Toss[i+1])
            curr = Toss[i] + 4

            j = i*2
            while j <= L:
                curr += 2
                Toss[j] = min(Toss[j], curr)
                j += i
            
        print(f'Case #{case}: {Toss[L]}')
        

if __name__ == '__main__':
    main()
