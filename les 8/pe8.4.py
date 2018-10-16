import math
studentencijfers_global = [[95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0]]


def gemiddelde_per_student(studentencijfers):
   gemiddelde = []
   for student_cijfers in studentencijfers:
       antw = sum(student_cijfers) / len(student_cijfers)
       gemiddelde.append(math.floor(antw))
   return gemiddelde


def gemiddelde_van_alle_studenten(studentencijfers):
    lijst = gemiddelde_per_student(studentencijfers)
    antw = sum(lijst) / len(lijst)
    return antw


print("gemiddelde cijfers van alle studenten {}\n".format(gemiddelde_per_student(studentencijfers_global)))


print("gemiddeld cijfer per student {}\n".format(gemiddelde_van_alle_studenten(studentencijfers_global)))