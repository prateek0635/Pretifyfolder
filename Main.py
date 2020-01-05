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
    path="C:\\Users\PRATEEK GUPTA\PycharmProjects\\untitled2"
    filename="Prateek_Book.txt"
    temp = open(filename, 'r').read().split('\n')
    ext="jpg"

    # print(temp)
    Check(path,filename,ext,temp)
