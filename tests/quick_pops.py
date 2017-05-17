#
# Copyright (C) 2017 Kevin Thornton <krthornt@uci.edu>
#
# This file is part of fwdpy11.
#
# fwdpy11 is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# fwdpy11 is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with fwdpy11.  If not, see <http://www.gnu.org/licenses/>.
#

#This is part of fwdpy11's test suite.
#This file contains functions for quickly
#obtaining simulated populations

def quick_neutral_slocus(N=1000,simlen = 100):
    from fwdpy11.ezparams import mslike
    from fwdpy11.model_params import SlocusParams
    from fwdpy11 import SlocusPop,GSLrng
    from fwdpy11.wright_fisher import evolve
    pop = SlocusPop(N)
    params_dict = mslike(pop,simlen=simlen)
    params = SlocusParams(**params_dict)
    rng=GSLrng(42)
    evolve(rng,pop,params)
    return pop

def quick_nonneutral_slocus(N=1000,simlen = 100):
    from fwdpy11.ezparams import mslike
    from fwdpy11.model_params import SlocusParams
    from fwdpy11 import SlocusPop,GSLrng
    from fwdpy11.wright_fisher import evolve
    from fwdpy11.regions import ExpS
    pop = SlocusPop(N)
    params_dict = mslike(pop,simlen=simlen,dfe=ExpS(0,1,1,-0.1),pneutral=0.95)
    params = SlocusParams(**params_dict)
    rng=GSLrng(42)
    evolve(rng,pop,params)
    return pop


