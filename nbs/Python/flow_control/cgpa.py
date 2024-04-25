# Assume 4 course units
# 1. Math - A
# 2. Science - B
# 3. SST - B
# 4. English - C


def calculate_CGPA(GPs_list, CUs_list):
    length = len(GPs_list)
    product_sum = 0

    for item in range(length):
        product_sum += GPs_list[item] * CUs_list[item]

    CUs_sum = sum(CUs_list)

    CGPA = product_sum / CUs_sum

    return CGPA

calculate_CGPA(4, 5)










 # other factors constant
