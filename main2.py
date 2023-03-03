from constraint import Problem


#def coloring_map():
    # Part 1 - we will do this together in class.
    #p = Problem()
    #p.addvariable("WA", ["Red", "Green", "Blue"])
    #p.addvariable("NT", ["Red", "Green", "Blue"])
    #p.addvariable("SA", ["Red", "Green", "Blue"])
    #p.addvariable("Q", ["Red", "Green", "Blue"])
    #p.addvariable("NSW", ["Red", "Green", "Blue"])
    #p.addvariable("V", ["Red", "Green", "Blue"])
    #p.addvariable("T", ["Red", "Green", "Blue"])
    
    
    #p.addConstraint(lambda a,b: a != b, ("WA","NT"))
    #p.addConstraint(lambda a,b: a != b, ("WA","SA"))
    #p.addConstraint(lambda a,b: a != b, ("SA","NT"))
    #p.addConstraint(lambda a,b: a != b, ("SA","Q"))
    #p.addConstraint(lambda a,b: a != b, ("SA","NSW"))
    #p.addConstraint(lambda a,b: a != b, ("SA","V"))
    #p.addConstraint(lambda a,b: a != b, ("NT","Q"))
    #p.addConstraint(lambda a,b: a != b, ("Q","NSW"))
    #p.addConstraint(lambda a,b: a != b, ("V","NSW"))
    #pass





def scheduling_problem():
    # Look at "Part 2" instructions and do that here.
    p = Problem()
    p.addVariable("Alice", ["Monday", "Wednesday", "Friday"])
    p.addVariable("Bob", ["Monday", "Tuesday"])
    p.addVariable("Charlie", ["Tuesday", "Wednesday", "Thursday","Friday"])
    p.addVariable("Danielle", ["Monday", "Wednesday", "Friday"])
    p.addVariable("Edwin", ["Wednesday", "Thursday", "Friday"])
    
    s1 = p.getSolution()
    print(s1)
    #pass

    p.addConstraint(lambda a,b: a != b, ("Danielle","Charlie"))
    p.addConstraint(lambda a,b: a != b, ("Bob","Charlie"))
    p.addConstraint(lambda a,b: a != b, ("Danielle","Edwin"))
    p.addConstraint(lambda a,b: a != b, ("Danielle","Alice"))
    p.addConstraint(lambda a,b,c: a == b or a == c, ("Edwin","Bob","Charlie"))

    s2 = p.getSolution()
    print(s2)
    #pass


def main():
  #coloring_map()
  scheduling_problem()
  

if __name__ == "__main__":
  main()