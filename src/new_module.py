
def new_function(param):
    assert isinstance(param,str), "Input must be a string"
    name_list=param.split(" ")
    new_name=[]
    for string in name_list:
        if len(string)>1:
            dummy=list(string)
            dummy2=string[0]
            dummy[0]=dummy[-1]
            dummy[-1]=dummy2
            new_name.append("".join(dummy)+"ay")
    final_name=" ".join(new_name)
    print(f'Your Pig Latin Name is {final_name}')
    return final_name

def square(x):
    assert isinstance(x, int), 'input must be an integer'
    y = x**2
    return(y)

