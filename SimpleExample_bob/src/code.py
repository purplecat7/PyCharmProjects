import numpy as np
import netCDF4 as nc

def get_slicer():
    return {
                'time_counter': None,
                'deptht': None,
                'y': None,
                'x': None,
                'axis_nbounds': None
            }

def get_data(fpath, var_list, slicer=None):
    ds = nc.Dataset(fpath)
    n_ds = {}
    # Loop over every variable we want
    for v in var_list:
        if slicer is not None:
            dyna_slice = []
            # Loop over dimensions for current var
            for d in ds[v].dimensions:
                # If it's a dimension we want to slice, we go to slice it
                if d in slicer:
                    # If we want to slice it, we make the tuple
                    if slicer[d] is not None:
                        dyna_slice.append(slice(slicer[d][0], slicer[d][1]))
                    # Otherwise we take the whole dimension
                    else:
                        dyna_slice.append(slice(None))
            # Slice out the array
            n_ds[v] = np.array(ds[v][tuple(dyna_slice)])
        # Else, we are copying the whole variable
        else:
            n_ds[v] = np.array(ds[v])
    return n_ds