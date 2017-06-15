#include <pybind11/pybind11.h>
#include <pybind11/numpy.h>
#include <pybind11/stl.h>
#include <pybind11/stl_bind.h>

#include <fwdpy11/types.hpp>
#include <cstdint>

struct recorder_data
{
    std::size_t generation;
    double wbar, s1, s2;
};

struct recorder
{
    std::vector<recorder_data> data;
    recorder_data d;
    recorder(const std::uint32_t simlen) : data(std::vector<recorder_data>())
    {
        data.reserve(simlen);
    }

    void
    operator()(const fwdpy11::singlepop_t& pop)
    {
        double w = 0., s1 = 0., s2 = 0.;
        for (auto&& dip : pop.diploids)
            {
                w += dip.w;
                for (auto&& key : pop.gametes[dip.first].smutations)
                    {
                        s1 += pop.mutations[key].s;
                    }
                for (auto&& key : pop.gametes[dip.second].smutations)
                    {
                        s2 += pop.mutations[key].s;
                    }
            }
        d.generation = pop.generation;
        d.wbar = w;
        d.s1 = s1 / static_cast<double>(pop.N);
        d.s2 = s2 / static_cast<double>(pop.N);
        data.push_back(d);
    }
};
