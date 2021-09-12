class Student(models.Model):
    pass
class Class(models.Model):
    pass




    
from django.db.models import Avg, Sum, Max, Min
    
def students_avg():
    return Student.objects.aggregate(Avg('score'))

def class_avgs():
    average_foreach_class = {}
    classes = Class.objects.all()
    for cl in classes:
        class_average = Student.objects.filter(class_room=cl).aggregate(Avg('score'))
        average_foreach_class.update({cl.name:class_average})


def calculate_number_of_products_without_enamad():
    count = 0
    for p in Product.objects.all().iterator():
        enamd_info = get_enamad_data(p.shop.domain)
        if enamad_info is None:
        count += 1
    return count