import unittest
import fwdpy11 as fp11
import fwdpy11.multilocus as fp11m
import fwdpy11.fitness as fp11w
import numpy as np

class testMultiLocusFitness(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.pop = fp11.MlocusPop(1000,5)
        self.all_additive = [fp11w.SlocusAdditive()]*5
        self.all_mult = [fp11w.SlocusMult()]*5
        self.agg_add_w = fp11m.AggAddFitness()
        self.agg_add_t = fp11m.AggAddTrait()
        self.agg_mult_w = fp11m.AggMultFitness()
        self.agg_mult_t = fp11m.AggMultTrait()
        self.additive_w = fp11m.MultiLocusGeneticValue(self.all_additive)
        self.mult_w = fp11m.MultiLocusGeneticValue(self.all_mult)
        self.additive_fitness_value_for_dip = self.additive_w(self.pop.diploids[0],self.pop)
        self.mult_fitness_value_for_dip = self.mult_w(self.pop.diploids[0],self.pop)
    def add_it_up(self,x):
        #naive/incorrect aggregator,
        #but serves to test type(x)
        self.assertEqual(isinstance(x,np.ndarray),True)
        return x.sum()
    def prod_it_up(self,x):
        #naive/incorrect aggregator,
        #but serves to test type(x)
        self.assertEqual(isinstance(x,np.ndarray),True)
        return x.prod()
    def testAllAdditive(self):
        self.assertEqual(len(self.all_additive),5)
        w = self.add_it_up(self.additive_fitness_value_for_dip)
        self.assertEqual(w,5.0)
    def testAllMult(self):
        self.assertEqual(len(self.all_mult),5)
        w = self.prod_it_up(self.mult_fitness_value_for_dip)
        self.assertEqual(w,1.0)
    def testAdditiveFitnessAggregator(self):
        w = self.agg_add_w(self.additive_fitness_value_for_dip);
        self.assertEqual(w,1.0)
    def testMultFitnessAggregator(self):
        w = self.agg_mult_w(self.mult_fitness_value_for_dip);
        self.assertEqual(w,1.0)
    def testSizeMismatchException(self):
        t = [fp11w.SlocusMult()]*4 #no. call backs != no. loci
        tw = fp11m.MultiLocusGeneticValue(t)
        with self.assertRaises(ValueError):
            x = tw(self.pop.diploids[0],self.pop)

class testRecombination(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.rng = fp11.GSLrng(42)
    def testMakeBinomial(self):
        v=[0.5]*5
        x = fp11m.binomial_rec(self.rng,v)
    def testMakePoisson(self):
        v=[1e-3]*5
        x = fp11m.poisson_rec(self.rng,v)
