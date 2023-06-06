simulations = [
    { "test": 1},
    { "test": 2},
    { "test": 3},
]

for s in simulations:
    print(s['test'])
    
    
print([simulation["test"]*2 for simulation in simulations])