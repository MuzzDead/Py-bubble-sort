do = str(input("Print *cut* to cut off the head of the hydra:"))
hydra = 1
hydracut = 1
if do == "cut":
    while hydra < 1024:
        hydra *= 2
        print(hydra, '1024 - because hydra have 1kb')

