import random


delfin_ut = [random.randint(-5, 3) for _ in range(80)]


viz_felett = len([x for x in delfin_ut if x >= 0])  
viz_alatt = len([x for x in delfin_ut if x < 0])   


osszes_elem = len(delfin_ut)


viz_felett_arany = viz_felett / osszes_elem  
viz_alatt_arany = viz_alatt / osszes_elem    


if viz_alatt > viz_felett:
    print("Több időt töltött a delfin a víz alatt.")
else:
    print("Több időt töltött a delfin a víz felett.")


print(f"Víz felett: ({viz_felett}/{osszes_elem})")
print(f"Víz alatt: ({viz_alatt}/{osszes_elem})")


max_kiugras_hossz = 0 
kiugras_kezd = -1      
aktualis_hossz = 0     
aktualis_kezd = -1 