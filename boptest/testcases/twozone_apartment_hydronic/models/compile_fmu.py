# -*- coding: utf-8 -*-
"""
This module compiles the defined test case model into an FMU using the
overwrite block parser.

The following libraries must be on the MODELICAPATH:

- Modelica IBPSA
- Modelica Buildings
- Modelica IDEAS
"""



from parsing import parser
from pymodelica import environ

environ['JVM_ARGS'] = '-Xmx8192m'
environ['JVM_ARGS'] = '-Xms8g'

def compile_fmu():
    '''Compile the fmu.
    
    Returns
    -------
    fmupath : str
        Path to compiled fmu.
    
    '''
    
    # DEFINE MODEL
    mopath = 'TwoZoneApartmentHydronic'
    modelpath = 'TwoZoneApartmentHydronic.TestCases.ApartmentModelQHTyp'


    # COMPILE FMU
    fmupath = parser.export_fmu(modelpath, [mopath])

    return fmupath
    
if __name__ == "__main__":
    fmupath = compile_fmu()
