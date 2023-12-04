import numpy as np

posi = [0,1,2,3,4,5]
buffe = [0,1,2,3]
states = []

for poseUE1x in posi:
    for poseUE1y in posi:
        for poseUE2x in posi:
            for poseUE2y in posi:
                for bufferUE1 in buffe:
                    for bufferUE2 in buffe:
                        state = ((poseUE1x, poseUE1y), (poseUE2x, poseUE2y), (bufferUE1, bufferUE2))
                        if (state[0] == state[1]) or (state[0] == (0,5)) or (state[1] == (0,5)):
                            continue
                        else:    
                            states.append(state)


mdp = np.zeros([len(states), 2, len(states)])

spec_eff_matrix = [[1, 1, 1, 1, 1, 1],
                   [2, 2, 2, 2, 2, 1],
                    [2, 2, 2, 2, 2, 1],
                    [3, 3, 2, 2, 2, 1],
                    [5, 5, 3, 2, 2, 1],
                    [0, 5, 3, 2, 2, 1]]

for s in range(len(states)):
    redorUE1 = ((states[s][0][0] + 1, states[s][0][1]), (states[s][0][0] - 1, states[s][0][1]),
                         (states[s][0][0], states[s][0][1] + 1 ), (states[s][0][0], states[s][0][1] - 1))
    redorUE2 = ((states[s][1][0] + 1, states[s][1][1]), (states[s][1][0] - 1, states[s][1][1]),
                         (states[s][1][0], states[s][1][1] + 1 ), (states[s][1][0], states[s][1][1] - 1))
    espec = (spec_eff_matrix[states[s][0][0]][states[s][0][1]], spec_eff_matrix[states[s][1][0]][states[s][1][1]])
    for a in range(2):
        auxbf = states[s][3][a] - espec[a]
        if auxbf < 0:
                auxbf = 0

        if a == 0: 
            nbuf = (auxbf, states[s][3][1])
        elif a == 1:
            nbuf = (states[s][3][0], auxbf)
        for sp in range(len(states)):
            a =2
         


