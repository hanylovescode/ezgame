import argparse
import logging

from main import EzGame


def profile_game(profile_id):
    import cProfile

    profile_name = f'p_{profile_id}'

    logger = logging.getLogger('Profile')
    logger.info('Profiling started ...')
    cProfile.run('EzGame()', f'{profile_name}_output.prof')
    logger.info('Profiling finished.')

    import pstats

    logger.info('Sorting profile')
    with open(f'{profile_name}_time.txt', 'w') as f:
        p = pstats.Stats(f'{profile_name}_output.prof', stream=f)
        p.sort_stats('time').print_stats()

    with open(f'{profile_name}_calls.txt', 'w') as f:
        p = pstats.Stats(f'{profile_name}_output.prof', stream=f)
        p.sort_stats('calls').print_stats()

    logger.info(
        f'Output files are:\n\
        \t{profile_name}_output.prof\n\
        \t{profile_name}_time.txt\n\
        \t{profile_name}_calls.txt'
    )


def parse_cl_args():
    parser = argparse.ArgumentParser(
        description='Building Space Invaders clone with pygame \
            use args to change loglevel and toggle cProfile output files'
    )
    parser.add_argument(
        '-p', '--profile',
        type=str,
        help='cProfile the project and sort the output by time and calls'
    )
    parser.add_argument(
        '-l', '--log',
        dest='loglevel',
        default='warning',
        choices=['debug', 'info', 'warning', 'error', 'critical'],
        help='changing the logging level, default=warning'
    )
    return parser.parse_args()
