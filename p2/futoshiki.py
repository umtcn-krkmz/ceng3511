from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from ortools.sat.python import cp_model
import sys

# Create a function called "chunks" with two arguments, l and n:
def chunks(l, n):
    # For item i in a range that is a length of l,
    for i in range(0, len(l), n):
        # Create an index range for l of n items:
        yield l[i:i+n]
def SimpleSatProgram():
    """Minimal CP-SAT example to showcase calling the solver."""

   # Reads the input file
    inp=open(sys.argv[1],"r")
    raw_inp=inp.readlines()
    less_raw_inp=[]
    for i in raw_inp:
        less_raw_inp.append(i.strip("\n"))
  

    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.

    variables=[]
    num_vals = 5
    a = model.NewIntVar(1, num_vals - 1, 'a')
    variables.append(a)
    b = model.NewIntVar(1, num_vals - 1, 'b')
    variables.append(b)
    c = model.NewIntVar(1, num_vals - 1, 'c')
    variables.append(c)
    d = model.NewIntVar(1, num_vals - 1, 'd')
    variables.append(d)
    e = model.NewIntVar(1, num_vals - 1, 'e')
    variables.append(e)
    f = model.NewIntVar(1, num_vals - 1, 'f')
    variables.append(f)
    g = model.NewIntVar(1, num_vals - 1, 'g')
    variables.append(g)
    h = model.NewIntVar(1, num_vals - 1, 'h')
    variables.append(h)
    i = model.NewIntVar(1, num_vals - 1, 'i')
    variables.append(i)
    j = model.NewIntVar(1, num_vals - 1, 'j')
    variables.append(j)
    k = model.NewIntVar(1, num_vals - 1, 'k')
    variables.append(k)
    l = model.NewIntVar(1, num_vals - 1, 'l')
    variables.append(l)
    m = model.NewIntVar(1, num_vals - 1, 'm')
    variables.append(m)
    n = model.NewIntVar(1, num_vals - 1, 'n')
    variables.append(n)
    o = model.NewIntVar(1, num_vals - 1, 'o')
    variables.append(o)
    p = model.NewIntVar(1, num_vals - 1, 'p')
    variables.append(p)
    dictionary={"A1":a,"A2":b,"A3":c,"A4":d,"B1":e,"B2":f,"B3":g,"B4":h,"C1":i,"C2":j,"C3":k,"C4":l,"D1":m,"D2":n,"D3":o,"D4":p}
    dictionary2 =  dict((y,x) for x,y in dictionary.items()) # {a:"a1",b:a2,c:a3,d:a4,e:b1,f:1,g:b3,h:b4,i:c1,j:c2,k:c3,l:c4,m:d1,n:d2,o:d3,p:2}
    col1=[a,b,c,d]
    col2=[e,f,g,h]
    col3=[i,j,k,l]
    col4=[m,n,o,p]
    row1=[a,e,i,m]
    row2=[b,f,j,n]
    row3=[c,g,k,o]
    row4=[d,h,l,p]
    # Creates the constraints.
    for q in less_raw_inp:
        if not q[4].isalpha():
            dictionary2[dictionary[q[0]+q[1]]]=q[4]

            for value in variables:
                if not dictionary2[value].isalpha():
                    try:
                        model.Add(value == int(dictionary2[value]))
                    except:
                        continue
   
        else:
            model.Add(dictionary[q[0]+q[1]]>dictionary[q[4]+q[5]])
    model.AddAllDifferent(col1)
    model.AddAllDifferent(col2)
    model.AddAllDifferent(col3)
    model.AddAllDifferent(col4)
    model.AddAllDifferent(row1)
    model.AddAllDifferent(row2)
    model.AddAllDifferent(row3)
    model.AddAllDifferent(row4)




    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    if status == cp_model.FEASIBLE:
        results=[]
        outputfile=open("futoshiki_output.txt","w")
        for q in variables:
            i=solver.Value(q)
            results.append(i)
        last_result=list(chunks(results,4))
        for i in last_result:
            print(i)
            outputfile.write(str(i))
            outputfile.write("\n")
    else:
        print("no solution found")
SimpleSatProgram()
