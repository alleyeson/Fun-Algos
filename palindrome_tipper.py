
# get min denomination to start 
# check is len string odd or even
## if odd then take decimal and number next to it as middle then add until palindrome 
## else add until decimal 

#alternatively 
'''  
get position of decimal is any
get length before and after decimal 
create new number w/o decimal (if none then should just be original number)
add 1 until new number is palindrome 
put decimal is proper place 
return total ones added (if to numbers before decimal then account for it)
'''
def check_num_is_palindrome(num): 
    str_num = str(num)
    for i in range(0,len(str_num)): 
        if str_num[i] != str_num[~i]: 
            return False 
    return True

def get_palidrome_tip_f(num,min_tip = 7): 
    old_num = num
    num = num+min_tip
    if check_num_is_palindrome(num) == True: 
        return 0
    
    num_str = str(num)
    num_wo_decimal = '' 
    count_number_b4_decimal = 0 
    count_number_after_decimal = 0 
    decimal_position = 0

    is_dec_point_seen = 0 
    n = len(num_str)

    for i in range(n): 
        if num_str[i] == '.':
            is_dec_point_seen = 1
            decimal_position = i

        if is_dec_point_seen == 1: 
            count_number_after_decimal += 1 
        else: 
            count_number_b4_decimal+=1 
        if num_str[i] != '.': 
            num_wo_decimal = num_wo_decimal + num_str[i]
    
    dum_num = int(num_wo_decimal)
    while check_num_is_palindrome(dum_num) == False:
        dum_num += 1

    str_num_new = str(dum_num)
    new_num = ''
    
    # now check if number grew beyon orginal size, if so, decimal place should shift right by difference in len(dum_num) - len(num)
## add smallest smallest_denom_str to end until 
    if len(str_num_new) > n: 
        decimal_position += len(str_num_new) - n

    for i in range(0, len(str_num_new)): 
        if i == decimal_position:
            new_num = new_num + '.'
        new_num = new_num + str_num_new[i]

    new_num = float(new_num)
    tip = new_num - old_num 

    return round(tip,count_number_after_decimal)

if __name__ == '__main__': 
    num = 3.1143 
    tip_till_palindrome = get_palidrome_tip_f(num)

    print('Tip for become palindrome: ' + str(tip_till_palindrome))
    print('New total: ' + str(tip_till_palindrome + num))
