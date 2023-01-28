"""
CMSC 14200, Winter 2023
Homework #4

People Consulted:
   List anyone (other than the course staff) that you consulted about
   this assignment.

Online resources consulted:
   List the URLs of any online resources other than the course text and
   the official Python language documentation that you used to complete
   this assignment.
"""

import numpy as np
import pandas as pd
import utils


def read_and_process_asc(filename):
    """
    Read in and process a ASC file from the ASQP data set

    Input:
        filename (string): name of the file

    Returns (Pandas DataFrame): a Pandas DataFrame with the ASQP data
    """
    raise NotImplementedError("todo: read_and_process_asc")


def delay_and_cancel_fractions(df):
    """
    Given ASQP data, compute the fraction of delayed and cancelled flights

    Input:
        df (DataFrame): an ASQP DataFrame

    Returns (tuple of floats): fraction of flights that were delayed,
        fraction of flights that were cancelled
    """
    raise NotImplementedError("todo: delay_and_cancel_fractions")


def per_carrier_delays_cancels(df):
    """
    Given ASQP data, determine how many of each carrier's flights were
        delayed or cancelled

    Input:
        df (DataFrame): an ASQP DataFrame

    Returns (tuple of DataFrame): delays by carrier, cancellations per carrier
    """
    raise NotImplementedError("todo: per_carrier_delays_cancels")


def average_delay(df):
    """
    Given ASQP data, determine the average flight delay

    Input:
        df (DataFrame): an ASQP DataFrame

    Returns (float): the average delay
    """
    raise NotImplementedError("todo: average_delay")


def average_delay_by_period(df):
    """
    Given ASQP data, determine whether or not delays get worse throughout
        the day

    Input:
        df (DataFrame): an ASQP DataFrame

    Returns (DataFrame): the average delay per period of day
    """
    raise NotImplementedError("todo: average_delay_by_period")


def underperforming_carriers(df):
    """
    Given ASQP data, determine which carriers have a worse than average delay

    Input:
        df (DataFrame): an ASQP DataFrame

    Returns (DafaFrame): underperforming carriers and their average delay
    """
    raise NotImplementedError("todo: underperforming_carriers")


def read_and_process_npy(filename):
    """
    Read in and process time series ASQP data

    Input:
        filename (string): name of the NPY file

    Returns (NumPy array): a time series NumPy array
    """
    raise NotImplementedError("todo: read_and_process_npy")


def remove_irregularities(ts, width):
    """
    Apply a smoothing technique to remove irregularities from the
        times series ASQP data

    Input:
        ts (NumPy array): the time series
        width (int): the width over which to smoothe

    Returns (NumPy array): smoothed time series data
    """
    raise NotImplementedError("todo: remove_irregularities")


def remove_trend(ts, width):
    """
    Remove overall trend from time series ASQP data

    Input:
        ts (NumPy array): the time series
        width (int): the width over which to smoothe

    Returns (NumPy array): detrended time series data
    """
    raise NotImplementedError("todo: remove_trend")


def is_seasonal(ts, width):
    """
    Bucket late flights, determine the bucket with the most
        late flights

    Input:
        ts (NumPy array): the time series
        width (int): the width over which to smoothe
        list_of_indices (lit of list of ints): something here

    Returns (NumPy array, int): number of delays in each month,
        the index of the month with the most delays (January = 0, etc.)
    """
    raise NotImplementedError("todo: is_seasonal")
