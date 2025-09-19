from dottore import Dottore
from paziente import Paziente

class Fattura:

    def __init__(self, patient:list[str], doctor:Dottore, salary:int = 0):


        if doctor.isAValidDoctor():
            self.doctor = doctor
            self.patinet = []
            self.salary = salary
            self.fatture = len(patient)
        else:
            self.doctor = None
            self.patinet = None
            self.salary = None
            self.fatture = len(patient)
            print("Non è possibile creare la classe fattura poichè il dottore non è valido!")

    def getSalary(self):
        return self.doctor.getParcel() * self.fatture

    def getFatture(self):
        return self.fatture
    
    def addPatient(self, paziente: Paziente):

        