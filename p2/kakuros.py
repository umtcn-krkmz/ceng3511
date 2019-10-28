from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from ortools.sat.python import cp_model
import sys


def SimpleSatProgram():
    """Minimal CP-SAT example to showcase calling the solver."""
    top_col=[]
    top_row=[]
   # Reads the input file

    inputfile=sys.argv[1]
    all_input=inputfile.readlines()
    top_row_sad=all_input[0].split(", ")
    top_col_sad=all_input[1].split(", ")
    for i in top_col_sad:
        top_col.append(int(i))
    for i in top_row_sad:
        top_row.append(int(i))
    # Creates the model.
    model = cp_model.CpModel()

    # Creates the variables.


    a = top_row[0]
    b = top_row[1]
    c = top_row[2]
    d = top_col[0]
    e = top_col[1]
    f = top_col[2]
    num_vals = 10
    g = model.NewIntVar(1, num_vals - 1, 'g')
    h = model.NewIntVar(1, num_vals - 1, 'h')
    i = model.NewIntVar(1, num_vals - 1, 'i')
    j = model.NewIntVar(1, num_vals - 1, 'j')
    k = model.NewIntVar(1, num_vals - 1, 'k')
    l = model.NewIntVar(1, num_vals - 1, 'l')
    m = model.NewIntVar(1, num_vals - 1, 'm')
    n = model.NewIntVar(1, num_vals - 1, 'n')
    o = model.NewIntVar(1, num_vals - 1, 'o')
    sec_col=[g,j,m]
    thr_col=[h,k,n]
    frt_col=[i,l,o]
    sec_row=[g,h,i]
    thr_row=[j,k,l]
    frt_row=[m,n,o]
    # Creates the constraints.

    model.AddAllDifferent(sec_col)
    model.AddAllDifferent(thr_col)
    model.AddAllDifferent(frt_col)
    model.AddAllDifferent(sec_row)
    model.AddAllDifferent(thr_row)
    model.AddAllDifferent(frt_row)
    model.Add(g + j + m == a)
    model.Add(h + k + n == b)
    model.Add(i + l + o == c)
    model.Add(g + h + i == d)
    model.Add(j + k + l == e)
    model.Add(m + n + o == f)

    # Creates a solver and solves the model.
    solver = cp_model.CpSolver()
    status = solver.Solve(model)
    g=solver.Value(g)
    h=solver.Value(h)
    i=solver.Value(i)
    j=solver.Value(j)
    k=solver.Value(k)
    l=solver.Value(l)
    m=solver.Value(m)
    n=solver.Value(n)
    o=solver.Value(o)
    if status == cp_model.FEASIBLE:
        towrite=["x",",",str(top_row[0]),",",str(top_row[1]),",",str(top_row[2]),"\n",str(top_col[0]),",",str(g),",",str(h),",",str(i),"\n",str(top_col[1]),",",str(j),",",str(k),",",str(l),"\n",str(top_col[2]),",",str(m),",",str(n),",",str(o),"\n"]
        outputfile=open("output.txt","w")
        outputfile.writelines(towrite)
        print(" x",",",top_row[0],",",top_row[1],",",top_row[2],"\n",top_col[0],",",g,",",h,",",i,"\n",top_col[1],",",j,",",k,",",l,"\n",top_col[2],",",m,",",n,",",o,"\n")
    else:
        print("no solution found")
SimpleSatProgram()
