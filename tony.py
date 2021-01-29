class Parent(object):
    def altered(self):
        print "Parent altered"

class Child(Parent):
    def altered(self):
        print "CHILD before parent altered()"
        super(Child,self).altered()
        print "CHILD after parent alteered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()