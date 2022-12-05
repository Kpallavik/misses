####                            ####
# Title:            Looking for Fermat's Last Theorem Near Misses
# Filename :        misses.py
# Name:             Pallavi Karengala,Ranjith Reddy Pingli
# Email:            PallaviKarengala@lewisu.edu,ranjithreddypingli@lewisu.edu
# Course & Sections:Software Engineering- 005 FA22-CPSC-60500-005
# Date:             Nov 19 2022
# Explanation:      search for near misses of the form (x, y, z, n, k) with
#                   the formula x^n + y^n = z^n, where x, y, z, n, k are
#                   positive integers, 2< n <12, 10 <= x <= k, 10 <= y <= k
# compiled on:      Python 3.10
####                            ####

def near_misses(n, k):
    # Calculate near misses with the Fermat's Last Theorem formula x^n + y^n = z^n and dsiplay results
    
    f = False # for checking the first iteration or not
    relative_miss = 0
    for x in range(10, k): # Outer loop for first variable x of function x^n + y^n = z^n
        for y in range(10, k): # loop for y
            xysum_pow = pow(x, n) + pow(y, n) # calculate (x^n + y^n) using python's built in pow method
            z = int(pow(xysum_pow, 1/n))
            z_pow = pow(z, n)
            z1_pow = pow(z+1, n)
            miss = min( xysum_pow - z_pow, z1_pow - xysum_pow)
            relative_miss_temp = miss / xysum_pow
            if f==False:
                relative_miss = relative_miss_temp # for the first iteration get the relative miss
                print("\nx: {}   |   y: {}   |   z: {}    |   Miss: {}   |   Relative Miss: {}%".format(x, y, z, miss, round(relative_miss*100,2)))
                f = True
            else:
                if relative_miss_temp < relative_miss: 
                    relative_miss = relative_miss_temp # get the minimum relative miss
                    print("x: {}   |   y: {}   |   z: {}    |   Miss: {}   |   Relative Miss: {}%".format(x, y, z, miss, round(relative_miss*100,2)))
    print("\n#### Final Near Miss Result: ####\n")
    # print the final 
    print("x: {}   |   y: {}   |   z: {}    |   Miss: {}   |   Relative Miss: {}%".format(x, y, z, miss, round(relative_miss*100,2)))
    
def main():
    # Get the input of n(power) and k(limit) from user then call the calculate function

    n = int(input("Exponent value(n): "))
    while n<3 or n>11:
        # check if n is bigger than 2
        n = int(input("Exponent value should be bigger than '2' and smaller than '12'. New Exponent value(n): "))
    k = int(input("Limit of x and y(k): "))
    while k<11:
        # check if k is bigger than 10
        k = int(input("Limit value should be bigger than '10'. New Exponent value(k): "))
    near_misses(n, k)
        
if __name__ == "__main__":
    main()
    # continue calculate misses till exit
    while(True):
        ch = input("\nCalculate another misses or Exit[y/n]: ")
        if (ch == 'y' or ch == 'Y'):
            main()
        else:
            exit()
