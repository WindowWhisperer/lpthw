# Inheritance vs Composition
# Interactions possible: Actions on the child imply an action on the parent, act on child overrides or alters parent
# class Foo(Bar) "Make a class Foo that inherits from Bar." So common functionality on Bar and specialize on Foo

class Parent(object):

    def override(self):
        print("PARENT override()")
        
    def implicit(self):
        print("PARENT implicit()")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):
    
    def override(self):
        print("CHILD, override()")

    def altered(self):
        print("CHILD, BEFORE PARENT (altered)")
        super(Child, self).altered()
        print("Child, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
