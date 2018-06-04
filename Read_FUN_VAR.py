import sys

class ReadFunVar:
    def __init__(self, file_fun, file_var):
        """
        Initialize class variables
        :param file_fun:
        :param file_var:
        """
        self.best_sp = [0, 0]
        self.best_tc = [0, 0]
        self.best_strike = [0, 0]
        self.median_sp = [0, 0]
        self.median_tc = [0, 0]
        self.median_strike = [0, 0]
        self.file_fun = file_fun
        self.file_var = file_var
        self.read_fun()

    def read_fun(self):
        """
        It completes the initial parameters where [score, line_of_the_score]
        :return:
        """
        strikes_for_median = []
        tc_for_median = []
        sp_for_median = []
        try:
            file = open(self.file_fun, 'r')
            # Changed var line counter for enumerate
            for line_number, line in enumerate(file):
                data = line.split('\t')
                strike = float(data[0])
                tc = float(data[1])
                sp = float(data[2])

                strikes_for_median.append(strike)
                tc_for_median.append(tc)
                sp_for_median.append(sp)

                if self.best_strike[0] < strike:
                    self.best_strike[0] = strike
                    self.best_strike[1] = line_number+1

                if self.best_tc[0] < tc:
                    self.best_tc[0] = tc
                    self.best_tc[1] = line_number+1

                if self.best_sp[0] < sp:
                    self.best_sp[0] = sp
                    self.best_sp[1] = line_number+1
        except FileNotFoundError as err:
            print("OS error: {0}".format(err))
            raise

        except ValueError:
            print("Could not convert data to an integer or data structure mismatch")

        position_of_the_median = int(len(strikes_for_median) / 2)

        sorted_strike = sorted(strikes_for_median)
        sorted_tc = sorted(tc_for_median)
        sorted_sp = sorted(sp_for_median)

        median_strike = sorted_strike[position_of_the_median]
        median_tc = sorted_tc[position_of_the_median]
        median_sp = sorted_sp[position_of_the_median]

        line_median_strike = strikes_for_median.index(median_strike) + 1
        line_median_tc = tc_for_median.index(median_tc) + 1
        line_median_sp = sp_for_median.index(median_sp) + 1

        self.median_sp = [median_sp, line_median_sp]
        self.median_tc = [median_tc, line_median_tc]
        self.median_strike = [median_strike, line_median_strike]

        file.close()

    def save_fun_value(self, filename_out, pair):
        """
        Saves the line of the passed pair to the specified file.
        :param filename_out:
        :param pair:
        :return:
        """
        global line
        with open(self.file_fun, 'r') as file_in:
            line = file_in.readline()
            i = 0
            while i < int(pair[1]):
                line = file_in.readline()
                i += 1
        with open(filename_out, 'w') as file_out:
            file_out.write(line)

    def save_var_value(self, filename_out_pair, pair):
        """
        Writes the sequences in a file
        """
        cnt_of_blocks = 1
        cnt_of_empty_lines = 0

        try:

            file = open(self.file_var, 'r')
            file_out = open(filename_out_pair, 'w')

            for line in file:

                if line[0] == '\n':
                    cnt_of_empty_lines = cnt_of_empty_lines + 1

                if cnt_of_blocks == pair[1] and line[0] != '\n' and cnt_of_empty_lines >= 0:
                    file_out.write(line)

                if cnt_of_empty_lines == 2:
                    cnt_of_blocks = cnt_of_blocks + 1
                    cnt_of_empty_lines = 0

            file.close()
            file_out.close()

        except OSError as err:
            print("OS error: {0}".format(err))

    def save_fun_values(self):
        """
        Saves best fun values
        :return:
        """
        self.save_fun_value('Best_strike_value', self.best_strike)
        self.save_fun_value('Best_tc_value', self.best_tc)
        self.save_fun_value('Best_sp_value', self.best_sp)

        self.save_fun_value('Median_strike_value', self.median_strike)
        self.save_fun_value('Median_tc_value', self.median_tc)
        self.save_fun_value('Median_sp_value', self.median_sp)

    def save_var_values(self):
        """
        Saves best var values
        :return:
        """
        self.save_var_value('Best_strike_seq', self.best_strike)
        print(self.best_strike)
        self.save_var_value('Best_tc_seq', self.best_tc)
        self.save_var_value('Best_sp_seq', self.best_sp)

        self.save_var_value('Median_strike_seq', self.median_strike)
        self.save_var_value('Median_tc_seq', self.median_tc)
        self.save_var_value('Median_sp_seq', self.median_sp)


# Create new ReadFunVar object and get best values
read = ReadFunVar("FUN.BB11001.tsv", "VAR.BB11001.tsv")
# Save values to file
read.save_fun_values()
read.save_var_values()