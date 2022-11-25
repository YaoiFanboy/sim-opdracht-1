import random
class FSM():
    def __init__(self):
        self.states = []
        self.alfabet = []
        self.start_states = []
        self.end_states = []
        self.deltas = []

            #FSM maken
        #self.FSM = FSM()
        #self.FSM.add_state('p1 attack')
        #self.FSM.add_state('p2 attack') 
        #self.end_states('P1 Verliest')
        #self.end_states('P2 verliest') 
        #self.start_states('Keuze P')
        #self.FSM.add_delta('Keuze P')
        #self.FSM.add_delta('Keuze P', '1, 2, 3,', 'pl attack') 
        #self.FSM.add_delta('Keuze P', '1, 2, 3,', 'p2 attack')
        #self.FSM.add_delta('pl attack','1,2,3,4','p2 attack') 
        #self.FSM.add_delta('p2 attack','1,2,3,4','p1 attack') 
        #self.FSM.add_delta('p1 attack', 'Hp <=0', 'p1 Verliest') 
        #self.FSM.add_delta('p2 attack', 'Hp <=0','p2 Verliest')
        #self.FSM.alfabet('>3', '<string>','1,2,3', '1,2,3,4','Hp <=0')


    def add_delta(self, a,b,c):
        self.deltas.append((a,b,c))

    def set_start(self, names):
        self.start_states = names

    def set_end(self,names):
        self.end_states = names

    def add_state(self, name):
        self.states.append(name)

    def set_alfabet(self, alfabet):
        self.alfabet = alfabet 


class Pokemon(object):
    
 def __init__(self,name,hp,moves,attack,defense,types):
        self.name=name
        self.hp=hp
        self.moves= moves
        self.attack=attack
        self.defense=defense
        self.types=types
        




 def get_name(self):
    return self.name
 
 def get_hp(self):
    return self.hp
 
 def get_attack(self):
    return self.attack
 
 def get_defense(self):
    return self.defense
 
 def get_type(self):
    return self.types
 
 def battle(self, EnemyPokemon):
    print(f"\n{self.name}")
    print("Types/",self.types)
    print("HP/", self.hp)
    print("Attack/", self.attack)
    print("Defense", self.defense)
    

    
    print(f"\n{EnemyPokemon.name}")
    print("Types/", EnemyPokemon.types)
    print("HP/", EnemyPokemon.hp)
    print("Attack/", EnemyPokemon.attack)
    print("Defense/", EnemyPokemon.defense)
    
    # de steen papier schaar for loop.
    type = ['Fire', 'Water', 'Grass']
    #https://realpython.com/python-enumerate/
    for x,y in enumerate(type):
        if self.types == y:
            # Zelfde type
            if EnemyPokemon.types == y:
                string_1_attack = '\nHet is niet erg effectief...'
                string_2_attack = '\nHet is niet erg effectief...'


            # EnemyPokemon heeft type advantage
            if EnemyPokemon.types == type[(x+1)%3]:
                EnemyPokemon.attack *= 2
                self.attack /= 2
                self.defense /= 2
                string_1_attack = '\nHet is niet erg effectief...'
                string_2_attack = '\nHet is erg effectief!'


            # EnemyPokemon heeft negatieve type 
            if EnemyPokemon.types == type[(x+2)%3]:
                self.attack *= 2
                EnemyPokemon.attack /= 2
                EnemyPokemon.defense /= 2
                string_1_attack = '\nHet is erg effectief!'
                string_2_attack = '\nHet is niet erg effectief...'
            
    while (self.hp > 0) and (EnemyPokemon.hp > 0):
            # hp van beide pokemons weergeven
            print(f"\n{self.name}\t\thp\t{self.hp}")
            print(f"{EnemyPokemon.name}\t\thp\t{EnemyPokemon.hp}\n")
            print(f"Go {self.name}!")
            print("FSM state: p1 attack")

            for x, y in enumerate(self.moves):
                print(f"{x+1}.", y)
            i= int(input('Kies een aanval: '))
            print(f"\n{self.name} gebruikte {self.moves[i-1]}!")
            print(string_1_attack)

            # Weer de damage check
            EnemyPokemon.hp -= (self.attack - EnemyPokemon.defense)

            print(f"\n{self.name}\t\thp\t{self.hp}")
            print(f"{EnemyPokemon.name}\t\thp\t{EnemyPokemon.hp}\n")


            # EnemyPokemon gefaint ja/nee
            if EnemyPokemon.hp <= 0:
                print("\n..."+ EnemyPokemon.name + ' is neer!.')
                print("FSM state: p2 Verliest")
                break

            # EnemyPokemon turn
            print(f"Go {EnemyPokemon.name}!")
            print("FSM state: p2 attack")

            for x, y in enumerate(EnemyPokemon.moves):
                print(f"{x+1}.", y)
            i = int(input('Kies een aanval: '))
            print(f"\n{EnemyPokemon.name} gebruikte {EnemyPokemon.moves[i-1]}!")
            print(string_2_attack)

            # insane formule voor damage
            self.hp -= (EnemyPokemon.attack - self.defense)
            
            # eerste pokemon gefaint ja/nee
            if self.hp <= 0:
               print("\n..." + self.name + ' is neer!.')
               print("FSM state: p1 Verliest")
               break        

def choose():
    print("kies je pokemons! \n 1. Ninetails vs Piplup, 2. Sprigatito vs Leafeon, 3 Random vs random")
    print("FSM state: Keuze P")
    try:
        user_choice = int(input())
        if user_choice == 1:
            Ninetails.battle(Piplup) 
        elif user_choice == 2:
            Sprigatito.battle(Leafeon) 
        elif user_choice == 3:
            randlist = [Ninetails,Piplup,Sprigatito,Leafeon,LordAndSaviourCaterpie]
            random_num1 = random.choice(randlist)
            random_num2 = random.choice(randlist)
            random_num1.battle(random_num2)
        
        elif user_choice >=3:
            print("Dat is geen 1,2 of 3!")

    except ValueError:
        print("alleen cijfers!")



if __name__ == '__main__':
    
    Ninetails = Pokemon('Ninetails',100,['Flash Fire', 'Incinerate', 'Flamewheel', 'Ember'],40,5,'Fire')
    Piplup = Pokemon('Piplup', 100, ['Aqua Jet', 'Aquatail', 'Scald', 'Dive'],40,6,'Water')
    Sprigatito = Pokemon('Sprigatito',120,['Flower trick', 'Trail blaze', 'Absorb', 'Mega drain'],40,8,'Grass')
    Leafeon = Pokemon('Leafeon',110,['Grass knot', 'Flower trick', 'Seed bomb', 'Vine whip'],40,5,'Grass')
    LordAndSaviourCaterpie = Pokemon('LordAndSaviourCaterpie',600,['Muddy Water', 'Rain Dance', 'Hydro Pump', 'Splash'],200,10,'Water')

    choose()
    
    
    

