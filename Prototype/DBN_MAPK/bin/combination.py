#combination of vector
def combination(vec):
    i=len(vec)-1
    while vec[i]==1:
        vec[i]=0
        i=i-1
    if i==-1:
        return False
    vec[i]=1
    return vec