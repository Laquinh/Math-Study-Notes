
def to_base(num, base):
    if num < base:
        return str(num)
    else:
        return to_base(num // base, base) + str(num % base)

def get_weights(q, n):
    numberOfWords = q**(n-1)
    weights = [0] * (n+1)

    for i in range(numberOfWords):
        prefix = to_base(i, q).zfill(n-1)

        sum = 0
        for j in range(n-1):
            sum += int(prefix[j])

        # Add parity bit
        word = prefix + str(sum % q)

        #number of non-null bits
        weight = n - word.count('0')
        weights[weight] += 1 

        if(weight == n):
            #print("w(" + word[:-1] + "-" + word[-1] + ") = " + str(weight) + ", " + str(sum))
            pass

    return weights

#get_weights(7, 5)

for q in range (2, 6):
    for n in range(2, 10):
        weights = get_weights(q, n)

        print("q=" + str(q) + ", n=" + str(n) + ": " + str(weights))
    
    print()