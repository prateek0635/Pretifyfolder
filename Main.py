import os
#os.rename("DonotAlter.tx","DonotAlter.txt")
def Check(path,filename,ext,temp):
    if os.getcwd()!=path:
        os.chdir(path)
    list1=os.listdir(path)
    for i in list1:
        if os.path.isfile(i):
            os.rename(i,i.capitalize())
    # print(os.listdir(path))
    var=1
    for j in list1:
        try:
            fname,fext=j.split(".")
            #print(fname,fext)
            if fext==ext:
                os.rename(j,f"{var}.{fext}")
                var+=1
        except:
            pass


if __name__ == '__main__':
    lis=[]
    path="C:\\Users\PRATEEK GUPTA\PycharmProjects\\untitled2" #Change this path #Take it as a Input if you want
    filename="Prateek_Book.txt"  #Change this FileName #Take it as a Input if you want
    temp = open(filename, 'r').read().split('\n')
    ext="jpg" #Take it as a Input if you want

    # print(temp)
    Check(path,filename,ext,temp)
