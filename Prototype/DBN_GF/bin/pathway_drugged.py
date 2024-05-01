import createDBN_drugged as cd_d
from pgmpy.inference import VariableElimination

def pathway(fl,drugv,idict):
    cd_d.createDBN(fl,drugv)
    inference = VariableElimination(cd_d.model)
    r1 = inference.query(variables=['O1'], evidence=idict)
    r2 = inference.query(variables=['O2'], evidence=idict)
    r3 = inference.query(variables=['O3'], evidence=idict)
    r4 = inference.query(variables=['O4'], evidence=idict)
    r5 = inference.query(variables=['O5'], evidence=idict)
    r6 = inference.query(variables=['O6'], evidence=idict)
    r7 = inference.query(variables=['O7'], evidence=idict)
    l=[]
    if r1.values[0]==1.0:
        l.append(0)
    else:
        l.append(1)
    if r2.values[0]==1.0:
        l.append(0)
    else:
        l.append(1)
    if r3.values[0]==1.0:
        l.append(0)
    else:
        l.append(1)
    if r4.values[0]==1.0:
        l.append(0)
    else:
        l.append(1)
    if r5.values[0]==1.0:
        l.append(0)
    else:
        l.append(1)
    if r6.values[0]==1.0:
        l.append(0)
    else:
        l.append(1)
    if r7.values[0]==1.0:
        l.append(0)
    else:
        l.append(1)
    
    return l

