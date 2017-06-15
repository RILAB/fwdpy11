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
    recorder(const std::uint32_t simlen) : data(std::vector<recorder_data>())
    {
        data.reserve(simlen);
    }

    void operator()(const fwdpy11::singlepop_t * pop) const
    {
    }
};
