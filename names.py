#make sure thinhs are declared before used
#line after delcares locations
#no things can be declared twice

#given a list of lists of tokens each list = tokens


def declaration_check(list):
    declared=["" for line in list]
    for i,line in enumerate(list):
            if isinstance(line[0], Variable) && isinstance(line[1], ISA):
                if line[0] in is_declared:
                    print(line[0]," is already declared: angEry!")
                else:
                    is_declared[list.index[line]]=line[0]
                    if isinstance(list[i+1][0], Variable) && isinstance(list[i+1][1], ISIN):
                        pass
                    else:
                        print(list[i+1]" IS NOT A LOCATION DECLARATION: ANgeRY")


    for line in list:
        if line[0] in is_declared[:(list.index[line]+1)]:
            pass
        else:
            print(line[0], " isn't DEcLARED: u shall NOT PASSS")
