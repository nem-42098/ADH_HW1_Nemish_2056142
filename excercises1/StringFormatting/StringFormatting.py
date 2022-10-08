def print_formatted(number):
    for i in range(1,number+1):
        space=len(str(bin(number))[2:])
        #bin_space=(len(bin(number)[2:])-len(bin(i)[2:])+1)*' '
        #hex_space=(len(bin(number)[2:])-len(hex(i)[2:])+1)*' '
        #oct_space=(len(bin(number)[2:])-len(oct(i)[2:])+1)*' '
        #int_space=' '
        print(str(i).rjust(space,' ')+str(oct(i)[2:]).rjust(space+1,' ')+str(hex(i)[2:]).upper().rjust(space+1,' ')+str(bin(i)[2:]).rjust(space+1,' '))
    # your code goes here

