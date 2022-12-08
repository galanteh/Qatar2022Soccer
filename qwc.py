#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Qatar 2022 Soccer is a project that aims to produce all the possible candidates to win.

import argparse
import sys
from colorama import init, Fore, Style
from qatarworldcup import QatarWorldCup
from configuration import WorldCupConfiguration

__author__ = "Hernan Galante"
__copyright__ = "Copyright 2022, Hernan Galante"
__credits__ = ["Hernan Galante"]
__license__ = "GNU Software"
__version__ = "1.0"
__email__ = "hernan_galante@hotmail.com"
__status__ = "Production"


class QWCProgram():
    description_message = "Generate possible matches starting with the Groups of the World Cup."
    exe_name = 'qwc.exe'
    welcome_message = "Qatar 2022 World Cup Fixture predictor. Have fun!"

    def initialize_terminal_colors(self):
        """
        Initialize the terminal colors.
        """
        init(autoreset=True)
        print(Fore.YELLOW + Style.BRIGHT + self.welcome_message + Fore.WHITE + Style.RESET_ALL)

    def print_action(self, message):
        """
        Print into the console an action message.
        :param message:
        """
        print(Fore.GREEN + Style.BRIGHT + message + Fore.WHITE + Style.RESET_ALL)

    def print_error(self, message):
        """
        Print into the console an error message.
        :param message:
        """
        print(Fore.RED + Style.BRIGHT + message + Fore.WHITE + Style.RESET_ALL)
        sys.exit(-1)

    def run_times(self, points, times=1):
        """
        Run all the matches with random results.
        """
        if points > 0:
            wcc = WorldCupConfiguration()
            wcc.logger.info("Points set on command line: {0}".format(points))
            wcc.automatic_points_required_to_win = points
        for _ in range(times):
            wc = QatarWorldCup()
            winner = wc.play()
            wc.save()
            wcc.logger.info(winner)
        sys.exit(1)

    def run(self, argv):
        """
        Run the command line with argument to run a possible fixture
        """

        self.initialize_terminal_colors()
        parser = argparse.ArgumentParser(epilog=self.welcome_message,
                                         prog=self.exe_name,
                                         description=self.description_message)
        parser.add_argument('-r', '--run', nargs=1, default=None, help="Run simulation by a number of times.",
                            dest='times', metavar='TIMES')
        parser.add_argument('-p', '--points', nargs=1, default=None,
                            help="Optional Field: Set the points of the FIFA Ranking between teams. If the difference is bigger than this number the best team wins. Otherwise the system will randomly select one.",
                            dest='points', metavar='POINTS')
        args = vars(parser.parse_args())

        try:
            if args['times'] is None or args['points'] is None:
                parser.print_help()
                sys.exit(1)
            if args['points'][0] is not None:
                points = int(args['points'][0])
            else:
                points = -1
            if args['points'][0] is not None:
                times = int(args['times'][0])
                self.run_times(points, times)
                sys.exit(1)

            self.print_action("Enjoy your data - From Yuntaz with love!")
        except Exception as e:
            self.print_error(str(e))
            parser.print_help()
        except KeyboardInterrupt:
            self.print_error("Batch has been stopped")


if __name__ == "__main__":
    qwcp = QWCProgram()
    qwcp.run(sys.argv[1:])
