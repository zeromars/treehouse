from peewee import *

db = SqliteDatabase('students.db')

#always use singular names (it represents one item in the db)
class Student(Model):
    username = CharField(max_length=255, unique=True)
    points = IntegerField(default=0)

    #defines what db this class belongs to
    class Meta:
        database = db

students = [
    {'username': 'koda', 'points': 1234},
    {'username': 'erin', 'points': 5678},
    {'username': 'landon', 'points': 9101112}
]

def add_students():
    for student in students:
        try:
            Student.create(username=student['username'], points=student['points'])
        except IntegrityError:
            student_record = Student.get(username=student['username'])
            student_record.points = student['points']
            student_record.save()

def top_student():
    student = Student.select().order_by(Student.points.desc()).get()
    # select gets all
    # get gets one
    return student

#if the file is load directly and not imported
if __name__ == '__main__':
    db.connect()
    db.create_tables([Student], safe=True)
    add_students()
    print("this guys has the most points {0.username}".format(top_student()))