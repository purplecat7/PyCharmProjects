"""Defines the Storm_data class.
When instantiated with a file name or open file,
reads in and stores the data.

@author: Simon Peatman
"""

# modules
import numpy as np


class StormData:
    """Class for holding storm data from file.

    Arguments when instantiating:
    <storm_file>    File, filename, or generator to read.
                    If the filename extension is `.gz` or `.bz2`, the
                    file is first decompressed. Note that generators
                    must return byte strings in Python 3k.
    <kwargs>        See numpy.genfromtxt documentation for
                    description of keyword arguments.
    """


    def __init__(self, storm_file, **kwargs):
        """Instantiates a Storm_data object, obtaining data from an open file.

        Arguments:
        <storm_file>    File, filename, or generator to read.
                        If the filename extension is `.gz` or `.bz2`, the
                        file is first decompressed. Note that generators
                        must return byte strings in Python 3k.
        <kwargs>        See numpy.genfromtxt documentation for
                        description of keyword arguments.
        """

        # default values if not present in kwargs
        missing_value = kwargs.pop('missing_values', -999)
        comments = kwargs.pop('comments', '#;~:@')
        names = kwargs.pop('names', ['serial_number',
                                     'year',
                                     'number',
                                     'basin_code',
                                     'station',
                                     'name',
                                     'datetime',
                                     'type_code',
                                     'latitude',
                                     'longitude',
                                     'windspeed',
                                     'pressure'])

        # get data as record
        d = np.recfromcsv(storm_file, filling_values=missing_value,
                          comments=comments, names=names, **kwargs)

        # retain data not containing missing_value
        new_d = []
        for rec in d:
            if missing_value not in rec:
                new_d.append(rec)

        # assign data to arrays
        (self.serial_number,
         self.year,
         self.number,
         self.basin_code,
         self.station,
         self.name,
         self.datetime,
         self.type_code,
         self.lat,
         self.lon,
         self.windspeed,
         self.pressure) = zip(*new_d)


    def windspeed_from_serial_number(self, serial_no):
        """Returns a list of all windspeeds
        recorded for the given serial number.

        Arguments:
        <serial_no>    string

        Returns:
        tuple of windspeeds
        """

        # generate windspeed dictionary if not already existent
        if not hasattr(self, 'dict_sn_ws'):
            self._gen_dict_sn_ws()

        # get list of windspeeds for given serial_no
        try:
            return self.dict_sn_ws[serial_no]
        except KeyError:
            raise KeyError(('serial_no \'%s\' not present in data; choose from: ' % serial_no)+str(self.dict_sn_ws.keys()))


    def serial_number_by_mean_pressure(self, save_path=None):
        """Generates list of serial numbers and the mean
        associated pressure, ordered by pressure.

        Records with negative or non-numeric pressure values
        are ignored in the calculation of the mean.

        Arguments:
        <save_path>    string/None    path to create output file
                                      if None (default), returns results
        """

        # put each pressure in dictionary
        self.dict_sn_p = {}
        for (sn,p) in zip(self.serial_number,self.pressure):
            # ignore if pressure is recorded as 0, -1 or
            # something which can't be cast as as float
            try:
                p = float(p)
            except:
                continue
            if p > 0:
                if sn in self.dict_sn_p.keys():
                    self.dict_sn_p[sn].append(p)
                else:
                    self.dict_sn_p[sn] = [p]

        # for each serial number, get mean pressure
        self.dict_sn_meanp = {}
        for (sn,plist) in self.dict_sn_p.items():
            self.dict_sn_meanp[sn] = np.mean(plist)

        # get pressures and serial numbers in order of mean pressure
        ordered_sn = []
        ordered_meanp = []
        while len(self.dict_sn_meanp):

            # get serial number for smallest value of mean pressure
            (k,v) = zip(*self.dict_sn_meanp.items())
            meanp = np.array(v).min()
            sn = k[v.index(meanp)]

            # append to lists and remove from dictionary
            ordered_sn.append(sn)
            ordered_meanp.append(meanp)
            rem = self.dict_sn_meanp.pop(sn)

        # save or return
        if save_path is not None:
            fout = open(save_path, 'w')
            fout.write('serial number\tmean pressure\n')
            for (sn,mp) in zip(ordered_sn, ordered_meanp):
                fout.write(str(sn)+'\t'+str(mp)+'\n')
            fout.close()
            print 'Saved %s' % save_path
        else:
            return zip(ordered_sn, ordered_meanp)


    def _gen_dict_sn_ws(self):
        """Generates dictionary containing list
        of windspeeds for each serial number.
        Internal function, not to be called by user.
        """

        # create dictionary
        self.dict_sn_ws = {}

        # put each windspeed in dictionary
        for (sn,ws) in zip(self.serial_number,self.windspeed):
            if sn in self.dict_sn_ws.keys():
                self.dict_sn_ws[sn].append(ws)
            else:
                self.dict_sn_ws[sn] = [ws]


    def __repr__(self):
        """String representation of Storm_data object.
        Displays data in neat table.
        """

        # iterate for each record in Storm_data object
        data = (self.serial_number,
                self.year,
                self.number,
                self.basin_code,
                self.station,
                self.name,
                self.datetime,
                self.type_code,
                self.lat,
                self.lon,
                self.windspeed,
                self.pressure)
        repr_str = ''
        for rec in zip(*data):
            repr_str_rec = repr(rec[0])
            for field in rec[1:]:
                repr_str_rec += '\t'
                repr_str_rec += repr(field)
            repr_str += repr_str_rec
            repr_str += '\n'
        return repr_str
