
import numpy as np
import math as math
import sympy as sp
from gekko import GEKKO
from tabulate import tabulate
from prettytable import PrettyTable
import pandas as pd
import platform   
import os
import matplotlib.pyplot as plt

# To install the libraries above enter the following command: pip install -r "_Path_to_requirements.txt"
# Example : pip install -r "C:\requirements.txt"

# Global variables
MM=9999
red = '\033[31m'
reset = '\033[0m'
green = '\033[32m'

# Method to clear the terminal (optional method)
def clear_screen():  
    # Check if the platform is Windows or linux
    if(platform.system().lower()=="windows"):
        cmdtorun='cls'
    else:
        cmdtorun='clear'   
    os.system(cmdtorun)

# Method to format constraints (Used in graphical method for displaying legends)
def ConcatStringTables(Printcc):
    for i in range(len(Printcc)):
        x=""
        for j in range(len(Printcc[i])):
            x=x+Printcc[i][j]
        Printcc[i]=x
    return Printcc
  
# Method to Display Pivot Coordinates
def PrintPivotCoordinates(inputpivot,outputpivot):
    xx=["\033[31mPivot column: \033[0m"+inputpivot] 
    yy=["\033[31mPivot row:   \033[0m"+outputpivot] 
    myTable = PrettyTable(xx)
    myTable.add_row(yy)
    print(myTable)

# Method to Display Solution
def PrintSolution(Righth):
    xx=["\033[31mSolution\033[0m"] 
    Solution=["Your optimal Z value is = "+str(Righth)]
    myTable = PrettyTable(xx)
    myTable.add_row(Solution)
    print(myTable)
    
# Method to Display Tables
def PrintTable(AA,Row1,Colm1):
    df=pd.DataFrame(AA, index=Row1,columns=Colm1+["c"])
    print(tabulate(df, headers='keys', tablefmt='psql'))
    
# Method to Display The Linear Program
def PrintLinearProgram(Zeroline1,Printcc1):
    print("\033[31m--------- Linear Program -------- \n",reset)
    print('Objective Function: ',*Zeroline1, sep=' ')
    print("\nSubject To:")
    for i in range(0,len(Printcc1)):
        print(*Printcc1[i], sep=' ')  
    print("\033[31m\n---------------------------------\n",reset)

# Method that Displays the linear program stored in memory
def SavedlinearProgramInR1():
    Printcc=[['+6.0x1', '+4.0x2', '<= 24.0'], ['+1.0x1', '+2.0x2', '<= 6.0'], ['-1.0x1', '+1.0x2', '<= 1.0'], ['+1.0x2', '<= 2.0'], ['+2.0x2', '<= 5.0'], ['+1.0x1', '>= 1.0'], ['+2.0x1', '>= 3.0'], ['+2.0x2', '>= 2.0'], ['+2.0x1', '+4.0x2', '<= 14.0'], ['-2.0x1', '+2.0x2', '<= 3.0']]
    A=[[-1.0, -1.0, -0.0, -0.0, -0.0, -0.0, -0.0, -0.0, 9999.0, -0.0, 9999.0,0 ,9999.0, 0, 0, 0 ], [6.0, 4.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 24.0], [1.0, 2.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 6.0], [-1.0, 1.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 2.0],[0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0.0,5.0],[1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,0.0,1.0],[2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 1.0, 0.0, 0.0, 0.0,0.0,3],[0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 1.0, 0.0,0.0,2.0],[2.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0,0.0,14],[-2.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,1.0,3.0]]
    Zeroline= ['Z =', '+1.0x1', '1.0x2']
    Colm=['x1', 'x2', 's1', 's2', 's3', 's4', 's5', 's6', 'R1', 's7', 'R2', 's8', 'R3', 's9','s10']
    Con=[1, 1, 1, 1, 1, 3, 3, 3, 1, 1]
    Row=['Z', 'S1', 'S2', 'S3', 'S4', 'S5', 'R1', 'R2', 'R3', 'S9', 'S10']
    PrintLinearProgram(Zeroline, Printcc)
    Colm1=['Available solutions ' ]
    Row1=[['The BIG M Method        \n'],['Graphic Method         \n'],['Select another LP       ']]
    myTable = PrettyTable(Colm1)
    myTable.add_rows(Row1)
    myTable.add_autoindex(' ')
    print(myTable)
    Choice=int(input("\033[32mPlease select one option: \033[0m"))
    if (Choice ==1):
      Mode=int(input("\033[32mPlease Choose your mode 1)Max 2)Min: \033[0m"))
      if (Mode!=1 and Mode!=2 ):
        exit()
      else:
        clear_screen()
        BigmMethod(A, Printcc, Zeroline, Colm, Row , Mode)
        exit0= int(input("\033[32mDo you want to continue ! 1) Yes 2) No: \033[0m"))
        if(exit0==1):
          SavedlinearProgramInR1()
        else:
          exit()
    elif(Choice==2):
      Mode=int(input("\033[32mPlease Choose your mode 1)Max 2)Min: \033[0m"))
      if (Mode!=1 and Mode!=2 ):
        exit()
      else:
        clear_screen()
        GraphicMethod(A,Printcc, Mode,Con )
        print("Graphical Solution")
        exit0= int(input("\033[32mDo you want to continue ! 1) Yes 2) No: \033[0m"))
        if(exit0==1):
          SavedlinearProgramInR1()
        else:
          exit()
    else:
      clear_screen()
      main() 

# Method that Displays the linear program stored in memory
def SavedlinearProgramInR2():
    Printcc=[['+1.0x1', '+1.0x2', '>= 2.0'], ['-1.0x1', '+1.0x2', '>= 1.0'], ['+1.0x2', '<= 3.0'], ['+2.0x2', '<= 7.0'], ['+1.0x1', '<= 2.0'], ['+1.0x2', '>= 1.0'], ['+1.0x2', '<= 4.0'], ['+1.0x1', '+1.0x2', '>= 1.0']]
    A=[[-1.0, 1.0, -0.0, 9999.0, -0.0, 9999.0, -0.0, -0.0, -0.0, -0.0, 9999.0, -0.0, -0.0, 9999.0,-0.0], [1.0, 1.0, -1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,2.0], [-1.0, 1.0, 0.0, 0.0, -1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,3.0], [0.0, 2.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 7.0], [1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0,2.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 1.0, 0.0, 0.0, 0.0,1.0], [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0,4.0], [1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, -1.0, 1.0, 1.0]]
    Zeroline= ['Z =', '+1.0x1', '-1.0x2']
    Row=['Z', 'R1', 'R2', 'S3', 'S4', 'S5', 'R3', 'S7', 'R4']
    Colm=['x1', 'x2', 's1', 'R1', 's2', 'R2', 's3', 's4', 's5', 's6', 'R3', 's7', 's8', 'R4']
    Con=[3, 3, 1, 1, 1, 3, 1, 3]
    PrintLinearProgram(Zeroline, Printcc)
    Colm1=['Available solutions ' ]
    Row1=[['The BIG M Method        \n'],['Graphic Method         \n'],['Select another LP       ']]
    myTable = PrettyTable(Colm1)
    myTable.add_rows(Row1)
    myTable.add_autoindex(' ')
    print(myTable)
    Choice=int(input("\033[32mPlease select one option: \033[0m"))
    if (Choice ==1):
      Mode=int(input("\033[32mPlease Choose your mode 1)Max 2)Min: \033[0m"))
      if (Mode!=1 and Mode!=2 ):
        exit()
      else:
        clear_screen()
        BigmMethod(A, Printcc, Zeroline, Colm, Row , Mode)
        exit0= int(input("\033[32mDo you want to continue ! 1)Yes 2)No: \033[0m"))
        if(exit0==1):
          SavedlinearProgramInR2()
        else:
          exit()
    elif(Choice==2):
        clear_screen()
        Mode=int(input("\033[32mPlease Choose your mode 1)Max 2)Min: \033[0m"))
        GraphicMethod(A,Printcc,Mode,Con)
        print("Graphical Solution")
        exit0= int(input("\033[32mDo you want to continue ! 1)Yes 2)No: \033[0m"))
        if(exit0==1):
          SavedlinearProgramInR2()
        else:
          exit()
    else:
      clear_screen()
      main() 

# Method that Displays the linear program stored in memory
def SavedlinearProgramInR3():
    Printcc=[['+2.0x1', '+5.0x2', '-1.0x3', '<=18.0'], ['+1.0x1', '-1.0x2', '-2.0x3', '<= -14.0'], ['+3.0x1', '+2.0x2', '+2.0x3', '= 26.0'], ['+2.0 x1', '+5.0 x2', '-1.0 x3', '<= 20.0'], ['+4.0x1', '+10.0x2', '-1.0x3', '<= 40.0']]
    A=[[-6.0, 7.0, 4.0, 0.0, 0.0, 9999.0, 0.0, 0.0, 0.0], [2.0, 5.0, -1.0, 1.0, 0.0, 0.0, 0.0, 0.0, 18.0], [1.0, -1.0, -2.0, 0.0, 1.0, 0.0, 0.0, 0.0, -14.0], [3.0, 2.0, 2.0, 0.0, 0.0, 1.0, 0.0, 0.0, 26.0], [2.0, 5.0, -1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 20.0], [4.0, 10.0, -1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 40.0]]
    Zeroline= ['Z =', '-6.0x1', '+7.0x2', '+4.0x3']
    Row=['Z', 'S1', 'S2', 'R1', 'S3', 'S4']
    Colm=['x1', 'x2', 'x3', 's1', 's2', 'R1', 's3', 's4']
    PrintLinearProgram(Zeroline, Printcc)
    Colm1=['\033[31mAvailable solutions \033[0m' ]
    Row1=[['The BIG M Method        \n'],['Select another LP       ']]
    myTable = PrettyTable(Colm1)
    myTable.add_rows(Row1)
    myTable.add_autoindex(' ')
    print(myTable)
    Choice=int(input("\033[32mPlease select one option: \033[0m"))
    if (Choice ==1):
      Mode=int(input("\033[32mPlease Choose your mode 1)Max 2)Min: \033[0m"))
      if (Mode!=1 and Mode!=2 ):
        exit()
      else:
        clear_screen()
        BigmMethod(A, Printcc, Zeroline, Colm, Row , Mode)
        exit0= int(input("\033[32mDo you want to continue ! 1) Yes 2) No: \033[0m"))
        if(exit0==1):
          SavedlinearProgramInR3()
        else:
          exit()
    else:
      main()

# Method displayed by the linear program entered by the user  
def RandomlinearProgramInR(A1, Printcc1, Zeroline1, Colm1, Row1 , Mode1,V1,Con1):
    if(V1==1 or V1==2):
      PrintLinearProgram(Zeroline1, Printcc1)
      #Print Available solutions
      Colm2=['Available solutions ' ]
      Row2=[['The BIG M Method        \n'],['Graphic Method         \n'],['Select another LP       ']]
      myTable = PrettyTable(Colm2)
      myTable.add_rows(Row2)
      myTable.add_autoindex(' ')
      print(myTable)
      Choice1=int(input("\033[32mPlease select one option: \033[0m"))
      if (Choice1 ==1):
          clear_screen()
          BigmMethod(A1, Printcc1, Zeroline1, Colm1, Row1 , Mode1)
          exit0= int(input("\033[32mDo you want to continue ! 1)Yes 2)No: \033[0m"))
          if(exit0==1):
            main()
          else:
            exit()
      elif(Choice1==2):
          clear_screen()
          GraphicMethod(A1,Printcc1,Mode1,Con1)
          print("Graphical Solution")
          exit0= int(input("\033[32mDo you want to continue ! 1)Yes 2)No: \033[0m"))
          if(exit0==1):
            RandomlinearProgramInR(A1, Printcc1, Zeroline1, Colm1, Row1 , Mode1,V1,Con1)
          else:
            exit()
      else:
        clear_screen()
        main()

# Method that Displays the linear programs stored in memory     
def SavedlinearProgram():
    Colm=['\033[31mSelect linear program from memory   \033[0m ' ]
    myTable = PrettyTable(Colm)
    Row=[['Linear Program In R 1(10 Constraints)  \n'],['Linear Program In R 2(10 Constraints)  \n'],['Linear Program In R3 (5 Constraints)   ']]
    myTable.add_rows(Row)
    myTable.add_autoindex(' ')
    print(myTable)
    Choice=int(input("\033[32m\nEnter your choice please: \033[0m"))
    print(Choice)
    if (Choice ==1):
       clear_screen()
       SavedlinearProgramInR1()
    elif (Choice==2):
       clear_screen()
       SavedlinearProgramInR2()
    elif (Choice==3):
        clear_screen()
        SavedlinearProgramInR3()
    else:
        clear_screen()
        print('End program...')    
        exit()

# Linear system input method
def LinearSystemInput():
  Colm=[]
  Row=["Z"]
  Mode=int(input("\033[32mPlease Choose Your Mode 1)Max 2)Min: \033[0m"))
  Sol=2
  V=int(input("\033[32mPlease Enter the Number of Variables: \033[0m\n"))
  C=int(input("\033[32mPlease Enter the Number of Constraints: \033[0m\n"))

  print("\033[36m Variables=",V,"\n Constraints=",C)
  print("\033[0m")
  con=[] 
  Added=[]
  ZZ=[]
  #Print probelm
  Zeroline=["Z ="]
  Printcc=[]
  counter1=1
  for i in range(0,C+1):
    if i==0:
      for k in range(1,V+1):
        print("\033[32mPlease enter the coefficient x",k,"In Z: \033[0m")
        Z=float(input())
        ZZ.append(Z)
        Colm=Colm+["x"+str(counter1)]
        if Z>0:
          Zeroline.append("+"+str(Z)+"x"+str(counter1))
        elif Z<0:
          Zeroline.append(str(Z)+"x"+str(counter1))
        counter1=counter1+1
      ZZ.append(0)
      Added.append(ZZ)
    else:
      print("\033[32mSpecify the type of constraint: ",i)
      Type=int(input("1_(Less than or equal) <= \n2_(equal)= \n3_(Greater than or equal)>= \n"))
      con.append(Type) #con is for type of constraint
      Addx=[]
      Printc=[]
      for j in range(0,V+1):
        if j==V:
          print("Please Enter C in Constraint: ",i)
          Xin=float(input())
          Addx.append(Xin)
          if Type==1:
            Printc.append("<= "+str(Xin))
          elif Type==2:
            Printc.append("= "+str(Xin))
          elif Type==3:
            Printc.append(">= "+str(Xin))
        else:
          print("Please enter the coefficient x",j+1,"In constraint: \033[32m",i)
          Xin=float(input())
          Addx.append(Xin)
          if Xin<0:
            Printc.append(str(Xin)+"x"+str(j+1))
          elif Xin>0:
            Printc.append("+"+str(Xin)+"x"+str(j+1))
      Added.append(Addx)
      Printcc=Printcc+[Printc]
  RHS=[]
  for i in range(0,len(Added)):
    RHS.append(Added[i][-1])
    Added[i].pop(-1)
  counter2=1
  counter3=1
  for i in range(1,len(con)+1):
    if con[i-1]==1: #Less than or equal Constraint
      Row=Row+["S"+str(counter2)]
      Colm=Colm+["s"+str(counter2)]
      counter2=counter2+1
      for j in range(0,len(Added)):
        if j != i:
          Added[j].append(0)
        else:
          Added[j].append(1)

    elif con[i-1]==2: #Equal Constraint
      Colm=Colm+["R"+str(counter3)]
      Row=Row+["R"+str(counter3)]
      counter3=counter3+1    
      for jj in range(0,len(Added)):
        if jj == 0:
          if Mode==1: #maximize
            Added[jj].append(-MM)
          elif Mode==2:#minimize
            Added[jj].append(MM)
        elif jj==i:
          Added[jj].append(1)
        elif (jj !=0 and jj !=i):
          Added[jj].append(0)
    elif con[i-1]==3: #Greater than or equal Constraint
      Colm=Colm+["s"+str(counter2)]
      Colm=Colm+["R"+str(counter3)]
      Row=Row+["R"+str(counter3)]
      counter2=counter2+1
      counter3=counter3+1
      for jjj in range(0,len(Added)):
        if jjj==0:
          if Mode==1:
            Added[jjj].append(0)
            Added[jjj].append(-MM)
          elif Mode==2:
            Added[jjj].append(0)
            Added[jjj].append(MM)
        elif jjj==i:
          Added[jjj].append(-1)
          Added[jjj].append(1)
        elif (jjj != 0 and jjj != i):
          Added[jjj].append(0)
          Added[jjj].append(0)
  for i in range(len(RHS)):
    Added[i].append(RHS[i])
  Added=np.array(Added)
  # xx=input()
  if Mode==1: #maximize
    Added[0]=-1*(Added[0])
  Added=np.array(Added).tolist()
  A=Added
  return A, Printcc, Zeroline, Colm, Row , Mode,V,con

#Graphic Method
def GraphicMethod(AA,Printcc, mode,con):
  
    # AA: Matrix that contains the linear system (With M) 
    # Printcc: List that contains the linear system (Strings)
    # Mode: Max or Min
    # con : table that indicates the signs of the constraints
    
    # ask for Objective function contours displaying
    contours=int(input("\033[32mDo you want to display Objective function contours ? 1) yes 2) No: \033[0m"))
    xopt=0
    yopt=0
    #preparation of constraints
    Legend=ConcatStringTables(Printcc)
    # solve LP
    m = GEKKO(remote=False)
    x,y = m.Array(m.Var,2,lb=0)
    #maximaze
    if (mode==1):
        for i in range(1,len(AA)):
            #Less than or equal Constraint
            if (con[i-1]==1):
                m.Equation(AA[i][0]*x+AA[i][1]*y<=AA[i][-1])
            #Equal Constraint
            elif(con[i-1]==2):
                m.Equation(AA[i][0]*x+AA[i][1]*y==AA[i][-1])
            elif(con[i-1]==3):
            #Greater than or equal Constraint
                m.Equation(AA[i][0]*x+AA[i][1]*y>=AA[i][-1])
        m.Maximize(-AA[0][0]*x-AA[0][1]*y)
    else:
    #minimize
        for i in range(1,len(AA)):
            #Less than or equal Constraint
            if (con[i-1]==1):
                m.Equation(AA[i][0]*x+AA[i][1]*y<=AA[i][-1])
            #Equal Constraint
            elif(con[i-1]==2):
                m.Equation(AA[i][0]*x+AA[i][1]*y==AA[i][-1])
            elif(con[i-1]==3):
            #Greater than or equal Constraint
                m.Equation(AA[i][0]*x+AA[i][1]*y>=AA[i][-1])
        m.Minimize(-AA[0][0]*x-AA[0][1]*y)
    try:
      m.solve(disp=False)
      xopt = x.value[0]; yopt = y.value[0]
    except:
      print("\033[31mWe did not find an optimal solution. Please check your Linear Program! \033[0m")
      if (mode==2):
        print("\033[31mTry to change the objective to Maximize! \033[0m")
      if (mode==1):
        print("\033[31mTry to change the objective to Minimize! \033[0m")
      print("\033[31mTry with the Big M method ! \033[0m")
    ## visualize solution
    g = np.linspace(0,5,10)
    [x,y] = np.meshgrid(g,g)
    obj = (-1*AA[0][0]*x)+(-1*AA[0][1]*y)

    # plot constraints
    x0 = np.linspace(0, 5, 100)
    for i in range(1,len(AA)):
        if(AA[i][1] !=0):
            plt.plot(x0,(AA[i][-1]-AA[i][0]*x0)/AA[i][1], label=Legend[i-1])
        else:
            co=AA[i][-1]/AA[i][0]
            plt.plot([co,co],[0,10], label=Legend[i-1])    
   
    # objective contours
    if (contours==1):
      CS = plt.contour(x,y,obj)
  
    # optimal point
    plt.plot([xopt],[yopt],marker='o',color='orange',markersize=10)
    plt.xlim(0,5); plt.ylim(0,5); plt.grid(); plt.tight_layout()
    plt.legend(loc=1); plt.xlabel('x'); plt.ylabel('y')
    plt.savefig('plot.png',dpi=300)
    plt.show()
    
# BiGM Method

def BigmMethod(A1, Printcc1, Zeroline1, Colm1, Row1 , Mode1):
  
  # A1: Matrix that contains the linear system (With M) 
  # Printcc1: List that contains the linear system (Strings)
  # Zeroline1: List that contains The objective function
  # Colm1,Row1: contains first row and column of table A (for display)
  # Mode: Max or Min
  
  # Ask for table displaying
  Displaytables= int(input("\033[32mDo you want to Display resolution across tables 1)Yes 2)No: \033[0m")) 
  # Setting the parameters of the table to display
  pd.set_option('display.max_columns', None)
  pd.set_option('display.max_rows', None)
  
  # replace 9999 with M in the display
  Mdisplay=sp.symbols("M")
  # Convert A To Table composed of floats
  A1=np.array(A1,dtype=float)
  Zero=[]
  # This for look for 9999 in A Table (Replace with ("M"))
  for i in range(len(A1[0])):
    if (A1[0][i] != MM):
      Zero.append(A1[0][i])
    else:
      # zero contained the first row with the display of M
      Zero.append(Mdisplay)
  # array B receives array A without the first Row
  B=np.delete(A1,0,axis=0)
  # Converting table B to a list
  B=np.array(B).tolist()
  # A1 presents the first Table which contains M (Before the definition of the pivot)
  AA=[]
  # Add the first row in the new AA table
  AA.append(Zero)
  for i in range(len(B)):
    AA.append(B[i])
  # A(For calculations) & AA(For Display)
  if(Displaytables==1):
    # Initial table display
    print("Initial Table: ")
    PrintTable(AA, Row1, Colm1)
  Mcolm=[]
  Mrow=[]
  for i in range(len(A1[0])):
    if (A1[0][i]==MM):
      Mcolm.append(i)   
  for i in range(1,len(A1)):
    for j in Mcolm:
      if A1[i][j]==1:
        Mrow.append(i)
  Mrow=np.array(Mrow)  # Mrow The line that contains an artificial variable
  
  #...q means for Display Like: rowq(For Display) row(For Calculations)
  #Prepare the First Table
  row=[]
  rowq=[]
  # Mrow The line that contains an artificial variable
  for i in Mrow:
    # calculate new values of Z with artificial variables
    row=-MM*(A1[i])
    rowq = [element*-Mdisplay for element in AA[i]]
    A1[0]=np.add(row,A1[0])
    AA[0]=np.add(rowq,AA[0])
    row=[]
  if(Displaytables==1):
    print("Table 2: ")
    PrintTable(AA, Row1, Colm1)
  xz=3 #(xz=Counter for Table Number)
  #___________________________________________________________________#
  MA=0
  while min(A1[0,:-1])<0 or MA==1: # Code repeats as long as the min of z <= 0
    if MA !=1:
      k=np.argmin(A1[0,:-1])  # pivot column search
    test=[]
    for i in range (1,A1.shape[0]): #row pivot search
      if (A1[i,k]<0) or (A1[i,k]==0):
        test.append(math.inf)  # replace negative values with -oo
        continue
      else:
        test.append(A1[i,-1]/A1[i,k]) # row pivot search
    test=np.array(test)
    #Degeneracy and Unbonded Testing Step
    s=0
    for i in test:
      if i == min(test[0:]):# row pivot search
        s=s+1
    if s>1 and min(test)!= math.inf: # several rows have the same result
      print("-----------(We have degeneracy in This Table)-----------")
    elif min(test)==math.inf: # unbound test
      print("-----------(We are unbonded in This Table)-----------")
      break
    n=int(np.argmin(test[0:]))+1
    ## replace pivot in 1
    PashneRow  = np.divide(A1[n], A1[n][k]) 
    PashneRowq = np.divide(AA[n], AA[n][k]) # division de la row pivot sur le point pivot
    A1=np.array(A1).tolist() # replace table A1 in list
    AA=np.array(AA).tolist() #replace table AA in list
    if(Displaytables==1):
      #display the coordinates of the pivot
      PrintPivotCoordinates(Colm1[k],Row1[n])
    Row1[n]=Colm1[k]     #Replace column instead of row for Print
    for j in range(len(A1)):
      Newrow=[] 
      if j==n:
        A1[n]  = np.divide(A1[n], A1[n][k]) # division de la row pivot sur le point pivot
        AA[n]=np.divide(AA[n], AA[n][k],dtype=float)
        continue
      else:
        # replace pivot column to 0 
        Newrow=PashneRow # PashneRow = pivot row
        Newrowq=PashneRowq
        Newrow=Newrow*(-1) # pivot row* (-1)
        Newrowq=Newrowq*(-1) # pivot row* (-1) (Display version)
        Newrow=Newrow*A1[j][k] 
        Newrowq=Newrowq*AA[j][k]
        Newrow=list(Newrow) # converting newrow to list
        Newrowq=list(Newrowq)#  # converting newrowq to list
        added=np.add(Newrow,A1[j])
        addedq=np.add(Newrowq,AA[j])
        A1[j]=list(added)
        AA[j]=list(addedq)
    A1=np.array(A1,dtype=float)
    limiti=0
    for i in range(0,len(A1[0])):
      limiti=sp.limit(AA[0][i],Mdisplay,0) # limiti: for calculating the limit de AA[0][i] pour  Mdisplay --> 0
      if math.isclose(limiti,A1[0][i]): # return true if the limit is tolerant
        AA[0][i]=A1[0][i]
    if(Displaytables==1): # ask for  Tables displaying
      print("Table",xz,":")
      PrintTable(AA, Row1, Colm1)
      xz=xz+1
    #Multi Answer Checking Step
    MA=0
  Righth=round(A1[0][-1],3)
  if Mode1==1 and min(test)!=math.inf:
    PrintSolution(Righth) #if the mode is max --> print solution
  elif Mode1==2 and min(test)!=math.inf:
    PrintSolution(-1*Righth)# if the mode is max multiply the solution by (-1)

  #Infeasible Test::
  Row1=str(Row1)
  if (Row1.find("R") != -1):
    print("\033[31mNote:\033[0m Impossible to answer ! ")
  
# Display of the main method
def MainMenuPrint():
    Colm=['\033[31mLinear Problem Optimization\033[0m' ]
    myTable = PrettyTable(Colm) ## initialize the array to display
    Row=[['Select linear program from memory  \n'],['Enter your own linear program in R \n'],['Enter your own linear program in Rn \n'],['Exit                               ']]
    myTable.add_rows(Row)  # Add Row to the table
    myTable.add_autoindex(' ')
    print(myTable) #Display

def main():
  MainMenuPrint() # Display of the main method
  Choice=int(input("\033[32m\nEnter your choice please: \033[0m"))
  print(Choice)
  if (Choice ==1): # Select linear program from memory
    clear_screen() # Clear screen
    SavedlinearProgram() 
  elif (Choice==2): # Enter your own linear program in R
    clear_screen() ## Clear screen
    A1, Printcc1, Zeroline1, Colm1, Row1 , Mode1,V1,Con1 =LinearSystemInput() #
    RandomlinearProgramInR(A1, Printcc1, Zeroline1, Colm1, Row1 , Mode1,V1,Con1)
  elif (Choice==3): # Enter your own linear program in Rn
    clear_screen() # Clear screen
    A1, Printcc1, Zeroline1, Colm1, Row1 , Mode1,V1,Con1 =LinearSystemInput() # Manual entry of a linear program
    BigmMethod(A1, Printcc1, Zeroline1, Colm1, Row1 , Mode1) # Launch of the bigM method
    exit0= int(input("\033[32mDo you want to continue ! 1) Yes 2) No: \033[0m")) # ask if you want to continue
    if(exit0==1):
      main() # yes condition
    else:
      exit() # else exit
  else:
    clear_screen()  # Clear screen
    print('End program...') # print End program message    
    exit()
 
main() # Launch of the program
