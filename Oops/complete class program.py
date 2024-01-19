class Community:
    total_population = 0
    data = []

    def __init__(self, name, age, standard, alive=True,marriage=True):
        self.name = name
        self.age = age
        self.standard = standard
        self.alive = alive
        self.marriage=marriage
        Community.total_population += 1
        Community.data.append(name)
    # method 1
    # function decrease the population if some one die
    def dead(self):
        if self.alive:
            print(f'{self.name} is no more now')
            Community.total_population -= 1
            self.alive = False
        else:
            print(f'{self.name}is already died')
    # method 2
    # AFter some one married then 
    def marriage_fun(self):
        if self.marriage:
            print(f'Congratulation for being married .Welcome {self.name} in our community.')
            Community.total_population += 1
            self.marriage = False
        
        else:
            print("already married")

x = Community('x', 84, '+2 pass')
y = Community('y', 82, '10 pass')
x.dead()
c = Community('c', 24, "bsc")
c.marriage_fun()
rs = Community("rs", 24, 'bbs')
rs.marriage_fun()
rs.marriage_fun()

print(f'Total Population = {Community.total_population}')
