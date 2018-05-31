class ReadFunVar:
    def __init__(self, file_fun, file_var):
        self.best_sp = [0, 0]
        self.best_tc = [0, 0]
        self.best_strike = [0, 0]
        self.file_fun = file_fun
        self.file_var = file_var

    def read_fun(self):
        # Returns a list of list with the best Strike,tc,sp and the position of the line where they are. That line is the number of the block int the next function read_VAR
        strikes_for_median = []
        tc_for_median = []
        sp_for_median = []
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
                self.best_strike[1] = line_number

            if self.best_tc[0] < tc:
                self.best_tc[0] = tc
                self.best_tc[1] = line_number

            if self.best_sp[0] < sp:
                self.best_sp[0] = sp
                self.best_sp[1] = line_number

        position_of_the_median = int(len(strikes_for_median) / 2)

        sorted_strike = sorted(strikes_for_median)
        sorted_tc = sorted(tc_for_median)
        sorted_sp = sorted(sp_for_median)

        median_strike = sorted_strike[position_of_the_median]
        median_tc = sorted_tc[position_of_the_median]
        median_sp = sorted_sp[position_of_the_median]

        line_median_strike = strikes_for_median.index(median_strike) + 1
        line_median_TC = tc_for_median.index(median_tc) + 1
        line_median_SP = sp_for_median.index(median_sp) + 1
        file.close()

    def save_fun_value(self, pair, filename_out):
        global line
        with open(self.file_fun, 'r') as file_in:
            i = 0
            while i < pair[1]:
                line = file_in.readline()
                i += 1
        with open(filename_out, 'w') as file_out:
            file_out.write(line)

    def save_var_value(self, pair, filename_out):
        fout = open(filename_out, 'w')
        with open(self.file_var, 'r') as file_in:
            i = 0
            while i < pair[1]:
                if file_in.readline() == '':
                    file_in.readline()
                    i += 1
            line = file_in.readline()
            while line != '':
                fout.write(line)
                line = file_in.readline()
        fout.close()

    def save_fun_values(self):
        self.save_fun_value('Best_strike_value', self.best_strike)
        self.save_fun_value('Best_tc_value', self.best_tc)
        self.save_fun_value('Best_sp_value', self.best_sp)

    def save_var_values(self):
        self.save_var_value('Best_strike_seq', self.best_strike)
        self.save_var_value('Best_tc_seq', self.best_tc)
        self.save_var_value('Best_sp_seq', self.best_sp)


read = ReadFunVar("FUN.BB11001.tsv", "VAR.BB11001.tsv")
read.read_fun()
read.save_fun_values()
read.save_var_values()
