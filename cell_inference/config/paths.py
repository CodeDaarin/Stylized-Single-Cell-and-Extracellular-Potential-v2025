import os
import platform

ROOT_DIR = os.path.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.path.sep)[:-1])
RESOURCES_ROOT = os.path.join(ROOT_DIR, 'resources/')

LIBRARY = 'nrnmech.dll' if platform.system() == 'Windows' else 'x86_64/.libs/libnrnmech.so'
COMPILED_REDUCED_ORDER = os.path.join(RESOURCES_ROOT, 'compiled', 'mechanisms_reduced_order')
COMPILED_LIBRARY_REDUCED_ORDER = os.path.join(COMPILED_REDUCED_ORDER, LIBRARY)

GEO_REDUCED_ORDER = os.path.join(RESOURCES_ROOT, 'geom_parameters_reduced_order_L5.csv')

ELECTRODES = os.path.join(RESOURCES_ROOT, 'Electrodes.csv')
