num_to_divsum_map = {}
##### SLOW AS A TRACTOR

for i in range(4,10000):
    sum_of_divisors = 0
    for j in range(1,(i/2)+1):
        if i % j == 0:
            sum_of_divisors+=j
    num_to_divsum_map[i] = sum_of_divisors


print type(num_to_divsum_map)
sum_of_amicables = 0

already_counted = []

for key,value in num_to_divsum_map.iteritems():
    for comp_key,comp_value in num_to_divsum_map.iteritems():
        if key == comp_value and comp_key == value and key != comp_key:
            sum_of_amicables = sum_of_amicables+key+comp_key
            print str(key)+' amicable with '+str(comp_key)
print sum_of_amicables/2
