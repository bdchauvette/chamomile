#!/usr/bin/env python
'''

    Chamomile
    =========
    A small script to help you sleep.
    Based heavily on David Shaw's sleepyti.me bedtime calculator.

'''

from __future__ import print_function
from datetime import date as datedate, datetime, timedelta
import argparse
import textwrap
import sys

__copyright__ = "Copyright (c) 2013, Benjamin Chauvette"
__license__   = "ISC (see LICENSE for details)"
__version__   = "0.1"

def calc_wakeup(bedtime):
    '''
    Returns a time to wakeup based on a bedtime and the
    lengths of the sleep delay and sleep cycle
    '''
    return bedtime + SLEEP_DELAY + SLEEP_CYCLE

def calc_bedtime(wakeup_time):
    '''
    Returns a time to go to bed based on a wakeup time
    and the lengths of the sleep delay and sleep cycle.
    '''
    return wakeup_time - SLEEP_DELAY - SLEEP_CYCLE

def show_wakeups(bedtime, num_cycles=6):
    '''
    Outputs times you should wake up based on a bedtime.
    '''
    wakeup_times = [calc_wakeup(bedtime + (SLEEP_CYCLE * t))
                     for t in range(0, num_cycles)]

    print('If you go to bed at {0}, '
          'you should wake up at one of the following times:'
          .format(datetime.strftime(bedtime, '%H:%M')))
    for t in wakeup_times:
        print('  ',t.strftime('%H:%M'))

def show_bedtimes(wakeup_time, num_cycles=6):
    '''
    Outputs times you should go to sleep based on when you want to wake up.
    '''
    bedtimes = reversed([calc_bedtime(wakeup_time - (SLEEP_CYCLE * t))
                for t in range(0, num_cycles)])

    print('To wake up at {0}, '
          'you should head to bed at one of the following times:'
          .format(datetime.strftime(wakeup_time, '%H:%M')))
    for bedtime in bedtimes:
        print('  ',bedtime.strftime('%H:%M'))

def get_args():
    '''
    Parse command line arguments
    '''
    parser = argparse.ArgumentParser(
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description=textwrap.dedent('''\
            Chamomile
            =========
            A small script to help you sleep.
            Based heavily on David Shaw's sleepyti.me bedtime calculator.
            '''))

    parser.add_argument(
        '-v', '--version',
        action='version',
        version='Chamomile {0}'.format(__version__))

    parser.add_argument(
        '-c', '--cycle',
        nargs=1,
        metavar='MINS',
        type=int,
        help='specifies length of sleep cycle in minutes'
        )

    parser.add_argument(
        '-d', '--delay',
        nargs=1,
        type=int,
        metavar='MINS',
        help='specifies how long it takes to fall asleep'
        )

    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        '-w', '--wakeup',
        nargs=1,
        metavar='TIME',
        type=str,
        help='specifies the time to wake up (HH:MM); Chamomile will tell you when to go to bed.',
        )

    group.add_argument(
        'bedtime',
        nargs='?',
        metavar='BEDTIME',
        type=str,
        help='specifies a bedtime (HH:MM); Chamomile will tell you when to wake up'
        )

    return parser.parse_args()


def main():
    # Get any command line arguments
    args = vars(get_args())

    # Globals are bad, and I should feel bad
    global NOW, SLEEP_CYCLE, SLEEP_DELAY
    NOW = datetime.now()
    SLEEP_CYCLE = timedelta(
        minutes=int(args['cycle'][0]) if args['cycle'] else 90)
    SLEEP_DELAY = timedelta(
        minutes=int(args['delay'][0]) if args['delay'] else 14)

    # Figure out if we're trying to find a bedtime or wakeup time
    if args['bedtime']:
        try:
            wakeup_time = datetime.strptime(args['bedtime'], '%H:%M')
            show_bedtimes(wakeup_time)
        except ValueError:
            print('Error: Unknown time format ({0})'.format(args['bedtime']))
            return 1
        except Exception, msg:
            print('Error: {0}'.format(msg))
            return 1
    elif args['wakeup']:
        try:
            bedtime = datetime.strptime(args['wakeup'][0], '%H:%M')
            show_wakeups(bedtime)
        except ValueError:
            print('Error: Unknown time format ({0})'.format(args['bedtime']))
            return 1
        except Exception, msg:
            print('Error: {0}'.format(msg))
            return 1
    else:
        try:
            show_wakeups(NOW)
        except Exception, msg:
            print('Error: {0}'.format(msg))
            return 1


if __name__ == '__main__':
    sys.exit(main())

# vim: ft=python ts=4 sts=4 sw=4:
