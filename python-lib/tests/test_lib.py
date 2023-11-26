import numpy
from python_lib import power_array


def test_power_array() -> None:
    array = numpy.random.rand(3)
    power = 3.
    assert numpy.allclose(array**power, power_array(array, power))
