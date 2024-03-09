from django.db import models

# Create your models here.
class Degree(models.Model):
    code = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)
    duration = models.PositiveIntegerField(default=5)
    
    def __str__(self) -> str:
        txt = "{0} ({1} year(s))".format(self.name, self.duration)
        return txt
    
class Student(models.Model):
    id_card = models.CharField(max_length=8, primary_key=True)
    middlename = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    birthdate = models.DateField()
    
    sex = models.CharField(max_length=1, choices=[('M', 'Masculine'), ('F', 'Femenine')], default = 'F')
    degree = models.ForeignKey(Degree, null=False, blank = False, on_delete=models.CASCADE)
    validity = models.BooleanField(default=True)

    def fullname(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.lastname, self.middlename, self.firstname)
    
    def __str__(self) -> str:
        txt = "{0} / Degree: {1} / {2}"
        
        if self.validity:
            status = "VALID"
        else:
            status = "INVALID"
        
        return txt.format(self.fullname(), self.degree, status)
    
class Course(models.Model):
    code = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=50)
    credits = models.PositiveIntegerField(default=4)
    professor = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        txt = "{0} ({1})".format(self.name, self.code, self.professor)
        return txt
    
class Enrollment(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, null=False, blank = False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, blank = False, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now =True)
    
    def __str__(self) -> str:
        """ just for spanisch version
            if self.student.sex == 'F':
                lettersex = "a"
            
            else:
                lettersex = "o"
        """
        txt = "{0} - {1}-{2}- Professor:{3} ({4})"
        date_enrol = self.enrollment_date.strftime("%Y/%m/%d %H:%M:%S")
        return txt.format(self.student.fullname(), self.course.name,self.course.code, self.course.professor,date_enrol)