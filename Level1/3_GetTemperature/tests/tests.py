from src import temperature_3 as t3
import nose.tools as ns


def set_array():
    test_array = [12, 14, 17, 22]
    return test_array

#@ns.with_setup(setup=set_array)
def test_nearest_idx_true():
    idx = t3.nearest_idx(14, set_array())
    ns.assert_equals(1, idx)


#@ns.with_setup(setup=set_array)
def test_nearest_idx_false():
    idx = t3.nearest_idx(14, set_array())
    ns.assert_not_equals(3, idx)