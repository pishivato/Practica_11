import random
f_name = "practica11.csv"

class Alumno:
    
    #constructor
    def __init__(self, name, numb, grades, avarage, f_name) -> None:
        self.name = name
        self.numb = numb
        self.grades = grades
        self.avarage = avarage
        self.f_read(f_name)

    def f_read(self, f_name):
        total = []
        with open(f_name, "r") as f:
            for i in f:
              a = i.split(",")
            for i in a:
                try:
                    total.append(int(i))
                except ValueError:
                    pass    
        self.f_rand(total)

    def f_rand(self, list):
        while(true):
            self.grades.append(random.choice(list))
            if len(self.grades) == 7:
                break
        self.prom()
    
    def prom(self):
        aux = 0
        for i in self.grades:
            aux += i
        self.avarage = aux/len(self.grades)
        self.info()

    def info(self):
        print(f"Nombre: {self.name}\n")
        print(f"Matricula: {self.numb}\n")
        print("Calificaciones: ")
        for i in self.grades:
            print(f"->{i}", sep="-")
        print(f"Promedio: {self.avarage}")
        self.f_write()
    
    def f_write(self):
        with open("students.txt", "a") as s:
            s.write(f"Nombre: {self.name}\n")
            s.write(f"Matricula: {self.numb}\n")
            s.write("Calificaciones: ")
            for i in self.grades:
                s.write(f"-> {i}")
                s.write("\n")
            s.write(f"Promedio: {self.avarage}\n\n")

        print("Los datos se guardaron conexito!!")                
        
if __name__ == '__main__':
    Alumno("Pedro", 126489, [], None, f_name)
    Alumno("Maria", 126978, [], None, f_name)
    Alumno("Josefa", 126519, [], None, f_name)
