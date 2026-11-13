# Pyxel Studio

import pyxel

class Jeu:
    def __init__(self):
        pyxel.init(256,256, title="Nuit du C0de")
        pyxel.load("theme2.pyxres")
        pyxel.mouse(True)
        self.joueur = Joueur()
        self.monde = Map()
        self.monde.monde[self.joueur.joueur_y][self.joueur.joueur_x] = -1
        self.pause = False
        pyxel.run(self.update, self.draw)
        
    def update(self):
        
        if self.pause == False : 
            
            
            if self.joueur.win == False : 
                
                if pyxel.btnp(pyxel.KEY_P) : 
                    self.pause = True
                
                self.joueur.deplacement(self.monde.monde)
                self.joueur.miner(self.monde.monde)
                
                if self.joueur.costume == 3 : 
                    self.joueur.costume = 0 
            
                if self.joueur.costume == 4 : 
                    self.joueur.costume -= 1  
                
                if 3 > self.joueur.costume > 0 : 
                    self.joueur.costume -=1
                    
                
                
    
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) and (15>pyxel.mouse_x//16>=14) and (9>pyxel.mouse_y//16>=8) : 
                    if self.joueur.gold >= self.joueur.upgrade_gold  : 
                        self.joueur.upgrade+= 1 
                        self.joueur.gold -= self.joueur.upgrade_gold
                        self.joueur.upgrade_gold = self.joueur.upgrade_gold*2+1
            else : 
                if pyxel.btnp(pyxel.KEY_R) : 
                    self.joueur = Joueur()
                    self.monde = Map()
                    self.monde.monde[self.joueur.joueur_y][self.joueur.joueur_x] = -1
        else : 
            if pyxel.btnp(pyxel.KEY_P) : 
                self.pause = False
    
    def draw(self):
        pyxel.cls(0)
        if self.pause == False : 
            if self.joueur.win == False : 
                for i in range(16) : 
                    for j in range(16) : 
                         
                        if self.monde.monde[i+self.joueur.joueur_y-6][j] == -1 : 
                            self.joueur.draw()
                        
                        if self.monde.monde[i+self.joueur.joueur_y-6][j] == 1 : 
                            pyxel.blt(j * 16, i * 16, 0, 16,112, 16,16,0)
                        
                        
                        if self.monde.monde[i+self.joueur.joueur_y-6][j] == 5 : 
                            pyxel.blt(j * 16, i * 16, 0, 64,112, 16,16,0)
                        if self.monde.monde[i+self.joueur.joueur_y-6][j] == 2 : 
                            pyxel.blt(j * 16, i * 16, 0, 0,112, 16,16,0)
                            
                        if self.monde.monde[i+self.joueur.joueur_y-6][j] == 3 : 
                            pyxel.blt(j * 16, i * 16, 0, 32,112, 16,16,0)
                        if self.monde.monde[i+self.joueur.joueur_y-6][j] == 4 : 
                            pyxel.blt(j * 16, i * 16, 0, 48,112, 16,16,0)
                        if self.monde.monde[i+self.joueur.joueur_y-6][j] == 6 :
                            pyxel.blt(j * 16, i * 16, 0, 48,112, 16,16,0)
                            pyxel.blt(j * 16, i * 16, 0, 0,16, 16,16,0)   
                 
                 
                pyxel.rect(14*16-3,6,8,8,0)          
                pyxel.text(14*16-3, 6, str(self.joueur.gold), 12)
                pyxel.blt((14*16)+5, 5, 0, 16,16, 16,16,0)
                
                
                pyxel.rect(14*16,9*16,8,8,0)
                
                if self.joueur.upgrade_gold-self.joueur.gold > 0 : 
                    pyxel.text(14*16, 9*16+2, str(self.joueur.upgrade_gold-self.joueur.gold), 12)
                    pyxel.blt(14*16, 8*16, 0, 0,96, 16,16,0)
                else : 
                    pyxel.text(14*16+1, 9*16+2, str(0), 12)
                    pyxel.rect(16,16,100,8,0)
                    pyxel.text(1*16, 1*16, "Amelioration disponible", 12)
                
                    
                    pyxel.blt(14*16, 8*16, 0, 16,96, 16,16,0)
                
                if self.joueur.upgrade == 0 : 
                    pyxel.blt(1*16, 14*16, 0, 0,64, 16,16,7)
                if self.joueur.upgrade == 1 : 
                    pyxel.blt(1*16, 14*16, 0, 32,64, 16,16,7)
                if self.joueur.upgrade >= 2 : 
                    pyxel.blt(1*16, 14*16, 0, 48,64, 16,16,7)
            else : 
                pyxel.text(15,64, "Bravo vous avez gagne, appuyez sur 'R' pour recommencer",7)
                pyxel.blt(7*16, 9*16, 0, 16,80, 16,16,0)
        else : 
            pyxel.blt(7*16, 8*16, 0, 0,80, 16,16,0)  
        
        
        
class Joueur:
    def __init__(self):
        self.joueur_x = 7
        self.joueur_y = 6
        self.outils = ["peb", 'pib', 'pif']
        self.upgrade = 0 
        self.gold = 0 
        self.upgrade_gold = 10
        self.costume = 0
        self.win = False
  
        
 
       
    
    def draw(self):
        
        pyxel.blt(self.joueur_x*16, 6*16, 0, self.costume*16, 0, 16, 16, 0)
    
    def deplacement(self, liste):
        if pyxel.btnp(pyxel.KEY_RIGHT) and self.joueur_x !=15 and liste[self.joueur_y][self.joueur_x+1] == 0   : 
            liste[self.joueur_y][self.joueur_x] = 0
            
            self.joueur_x += 1 
            self.costume = 2
            
            liste[self.joueur_y][self.joueur_x] = -1
        if pyxel.btnp(pyxel.KEY_LEFT) and self.joueur_x !=0 and liste[self.joueur_y][self.joueur_x-1] == 0   : 
            liste[self.joueur_y][self.joueur_x] = 0
            
            self.joueur_x -= 1
            self.costume = 2
            
            liste[self.joueur_y][self.joueur_x] = -1
        
        if pyxel.btnp(pyxel.KEY_DOWN) and liste[self.joueur_y+1][self.joueur_x] == 0 and self.joueur_y != max(liste) : 
            liste[self.joueur_y][self.joueur_x] = 0
            
            self.joueur_y += 1 
            self.costume = 4
            liste[self.joueur_y][self.joueur_x] = -1
        
        if pyxel.btnp(pyxel.KEY_UP) and liste[self.joueur_y-1][self.joueur_x] == 0 and self.joueur_y > 6  : 
            liste[self.joueur_y][self.joueur_x] = 0
            
            self.joueur_y -= 1 
            self.costume = 4
            liste[self.joueur_y][self.joueur_x] = -1
    
    
    def miner(self, liste) : 
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) : 
            print("############################")
            print(pyxel.mouse_x//16  , self.joueur_x+1)
            print(pyxel.mouse_x//16  , self.joueur_x)
            print(pyxel.mouse_x//16  , self.joueur_x-1)
            print("")
            print(pyxel.mouse_y//16  , self.joueur_y+1)
            print(pyxel.mouse_y//16  , self.joueur_y)
            print(pyxel.mouse_y//16  , self.joueur_y-1)
            print("")
            
            if (pyxel.mouse_x//16  == self.joueur_x+1 or pyxel.mouse_x//16 == self.joueur_x-1 or pyxel.mouse_x//16 == self.joueur_x ) and ((pyxel.mouse_y//16) + (self.joueur_y-6) == self.joueur_y+1 or (pyxel.mouse_y//16) + (self.joueur_y-6) == self.joueur_y-1 or (pyxel.mouse_y//16) + (self.joueur_y-6) == self.joueur_y) : 
                if liste[(pyxel.mouse_y//16) + (self.joueur_y-6)][pyxel.mouse_x//16] == 2 and self.upgrade >= 0 :
                    liste[(pyxel.mouse_y//16) + (self.joueur_y-6)][pyxel.mouse_x//16] = 0
                    self.gold += 1
                if liste[(pyxel.mouse_y//16) + (self.joueur_y-6)][pyxel.mouse_x//16] == 3 and self.upgrade >= 1 :
                    liste[(pyxel.mouse_y//16) + (self.joueur_y-6)][pyxel.mouse_x//16] = 0
                    self.gold += 2
                if liste[(pyxel.mouse_y//16) + (self.joueur_y-6)][pyxel.mouse_x//16] == 4 and self.upgrade >= 2 :
                    liste[(pyxel.mouse_y//16) + (self.joueur_y-6)][pyxel.mouse_x//16] = 0
                    self.gold += 3
                if liste[(pyxel.mouse_y//16) + (self.joueur_y-6)][pyxel.mouse_x//16] == 1 and self.upgrade >= 0 :
                    liste[(pyxel.mouse_y//16) + (self.joueur_y-6)][pyxel.mouse_x//16] = 0
                    self.gold += 1
                if liste[(pyxel.mouse_y//16) + (self.joueur_y-6)][pyxel.mouse_x//16] == 6 and self.upgrade >= 2 :
                    liste[(pyxel.mouse_y//16) + (self.joueur_y-6)][pyxel.mouse_x//16] = 0
                    self.gold = 9e99
                    self.win = True
                
    
    

class Map : 
    def __init__(self) :
        
        self.monde = [[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16,[0]*16]
        
        self.monde += [[1,1,1,1,1,1,1,5,1,1,1,1,1,1,1,1]]
        self.monde += [[2] * 16]
        k = 2
        for j in range(25) : 
            if j > 8 : 
                k = 3
            if j > 18 : 
                k = 4
            self.monde += [[k] * 16]
        self.monde[len(self.monde)-1][15] = 6
        self.monde += [[5]*16,[5]*16,[5]*16,[5]*16,[5]*16,[5]*16,[5]*16,[5]*16,[5]*16]
     
        print(self.monde)
            
                
        
Jeu()