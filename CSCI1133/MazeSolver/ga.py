import maze
import maze_samples
import random

## IMPORTANT ##
'I didnt understand how the if __name__ thing worked, so you have to call main() manually'


''' Welcome
    To Yet Another Fun Programming Experience Brought To You By:
            Zachary Riehl
    This usually works on the smaller maze, but iterates EXTREMELY slowly so
    hopefully you don't have to watch it on a bigger maze....'''




            #there are multiple places where the Starting Position Must be
                            #put in if you don't use the smaller default maze
                            #each place is marked with RED comment text.
                            #they are all within the individual class also.



string_length = 11               #the length you want the individual strings
maze_list = maze_samples.maze[1] #maze path 
k = 'here'                       #nothing that matters
mutate_chance = 50               #chance of mutating, goes through each element of the string
population_size = 500            #size of population
max_generations = 500

class ga:
    def __init__(self,pop_size):
        self.ind_list = ['ind' + str(r) for r in range(pop_size)]
        self.population = dict((ind,individual()) for ind in self.ind_list)
        self.parent1 = None
        self.parent2 = None     #these should be strings
        self.population_alt = dict((ind,individual()) for ind in self.ind_list) #the second population dictionary
        self.values = [el for el in self.population.values()]
        self.keys = [el for el in self.population.keys()]
    def mutate(self,individ):
        mutate_list = list(individ.string)
        count = 0
        while count < len(mutate_list):
            rand_var = random.randint(1,100)
            #print(mutate_chance)
            #print(rand_var)
            if rand_var < mutate_chance:
                x = random.randint(1,4)
                if x == 1:
                    mutate_list[count] = 'U'
                if x == 2:
                    mutate_list[count] = 'D'
                if x == 3:
                    mutate_list[count] = 'L'
                if x == 4:
                    mutate_list[count] = 'R'
            count += 1
        individ.string = ''.join(mutate_list)

    def crossBreed(self,parent1,parent2): #parents brought in are the dict value, not string
        par1_list = list(parent1.string)
        par2_list = list(parent2.string)
        break_point = random.randint(int(string_length/4),int(3*string_length/4))
        #print(break_point)
        par1_A = par1_list[:break_point]
        par1_B = par1_list[break_point:]
        par2_A = par2_list[:break_point]
        par2_B = par2_list[break_point:]
        new1 = par1_A + par2_B
        new2 = par2_A + par1_B
        new_ind1 = ''.join(new1)
        new_ind2 = ''.join(new2)
        parent1.string = new_ind1
        parent2.string = new_ind2

    def SetWeightsForMonteCarloSelection(self,values):
        normalized_values = [int(v/sum(values)*100+.5) for v in values]
        accum = 0
        selection_weights = []
        for w in normalized_values:
            accum += w
            selection_weights.append(accum)
        return selection_weights

    def MonteCarloSelection(self,selection_weights):
        selection = random.randint(0,selection_weights[-1])
        for i,w in enumerate(selection_weights):
            if selection <= w:
                return i

        
                
            
            

            
#beware, if running individual tests the initialized vales are changed and must
#be reset between tests.
''' The fitness function is kinda cool in that the mouse only gets 'fitness points' for moving to tiles it hasn't been to before '''

            
class individual:
    def __init__(self):
        self.string = []
        self.start = [2,4] #starting position###############################################################################################################################
        self.fitness = None
        self.position_list = [[2,4]]# starting position in a nested list####################################################################################################
    def createString(self):
        count = 0
        string_list = []
        while count < string_length:
            x = random.randint(1,4)
            if x == 1:
                string_list.append('U')
            if x == 2:
                string_list.append('R')
            if x == 3:
                string_list.append('L')
            if x == 4:
                string_list.append('D')
            count += 1
        self.string = ''.join(string_list)
    def findFitness(self,maze_list): # its ya boi with the nested if loops
        fitness = 1                  # this is just a poorly written position checker, but it works for the small maze at least.
        pos_list = [[2,4]] # another place you need to put the initial position ############################################################################################
        for letter in self.string:
            temp_pos = []
            #print(pos_list)
            if letter == 'R':
                try:
                    if maze_list[self.start[0]][self.start[1]+1] == '-':
                        if [self.start[0],self.start[1]+1] not in pos_list:
                            temp_pos = [self.start[0],self.start[1]+1]
                            pos_list.append(temp_pos)
                            fitness += 2
                            #print(k)
                        self.start[1] += 1
                    if maze_list[self.start[0]][self.start[1]+1] == 'C':
                        if [self.start[0],self.start[1]+1] not in pos_list:
                            temp_pos = [self.start[0],self.start[1]+1]
                            pos_list.append(temp_pos)
                            fitness += 100
                            #print(k)
                        self.start[1] += 1
                    if maze_list[self.start[0]][self.start[1]+1] == 'M':
                        self.start[1] += 1
                    #print('Path A')
                except:
                    None
                    #print('Path B')
            if letter == 'L':
                try:
                    if maze_list[self.start[0]][self.start[1]-1] == '-':
                        if [self.start[0],self.start[1]-1] not in pos_list:
                            temp_pos = [self.start[0],self.start[1]-1]
                            pos_list.append(temp_pos)
                            fitness += 2
                            #print(k)
                        self.start[1] -= 1
                    if maze_list[self.start[0]][self.start[1]-1] == 'C':
                        if [self.start[0],self.start[1]-1] not in pos_list:
                            temp_pos = [self.start[0],self.start[1]-1]
                            pos_list.append(temp_pos)
                            fitness += 100
                            #print(k)
                        self.start[1] -= 1
                    if maze_list[self.start[0]][self.start[1]-1] == 'M':
                        self.start[1] -= 1
                    #print('Path A')
                except:
                    None
                    #print('Path B')
                    

            if letter == 'U':
                try:
                    if maze_list[self.start[0]+1][self.start[1]] == '-':
                        if [self.start[0]+1,self.start[1]] not in pos_list:
                            temp_pos = [self.start[0]+1,self.start[1]]
                            pos_list.append(temp_pos)
                            fitness += 2
                            #print(k)
                        self.start[0] += 1
                    if maze_list[self.start[0]+1][self.start[1]] == 'C':
                        if [self.start[0]+1,self.start[1]] not in pos_list:
                            temp_pos = [self.start[0]+1,self.start[1]]
                            pos_list.append(temp_pos)
                            fitness += 100
                            #print(k)
                        self.start[0] += 1
                    if maze_list[self.start[0]+1][self.start[1]] == 'M':
                        self.start[0] += 1
                    #print('Path A')
                except:
                    None
                    #print('Path B')
            if letter == 'D':
                try:
                    if maze_list[self.start[0]-1][self.start[1]] == '-':
                        if [self.start[0]-1,self.start[1]] not in pos_list:
                            temp_pos = [self.start[0]-1,self.start[1]]
                            pos_list.append(temp_pos)
                            fitness += 2
                            #print(k)
                        self.start[0] -= 1
                    if maze_list[self.start[0]-1][self.start[1]] == 'C':
                        if [self.start[0]-1,self.start[1]] not in pos_list:
                            temp_pos = [self.start[0]-1,self.start[1]]
                            pos_list.append(temp_pos)
                            fitness += 100
                            #print(k)
                        self.start[0] -= 1
                    if maze_list[self.start[0]-1][self.start[1]] == 'M':
                        self.start[0] -= 1
                    #print('Path A')
                except:
                    None
                    #print('Path B')
        self.start = [2,4] #yet another place to put the initial position
        self.fitness = fitness
##        print(fitness)
##        print(temp_pos)
##        print(self.start)
    





def main():
    # There are currently 2 samples in maze_samples.py
    GA = ga(population_size)
    for value in GA.population.values():
        value.createString()
        value.findFitness(maze_list)
    done = False
    solved_string = None
    iter_count = 0
    while done == False:
        iter_count += 1
        if iter_count >= max_generations:
            done = True
            solved_string = GA.population['ind55'].string
            #print(solved_string)
            #print(GA.population['ind50'].string)
        for i in range(len(GA.values)//2):
            values_list = [ind.fitness for ind in GA.values]
            p1 = GA.MonteCarloSelection(GA.SetWeightsForMonteCarloSelection(values_list))
            p2 = GA.MonteCarloSelection(GA.SetWeightsForMonteCarloSelection(values_list))
            p1_key = GA.keys[p1]
            p2_key = GA.keys[p2]
            GA.crossBreed(GA.population[p1_key],GA.population[p2_key])
        val_list = [val for val in GA.population.values()]
        for el in val_list[len(val_list)//2:]:
            GA.mutate(el)
        for value in GA.population.values():
            value.findFitness(maze_list)
        for value in GA.population.values():
            if value.fitness > 100:
                solved_string = value.string
                done = True
        print(iter_count)
            
    #print(GA.values[4].fitness)
    #print(GA.population['ind0'].fitness)
    test_case = 1
    M = maze.Maze(maze_samples.maze[test_case])
    string_length = maze_samples.string_length[test_case]
    M.Visualize()
    #M.RunMaze('RLUUURLLUUDR')
    #M.RunMaze('UULLRLDDDULR')
    #M.ResetMouse()
    M.RunMaze(solved_string)
    #print(GA.population['ind450'].string)
    

#if __name__=='__main__' :
    #main()
