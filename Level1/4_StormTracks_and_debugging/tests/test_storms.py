import nose.tools as ns
import numpy as np
import filecmp
import os
import glob
from src3 import stormTracks as st3
from src5 import stormTracks as st5
from src5 import stormStruct as ss5

def clean_up():
    # remove output files
    try:
        for fl in glob.glob('.\\test_data_out_good.dat'):
            os.remove(fl)
        for fl in glob.glob('.\\results_a_variable.txt'):
            os.remove(fl)
    except Exception as ex:
        raise ex


@ns.with_setup(teardown=clean_up)
def test_data_load_3():
    data = st3.load_data("test_data_good.dat")
    np.savetxt("test_data_out_good.dat", data, fmt='%d', delimiter=",")
    ns.assert_true(filecmp.cmp("test_data_out_good.dat",
                               "test_data_out_good_ref.dat",
                               shallow=False))


@ns.with_setup(teardown=clean_up)
def test_write_result_3():
    the_avg_dict = {}
    the_avg_dict['1'] = 40
    the_avg_dict['2'] = 35
    st3.write_result(the_avg_dict, 'a_variable')
    # compare file contents with pre-existing file
    ns.assert_true(filecmp.cmp("results_a_variable.txt",
                               "results_a_variable_ref.txt",
                               shallow=False))


def test_averaging_3():
    the_dict = {}
    the_dict['1'] = [40, 20, 30]
    the_dict['2'] = [1, 2, 3]
    the_avg_dict = {}
    the_avg_dict['1'] = 30
    the_avg_dict['2'] = 2
    result = st3.get_average_for_storm(the_dict)
    ns.assert_dict_equal(the_avg_dict, result)


def test_averaging_5():
    s1 = ss5.Storm()
    s1.stormid = 1
    s1.windspeed = [31, 32, 33, 34]
    s1.pressure = [21, 22, 23, 24]
    wind_avg_dict = {1: 32.5}
    pres_avg_dict = {1: 22.5}
    result_wind_avg, result_pres_avg = st5.get_averages_for_storm([s1])
    ns.assert_dict_equal(wind_avg_dict, result_wind_avg)
    ns.assert_dict_equal(pres_avg_dict, result_pres_avg)


def test_extract_field_3():
    # NOTE: this test fails, which I wasn't expecting... I know what the error
    # in the code is... proof that testing works... did anyone else spot that
    # extract_field() has a big bug?
    # Clue: it's a boundary case - i.e. one that happens at the start/end

    # use st3.load_data() on test data
    data = st3.load_data("test_data_good.dat")
    # construct expected dictionary from test data - by hand!!!
    the_dict = {'1': [35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 40, 40, 40],
                '2': [],
                '3': [35, 40, 45, 50, 55, 60, 60, 60, 60, 60, 60, 60, 60]}
    # call st3.extract_data() giving it loaded test data and name of variable wanted -
    # the same one as you used to make the expected result!!!
    wind_data = st3.extract_field(data, 'wind')
    # compare returned dictionary with hand crafted one
    ns.assert_dict_equal(the_dict, wind_data)


def test_extract_field_5():
    # prepare storm structures by reading the file directly
    s1 = ss5.Storm()
    s1.stormid = 1
    s1.windspeed = [35, 35, 35, 35, 35, 35, 35, 35, 35, 35, 40, 40, 40]
    s1.pressure = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    s2 = ss5.Storm()
    s2.stormid = 2
    s2.windspeed = []
    s2.pressure = []
    s3 = ss5.Storm()
    s3.stormid = 3
    s3.windspeed = [35, 40, 45, 50, 55, 60, 60, 60, 60, 60, 60, 60, 60]
    s3.pressure = [1000, 990, 980, 980, 980, 975, 975, 970, 970, 965, 965, 960, 960]
    data = st5.load_data("test_data_good.dat")
    storm_list = st5.extract_fields(data)
    # We shall take a random sample of the contents of the returned storms
    # Note that this is not very satisfactory and we should really do
    # things properly and define a way of comparing two structures.
    ns.assert_equal(s1.stormid, storm_list[0].stormid)
    ns.assert_list_equal(s2.windspeed, storm_list[1].windspeed)
    ns.assert_list_equal(s3.pressure, storm_list[2].pressure)


@ns.raises(TypeError)
def test_averaging_fail_3():
    # test to specifically check that we raise the correct exception
    the_dict = {}
    the_dict['1'] = ['z', 20, 30]
    the_dict['2'] = [1, 'bob', 3]
    the_avg_dict = {}
    the_avg_dict['1'] = 30
    the_avg_dict['2'] = 2
    # exception thrown here so no other code after it would be executed
    result = st3.get_average_for_storm(the_dict)


@ns.raises(TypeError)
def test_bad_data_3():
    # same as above but making sure it works for a file
    data = st3.load_data("test_data_bad.dat")
    wind_data = st3.extract_field(data, 'wind')
    result = st3.get_average_for_storm(wind_data)