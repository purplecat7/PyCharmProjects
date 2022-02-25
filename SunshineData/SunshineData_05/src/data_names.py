from enum import Enum

class ColNames(str, Enum):   #  make sure this Enum works with strings
    UTC = "UTC"
    hrmins = "hhmm"
    hrs = "h"

# and then use the Py3.x formatted string construct
# f"{ColNames.UTC}"   will give 'UTC'
# or you have to use    ColNames.UTC.value   to get the string