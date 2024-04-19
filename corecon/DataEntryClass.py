import numpy as np
import os
import copy

from .InternalFunctions import _insert_blank_spaces, _get_str_from_array1d, _get_str_from_multiarray, _get_str_from_array#, _compare_arrays

###################
# DataEntry CLASS #
###################


class DataEntry:
    """Class representing a single constraint.
    """

    def __init__(self, 
                 dictionary_tag,
                 description   = None,  
                 reference     = None,
                 url           = None, 
                 extracted     = None,  
                 values        = None,
                 variable_list = None):
        """construct method
        """    
        self.dictionary_tag         = dictionary_tag
        self.description            = description           
        self.reference              = reference          
        self.url                    = url                   
        self.extracted              = extracted           
        #self.values                 = values
        self.variable_list          = variable_list
        
        if values is not None:
            for k,v in values.items():
                setattr(self, k, v)

    def __repr__(self):
        """string describing the class
        """
        return "corecon DataEntry class"

    def __str__(self):
        """output of print
        """

        ostr=""               
        ostr +=                       "description            = %s\n"%_insert_blank_spaces(self.description, 25)
        ostr +=                       "reference              = %s\n"%self.reference           
        ostr +=                       "url                    = %s\n"%self.url                   
        ostr +=                       "extracted              = %s\n"%self.extracted          
        for ed in self.variable_list:
            ostr += _get_str_from_array1d(ed+" "*max(0,23-len(ed))+"= ", getattr(self, ed) )
        return ostr

    def __eq__(self,other):
        """custom equality definition
        """

        #need to check extra_fields here
        if len(self.extra_data) != len(other.extra_data):
            return False
        else:
            for s,o in zip(self.extra_data, other.extra_data):
                if (s != o) or ( np.any(getattr(self,s) != getattr(other,o)) ):
                    return False
            #all ok for extra_data, now check the rest
            return(
                               (self.ndim                   == other.ndim                                     ) & \
                               (self.description            == other.description                              ) & \
                               (self.reference              == other.reference                                ) & \
                               (self.parent_field           == other.parent_field                             ) & \
                               (self.url                    == other.url                                      ) & \
                               (self.extracted              == other.extracted                                ) & \
                    np.all     (self.dimensions_descriptors == other.dimensions_descriptors                   ) & \
                    np.all     (self.axes                   == other.axes                                     ) & \
                    np.allclose(self.values                 ,  other.values                 , equal_nan=True  ) & \
                    np.allclose(self.err_up                 ,  other.err_up                 , equal_nan=True  ) & \
                    np.allclose(self.err_down               ,  other.err_down               , equal_nan=True  ) & \
                    np.all     (self.upper_lim              == other.upper_lim                                ) & \
                    np.all     (self.lower_lim              == other.lower_lim                                ) )

    def swap_limits(self):
        """Swap upper and lower limits. Useful when computing a derived quantity.
        """
        ul_copy = copy.deepcopy(self.upper_lim)
        self.upper_lim = copy.deepcopy(self.lower_lim)
        self.lower_lim = copy.deepcopy(ul_copy)

    def swap_errors(self):
        """Swap upper and lower errors. Useful when computing a derived quantity.
        """
        eu_copy = copy.deepcopy(self.err_up)
        self.err_up   = copy.deepcopy(self.err_down)
        self.err_down = copy.deepcopy(eu_copy)

    #def none_to_value(self, value):
    #    for f in [self.values, self.err_up, self.err_down]:
    #        w = (f == None)
    #        f[w] = value

    #def none_to_nan(self):
    #    self.none_to_value(np.nan)
    
    def nan_to_values(self, array, new_vals):
        """Replaces all NaN with values.

        :param array: (list of) variable name(s) to work on. Use 'all' to replace NaNs in all array variables.
        :type array: (list of) str
        :param new_vals: value(s) to replace the NaNs with. If a np.array, it should have the correct dimension, i.e. the same as the number of NaNs.
        :type new_vals: float or np.array
        """
        #if array=='values' or array=='all':
        #    w = np.isnan(self.values)
        #    self.values[w] = new_vals
        #if array=='err_up' or array=='all':
        #    w = np.isnan(self.err_up)
        #    self.err_up[w] = new_vals
        #if array=='err_down' or array=='all':
        #    w = np.isnan(self.err_down)
        #    self.err_down[w] = new_vals
        if isinstance(array, str):
            if array=='all':
                names = []
                names.append('values')
                names.append('err_up')
                names.append('err_down')
                for k in self.extra_data:
                    if isinstance(getattr(self,k), np.ndarray):
                        names.append(k)
            else:
                names = [array]
        elif (isinstance(array, list) or isinstance(array, tuple)):
            names = array
        else:
            print("ERROR: the argument 'array' should be a string or a list/tuple of strings!")
            return

        for name in names:
            v = getattr(self, name)
            v[np.isnan(v)] = new_vals
            setattr(self, name, v)

    def set_lim_errors(self, newval, frac_of_values=False):
        """Set the value of error arrays for upper and lower limits.

        :param newval: value to assign to the error arrays.
        :type newval: float
        :param frac_of_values: if True, newval \*= values.
        :type frac_of_values: bool, optional
        """
        w = (self.upper_lim|self.lower_lim)
        if frac_of_values:
            newval *= self.values[w]
        self.err_up   [w] = newval
        self.err_down [w] = newval

    def list_attributes(self):
        """List the attributes for the current entry.
        """
        return list(self.__dict__.keys())
