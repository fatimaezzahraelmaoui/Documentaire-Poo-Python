class Documaentaire:
    nbr = 0
    def __init__(self,titre,date1):
        self.__titre = titre
        self.__datesortie = date1
        self.__code = Documaentaire.nbr
        Documaentaire.nbr += 1
        
    def getcode(self):
        return self.__code
    def gettitre(self):
        return self.__titre
    def settitre(self,titre):
        self.__titre = titre
    def getdate_de_sortie(self):
        return self.__datesortie
    def setdate_de_sortie(self,date1):
        self.__datesortie = date1
    def getcode(self):
        return self.__code
    
    
    def ToString(self):
        return ("titre :",self.__titre , "date de sortie :", self.__datesortie
                , "code :", self.__code)
    def Equals(self,date):
        if self.__datesortie == date :
            return True
        else :
            return False

class Exemplaire(Documaentaire):
    def __init__(self,titre,date1,numéro,date2):
        Documaentaire.__init__(self,titre,date1)
        self.__titre = titre
        self.__datesortie = date1
        self.__code = Documaentaire.nbr
        self.__numéro = numéro
        self.__date_de_dachat =  date2
        
    def getnuméro(self):
        return self.__numéro
    def setnuméro(self,numéro):
        self.__numéro = numéro
    def getdate_de_dachat(self):
        return self.__date_de_dachat
    def setdate_de_dachat(self,date2):
        self.__date_de_dachat = date2
        
    def ToString(self):
        return ("titr est :",self.__titre ,"date de sortue :", self.__datesortie , 
                "numéro est :",self.__numéro, "date de dachat :", self.__date_de_dachat)
    def Equals(self,numéro):
        if self.__numéro == numéro:
            return True
        else :
            return False

DOC = Documaentaire("sarati","1/2/2003")
DOC1 = Documaentaire("ralhi","6/3/1765")
print(DOC.ToString())
print(DOC.nbr)
print(DOC.Equals("2/4/2004"))
print(DOC1.getcode())
EX1 = Exemplaire("hassani","31/4/2003",32,"21/8/1999")
print(EX1.ToString())
print(EX1.Equals(12))
