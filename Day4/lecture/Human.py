#define class
class Human:
    #class var---->value shared to all objects
    count=0
    #special or magical method

    def __init__(self,_id=None,_name=None,_add=None):#(1,2,3)

        #instnace variable--->value depend on object
        #validation
        if( _add is not None and  'fayoum' in _add):
            #intaliztion instance var
            self.id=_id
            self.name=_name
            self.add=_add
            Human.count+=1
        else:
            #'ali my own exception
            raise ('you must belong to fayoum')
        print('iam constructr',self)
    #instance method must be called by object
    def drink(self):
        print(self.name,'drinked')
    def eat(self):
        print(self.name,'eaten')
    def sleep(self):
        print(self.name,'sleep')
    @classmethod
    def getcount(cls):
        return cls.count #Human.count
    @classmethod
    def setcount(cls,newcount):
        if(newcount>0):
            cls.count=newcount
        else:
            raise (f'you have {cls.count }objects how  you want to set {newcount}')
    #logic related to human
    #depend object
    #accsess shared value of objects
    @staticmethod
    def measuretemp(temp):
        if(temp>37):
            print('too hot')
        elif(temp<37):
            print('too cold')
        else:
            print('normal')