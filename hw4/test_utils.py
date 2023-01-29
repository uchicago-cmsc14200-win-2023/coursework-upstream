import math

import pandas as pd


def compare_dataframes(actual, expected):
    '''
    Compare two dataframes.  Inputs can contain a mix of types,
    including floats.
    Inputs:
        actual: pandas dataframe
        expected: pandas dataframe
    Returns: boolean, string with an error message
    '''

    if actual is None:
        if expected is not None:
            return (False, "Actual is None, when expected is not None\n")
        else:
            return (True, None)

    if expected is None:
        return (False, "Actual is not None, when expected is None\n")

    if not isinstance(actual, pd.DataFrame):
        return (False, f"Actual is not a dataframe (got {type(actual)} instead)")

    assert isinstance(expected, pd.DataFrame), f"Test data contains non-dataframe ({type(expected)})"

    if actual.equals(expected):
        return (True, None)

    actual_row_names = actual.index.tolist()
    actual_col_names = actual.columns.tolist()

    expected_row_names = expected.index.tolist()
    expected_col_names = expected.columns.tolist()

    if sorted(actual_row_names) != sorted(expected_row_names):
        msg = "Row names differ.    Expected: {}\n    Actual: {}"
        return False, msg.format(expected_row_names, actual_row_names)

    if sorted(actual_col_names) != sorted(expected_col_names):
        msg = "Column names differ.    Expected: {}\n    Actual: {}"
        return False, msg.format(expected_col_names, actual_col_names)

    for col_name in actual_col_names:
        for row_name in actual_row_names:
            a = actual[col_name][row_name]
            e = expected[col_name][row_name]

            msg = "Actual and expected differ at {}, {}.\n    Expected: {}\n    Actual: {}"

            if isinstance(e, float):
                if (abs(a - e) > 0.001) or \
                   (math.isnan(a) and not math.isnan(e)) or \
                   (not math.isnan(a) and math.isnan(e)):
                    return False, msg.format(col_name, row_name, e, a)
            elif a != e:
                return False, msg.format(col_name, row_name, e, a)

    return True, None