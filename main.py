#! /usr/bin/env python
print ("hello world")

class Person():

    def __init__(self,*args,**kwds):
        # self.args=args
        # self.kwds=kwds
        self.mydatalist =["sdf","df"]

        self.biodata = dict(nama = "None",ulangtahun="dd")
        pass


class Personin(Person):

    def __init__(self,*args,**kwds):    
        super().__init__(*args,**kwds)

        # self.parent = parent
        # print(args[0])
        # print(self.mydatalist)
        # self.mydatalist.append(args)
        self.biodata.update(kwds)
        # # print(len(self.biodata))
        # if len(self.biodata)>2:
        #     print("error")
        #     self.biodata.popitem()
        # else:
        #     print("pass")

   
    # def __setattr__(self, name, value):
    #     print("Attempt to edit the attribute %s" %(name))





if __name__ == "__main__":
    # user1add =Personin(ulangtahun="ganti pokoke")
    user1add = Personin()
    print(user1add.biodata)
    print(user1add.mydatalist)
    
