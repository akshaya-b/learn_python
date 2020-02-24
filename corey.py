class Tree:

    #class variable
    nooftrees=0
    noofbrances=1.05
    def __init__(self,name,age,region):
        self.name=name
        self.age=age
        self.region=region
        self.biology= name +"-"+ region
        Tree.nooftrees +=1

    def morphology(self):
        return (str(self.age) + self.region)

    def branches(self):
        return Tree.noofbrances * self.age

tree1=Tree('neem',20,'india')
tree2=Tree('pine',50,'uk')
print(tree1.biology)
print(Tree.morphology(tree1))
print(tree2.morphology())

#class variable output
print(Tree.nooftrees)
print(tree1.branches())
tree1.noofbrances=1.08
print(tree1.noofbrances)
print(tree2.noofbrances)
print(Tree.noofbrances)