#encoding output vector
def encode(outv,design_parameter=0.5):
    t=0
    r=0
    a=design_parameter
    for i in range(6):
        t+=outv[i]
    for i in range(6,9):
        r+=outv[i]
    res=a*abs(t-r)+(1-a)*(t*r)
    return res

