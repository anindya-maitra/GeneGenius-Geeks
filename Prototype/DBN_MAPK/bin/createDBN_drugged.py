from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD

model = BayesianNetwork([('I1', 'P1'), ('I1', 'P2'), ('I2', 'P2'),
                         ('I3', 'P3'), ('I4', 'P4'), ('P1', 'P5'),
                         ('P2', 'P5'), ('P3', 'P5'), ('P4', 'P5'),
                         ('P5', 'P6'), ('P3', 'P8'), ('P4', 'P9'),
                         ('P6', 'P9'), ('P8', 'P9'), ('I5', 'P10'),
                         ('P9', 'P10'), ('P10', 'P11'), ('P11', 'P12'),
                         ('P6', 'P13'), ('P13', 'P14'), ('P14', 'P15'),
                         ('P6', 'P16'), ('P16', 'P17'), ('P17', 'P18'),
                         ('P12', 'P19'), ('P12', 'P20'), ('P20', 'P21'),
                         ('P21', 'P22'), ('P22', 'P23'), ('P11', 'P23'),
                         ('P18', 'P23'), ('P12', 'P24'), ('P23', 'P24'),
                         ('P18', 'P25'), ('P22', 'P25'), ('P18', 'P26'),
                         ('P22', 'P26'), ('P26', 'P27'),
                         ('P15', 'O1'), ('P23', 'O1'), ('P18', 'O2'),
                         ('P18', 'O3'), ('P23', 'O3'), ('P18', 'O4'),
                         ('P23', 'O4'), ('P25', 'O5'), ('P27', 'O6'),
                         ('P24', 'O7'), ('P24', 'O8'), ('P19', 'O9')])


def createDBN(fl, drugv):
    i1 = TabularCPD(variable='I1', variable_card=2, values=[[0.5], [0.5]])
    i2 = TabularCPD(variable='I2', variable_card=2, values=[[0.5], [0.5]])
    i3 = TabularCPD(variable='I3', variable_card=2, values=[[0.5], [0.5]])
    i4 = TabularCPD(variable='I4', variable_card=2, values=[[0.5], [0.5]])
    i5 = TabularCPD(variable='I5', variable_card=2, values=[[0.5], [0.5]])

    if drugv[0]==1 or drugv[1]==1:      #lapatinib/AG825
       p1= TabularCPD(variable='P1', variable_card=2, values=[[1,1],[0,0]],
                       evidence=['I1'], evidence_card=[2])
    elif 1 in fl:
        p1= TabularCPD(variable='P1', variable_card=2, values=[[0,0],[1,1]],
                       evidence=['I1'], evidence_card=[2])
    else:
        p1= TabularCPD(variable='P1', variable_card=2, values=[[1,0],[0,1]],
                       evidence=['I1'], evidence_card=[2])
    
    if drugv[0]==1:                     #lapatinib
        p2= TabularCPD(variable='P2', variable_card=2, values=[[1,1,1,1],[0,0,0,0]],
                       evidence=['I1','I2'], evidence_card=[2,2])
        
    elif 2 in fl:
        p2= TabularCPD(variable='P2', variable_card=2, values=[[0,0,0,0],[1,1,1,1]],
                       evidence=['I1','I2'], evidence_card=[2,2])
    else:
        p2= TabularCPD(variable='P2', variable_card=2, values=[[1,0,0,0],[0,1,1,1]],
                       evidence=['I1','I2'], evidence_card=[2,2])
    
    
    if drugv[2]==1:                     #AG1024
        p3= TabularCPD(variable='P3', variable_card=2, values=[[1,1],[0,0]],
                       evidence=['I3'], evidence_card=[2])
    elif 3 in fl:
        p3= TabularCPD(variable='P3', variable_card=2, values=[[0,0],[1,1]],
                       evidence=['I3'], evidence_card=[2])
    else:
        p3= TabularCPD(variable='P3', variable_card=2, values=[[1,0],[0,1]],
                       evidence=['I3'], evidence_card=[2])
    
    
    if drugv[0]==1 or drugv[1]==1:      #lapatinib/AG825
        p4= TabularCPD(variable='P4', variable_card=2, values=[[1,1],[0,0]],
                       evidence=['I4'], evidence_card=[2])
    
    elif 4 in fl:
        p4= TabularCPD(variable='P4', variable_card=2, values=[[0,0],[1,1]],
                       evidence=['I4'], evidence_card=[2])
    else:
        p4= TabularCPD(variable='P4', variable_card=2, values=[[1,0],[0,1]],
                       evidence=['I4'], evidence_card=[2])
    
    if 5 in fl:
        p5= TabularCPD(variable='P5', variable_card=2,
                       values=[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                               [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],
                       evidence=['P1','P2','P3','P4'],
                       evidence_card=[2,2,2,2])
    else:
        p5= TabularCPD(variable='P5', variable_card=2,
                       values=[[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                               [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]],
                       evidence=['P1','P2','P3','P4'],
                       evidence_card=[2,2,2,2])
    
    if 6 in fl:
        p6= TabularCPD(variable='P6', variable_card=2, values=[[0,0],[1,1]],
                       evidence=['P5'], evidence_card=[2])
    else:
        p6= TabularCPD(variable='P6', variable_card=2, values=[[1,0],[0,1]],
                       evidence=['P5'], evidence_card=[2])        
    
    if 7 in fl:
        i5 = TabularCPD(variable='I5', variable_card=2, values=[[1], [0]])
        
    if 8 in fl:
        p8= TabularCPD(variable='P8', variable_card=2, values=[[0,0],[1,1]],
                       evidence=['P3'], evidence_card=[2])
    else:
        p8= TabularCPD(variable='P8', variable_card=2, values=[[1,0],[0,1]],
                       evidence=['P3'], evidence_card=[2])
    
    if drugv[4]==1:                     #LY294002
        p9= TabularCPD(variable='P9', variable_card=2,
                        values=[[1,1,1,1,1,1,1,1],[0,0,0,0,0,0,0,0]],
                        evidence=['P4','P6','P8'],evidence_card=[2,2,2])

    elif 9 in fl:
        p9= TabularCPD(variable='P9', variable_card=2,
                       values=[[0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1]],
                       evidence=['P4','P6','P8'],evidence_card=[2,2,2])
    else:
        p9= TabularCPD(variable='P9', variable_card=2,
                       values=[[1,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1]],
                       evidence=['P4','P6','P8'],evidence_card=[2,2,2])
    
    if 10 in fl:
        p10= TabularCPD(variable='P10', variable_card=2, values=[[0,0,0,0],[1,1,1,1]],
                       evidence=['I5','P9'], evidence_card=[2,2])    
    else:
        p10= TabularCPD(variable='P10', variable_card=2, values=[[0,0,1,0],[1,1,0,1]],
                       evidence=['I5','P9'], evidence_card=[2,2])
    
    if 11 in fl:
        p11= TabularCPD(variable='P11', variable_card=2, values=[[0,0],[1,1]],
                       evidence=['P10'], evidence_card=[2])
    else:
        p11= TabularCPD(variable='P11', variable_card=2, values=[[1,0],[0,1]],
                       evidence=['P10'], evidence_card=[2])
    
    if 12 in fl:
        p12= TabularCPD(variable='P12', variable_card=2, values=[[0,0],[1,1]],
                       evidence=['P11'], evidence_card=[2])
    else:
        p12= TabularCPD(variable='P12', variable_card=2, values=[[1,0],[0,1]],
                       evidence=['P11'], evidence_card=[2])
    
    if 13 in fl:
        p13= TabularCPD(variable='P13', variable_card=2, values=[[0,0],[1,1]],
                       evidence=['P6'], evidence_card=[2])
    else:
        p13= TabularCPD(variable='P13', variable_card=2, values=[[1,0],[0,1]],
                       evidence=['P6'], evidence_card=[2])
    
    if 14 in fl:
        p14= TabularCPD(variable='P14', variable_card=2, values=[[0,0],[1,1]],
                       evidence=['P13'], evidence_card=[2])
    else:
        p14= TabularCPD(variable='P14', variable_card=2, values=[[1,0],[0,1]],
                       evidence=['P13'], evidence_card=[2])
    
    if 15 in fl:
        p15= TabularCPD(variable='P15', variable_card=2, values=[[0,0],[1,1]],
                       evidence=['P14'], evidence_card=[2])
    else:
        p15= TabularCPD(variable='P15', variable_card=2, values=[[1,0],[0,1]],
                       evidence=['P14'], evidence_card=[2])
    
    if 16 in fl:
        p16= TabularCPD(variable='P16', variable_card=2, values=[[0,0],[1,1]],
                       evidence=['P6'], evidence_card=[2])
    else:
        p16= TabularCPD(variable='P16', variable_card=2, values=[[1,0],[0,1]],
                       evidence=['P6'], evidence_card=[2])
        
    if drugv[3]==1:                     #U0126
        p17= TabularCPD(variable='P17', variable_card=2, values=[[1,1],[0,0]],
                       evidence=['P16'], evidence_card=[2])
        
    elif 17 in fl:
        p17= TabularCPD(variable='P17', variable_card=2, values=[[0,0],[1,1]],
                       evidence=['P16'], evidence_card=[2])
    else:
        p17= TabularCPD(variable='P17', variable_card=2, values=[[1,0],[0,1]],
                       evidence=['P16'], evidence_card=[2])
        
    if 18 in fl:
        p18= TabularCPD(variable='P18', variable_card=2, values=[[0,0],[1,1]],
                       evidence=['P17'], evidence_card=[2])
    else:
        p18= TabularCPD(variable='P18', variable_card=2, values=[[1,0],[0,1]],
                       evidence=['P17'], evidence_card=[2])
    
    if 19 in fl:
        p19= TabularCPD(variable='P19', variable_card=2, values=[[1,1],[0,0]],
                       evidence=['P12'], evidence_card=[2])
    else:
        p19= TabularCPD(variable='P19', variable_card=2, values=[[0,1],[1,0]],
                       evidence=['P12'], evidence_card=[2])
    
    if drugv[6]==1:                      #metformin
        p20= TabularCPD(variable='P20', variable_card=2, values=[[0,1],[1,0]],
                        evidence=['P12'], evidence_card=[2])
    
    elif 20 in fl:
        p20= TabularCPD(variable='P20', variable_card=2, values=[[1,1],[0,0]],
                       evidence=['P12'], evidence_card=[2])
    else:
        p20= TabularCPD(variable='P20', variable_card=2, values=[[0,0],[1,1]],
                       evidence=['P12'], evidence_card=[2])
    
    if 21 in fl:
        p21= TabularCPD(variable='P21', variable_card=2, values=[[0,0],[1,1]],
                       evidence=['P20'], evidence_card=[2])
    else:
        p21= TabularCPD(variable='P21', variable_card=2, values=[[0,1],[1,0]],
                       evidence=['P20'], evidence_card=[2])
    
    if drugv[5]==1:                     #temsirolimus
        p22= TabularCPD(variable='P22', variable_card=2, values=[[1,1],[0,0]],
                       evidence=['P21'], evidence_card=[2])
    
    elif 22 in fl:
        p22= TabularCPD(variable='P22', variable_card=2, values=[[0,0],[1,1]],
                       evidence=['P21'], evidence_card=[2])
    else:
        p22= TabularCPD(variable='P22', variable_card=2, values=[[1,0],[0,1]],
                       evidence=['P21'], evidence_card=[2])
    
    if 23 in fl:
        p23= TabularCPD(variable='P23', variable_card=2,
                       values=[[0,0,0,0,0,0,0,0],[1,1,1,1,1,1,1,1]],
                       evidence=['P11','P18','P22'],evidence_card=[2,2,2])
    else:
        p23= TabularCPD(variable='P23', variable_card=2,
                       values=[[1,0,0,0,0,0,0,0],[0,1,1,1,1,1,1,1]],
                       evidence=['P11','P18','P22'],evidence_card=[2,2,2])
    
    if 24 in fl:
        p24= TabularCPD(variable='P24', variable_card=2, values=[[1,1,1,1],[0,0,0,0]],
                       evidence=['P12','P23'], evidence_card=[2,2])
    else:
        p24= TabularCPD(variable='P24', variable_card=2, values=[[0,1,1,1], [1,0,0,0]],
                       evidence=['P12','P23'], evidence_card=[2,2])
        
    if 25 in fl:
        p25= TabularCPD(variable='P25', variable_card=2, values=[[0,0,0,0],[1,1,1,1]],
                       evidence=['P18','P22'], evidence_card=[2,2])
    else:
        p25= TabularCPD(variable='P25', variable_card=2, values=[[1,0,0,0], [0,1,1,1]],
                       evidence=['P18','P22'], evidence_card=[2,2])
        
    if 26 in fl:
        p26 = TabularCPD(variable='P26', variable_card=2, values=[[1,1,1,1],[0,0,0,0]],
                       evidence=['P18','P22'], evidence_card=[2,2])
    else:
        p26 = TabularCPD(variable='P26', variable_card=2, values=[[0,1,1,1], [1,0,0,0]],
                       evidence=['P18','P22'], evidence_card=[2,2])
        
    if 27 in fl:
        p27= TabularCPD(variable='P27', variable_card=2, values=[[0, 0],[1,1]],
                       evidence=['P26'], evidence_card=[2])
    else:
        p27= TabularCPD(variable='P27', variable_card=2, values=[[0,1], [1,0]],
                       evidence=['P26'], evidence_card=[2])
    
    
    
    
    o1= TabularCPD(variable='O1', variable_card=2, values=[[1,1,1,0], [0,0,0,1]],
                   evidence=['P15','P23'], evidence_card=[2,2])
    
    o2= TabularCPD(variable='O2', variable_card=2, values=[[1,0],[0,1]],
                   evidence=['P18'], evidence_card=[2])
    
    o3= TabularCPD(variable='O3', variable_card=2, values=[[1,1,1,0], [0,0,0,1]],
                   evidence=['P18','P23'], evidence_card=[2,2])
    
    o4= TabularCPD(variable='O4', variable_card=2, values=[[1,1,1,0], [0,0,0,1]],
                   evidence=['P18','P23'], evidence_card=[2,2])
    
    o5= TabularCPD(variable='O5', variable_card=2, values=[[1,0],[0,1]],
                   evidence=['P25'], evidence_card=[2])
    
    o6= TabularCPD(variable='O6', variable_card=2, values=[[1,0],[0,1]],
                   evidence=['P27'], evidence_card=[2])
    
    o7= TabularCPD(variable='O7', variable_card=2, values=[[0,1],[1,0]],
                   evidence=['P24'], evidence_card=[2])
    
    o8= TabularCPD(variable='O8', variable_card=2, values=[[0,1],[1,0]],
                   evidence=['P24'], evidence_card=[2])
    
    o9= TabularCPD(variable='O9', variable_card=2, values=[[0,1],[1,0]],
                   evidence=['P19'], evidence_card=[2])
    
    
    
    model.add_cpds(i1,i2,i3,i4,i5,p1,p2,p3,p4,p5,p6,p8,p9,p10,
                   p11,p12,p13,p14,p15,p16,p17,p18,p19,p20,p21,
                   p22,p23,p24,p25,p26,p27,o1,o2,o3,o4,o5,o6,o7,o8,o9)
    
    if model.check_model():
        print("Model is valid.")
        