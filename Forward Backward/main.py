import numpy as np

def calculateStableStates(T, T_1, O, prior, evidences):
    f = prior;
    for e in evidences:
        O_temp = O[0] if e==True else O[1];
        # Perform f = O * T' * f
        f = np.matmul( np.matmul(O_temp,T.transpose()), f );
        f = f/np.sum(f);

    prev_f = np.zeros((2,1));
    k=0
    while( np.all( np.absolute(prev_f-f) ) > 0.001):
        prev_f = f;
        f = np.matmul(T_1.transpose(), f);
        f = f/np.sum(f);
        k=k+1;
        print(f[0]);
    print( "Converged Probabilities after k="+ str(k) +" steps : "); print(f);



def calculateSmoothing(T ,O, prior, evidences, position):
    f = prior;
    for i in range(0, position):
        e = evidences[i];
        O_temp = O[0] if e==True else O[1];
        # Perform f = O * T' * f
        f = np.matmul( np.matmul(O_temp,T.transpose()), f );
        f = f/np.sum(f);

    b = np.array( [ [1.0], [1.0] ] );
    for i in reversed(range(position, len(evidences))):
        e = evidences[i];
        O_temp = O[0] if e==True else O[1];
        b = np.matmul( np.matmul(T, O_temp), b );
        b = b/np.sum(b);

    result = np.array(f) * np.array(b);
    result = result/np.sum(result);
    print( "Smoothed Probabilities at state="+ str(position) +" : ");print(result);



# Enter transition probabilities
T = np.array( [ [0.75, 0.25], [0.25, 0.75] ]);
# Enter transition probabilities for prediction
T_1 = np.array( [ [0.81, 0.19], [0.16, 0.84] ]);
# Enter Evidence probabilities as a diagonal matrix
O = [ np.array( [ [0.71, 0], [0, 0.01] ] ), np.array( [ [0.29, 0],[0, 0.99] ] ) ];
# Enter prior state probabilities
prior = np.array( [ [0.2], [0.8] ] );
# Enter sequence of evidences
evidences = [True,False,True,False,True,False];

# Calculates stable states (infinite prediction)
calculateStableStates(T, T_1, O, prior, evidences);

# Calculates smoothing
calculateSmoothing(T, O, prior, evidences, 3);
