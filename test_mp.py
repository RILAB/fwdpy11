import fwdpy11 as fp11
import fwdpy11.evolve
import multiprocessing as mp
from collections import Counter
import numpy as np

class RecordSFS:
    def __init__(self):
        self.data=[]
    def __call__(self,pop,generation):
        c=Counter()
        for m in pop.mcounts:
            if m > 0:
                c[m]+=1
        self.data.append((generation,c))

def evolve_and_return(args):
    N,seed=args
    pop = fp11.Spop(N)
    rec=RecordSFS()
    rng=fp11.GSLrng(seed)
    fwdpy11.evolve.evolve(pop,rng,1000,10000,0.001,0.001,rec)
    #OMG pops are now pickle-able!!!
    return (pop,rec)

if __name__ == "__main__":
    args=[(1000,seed) for seed in np.random.randint(0,42000000,10)]
    print(args)
    P=mp.Pool()
    res=P.imap(evolve_and_return,args)
    P.close()
    P.join()

    for r in res:
        print(r[0].mcounts,len(r[1].data))