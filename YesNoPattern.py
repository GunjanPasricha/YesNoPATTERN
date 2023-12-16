def no_yes():
    string=" "
    a = 6
    p=8
    c =12
    d=0
    b=0
    for j in range(8):
        ispace = string*(j)
        p = p-1
        dspace = string*(p)
        if a>=0 and b<=12:
          sspace = string*(a)
          a=a-2
          fspace = string*(b) 
          b=b+4
        else:
             sspace = string*(d)
             d=d+2
             fspace = string*(c)
             c=c-4
             
             
        print(f"yes{ispace}yes{dspace}yes  {sspace}yes{fspace}yes")
no_yes()