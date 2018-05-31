class ReadFunVar:
    def __init__(self):
        pass

    def read_fun(self, fileName):
        # Returns a list of list with the best Strike,tc,sp and the position of the line where they are. That line is the number of the block int the next function read_VAR
        strikes_for_median = []
        tc_for_median = []
        sp_for_median = []
        best_strike = [0, 0]
        best_tc = [0, 0]
        best_sp = [0, 0]
        file = open(fileName, 'r')
        # Changed var line counter for enumerate
        for line_number, line in enumerate(file):

            data = line.split('\t')
            strike = float(data[0])
            tc = float(data[1])
            sp = float(data[2])

            strikes_for_median.append(strike)
            tc_for_median.append(tc)
            sp_for_median.append(sp)

            if best_strike[0] < strike:
                best_strike[0] = strike
                best_strike[1] = line_number

            if best_tc[0] < tc:
                best_tc[0] = tc
                best_tc[1] = line_number

            if best_sp[0] < sp:
                best_sp[0] = sp
                best_sp[1] = line_number

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

        # result_dictionary = {best_strike[0]:best_strike[1],best_tc[0]:best_tc[1],best_sp[0]:best_sp[1]}

        return [best_strike, best_tc, best_sp]
        # print(result_dictionary)

    # lista_de_bloques = [best_STRIKE[1],best_TC[1],best_SP[1]]
    # print(lista_de_bloques)

    def read_var(self, file_name, list_of_lists):
        cnt_of_blocks = 1
        cnt_of_empty_lines = 0

        file = open(file_name, 'r')
        file_strike = open("Best_strike_seq.txt", 'w')
        file_strike.write("Best STRIKE :" + str(list_of_list[0][0]) + '\n')

        file_tc = open("Best_TC_seq.txt", 'w')
        file_tc.write("Best TC :" + str(list_of_list[1][0]) + '\n')

        file_sp = open("Best_SP_seq.txt", 'w')
        file_sp.write("Best SP :" + str(list_of_list[2][0]) + '\n')

        for line in file:

            if line[0] == '\n':
                cnt_of_empty_lines = cnt_of_empty_lines + 1

            if cnt_of_blocks == list_of_list[0][1] and line[0] != '\n' and cnt_of_empty_lines >= 0:
                file_strike.write(line + '\n')

            if cnt_of_blocks == list_of_list[1][1] and line[0] != '\n' and cnt_of_empty_lines >= 0:
                file_tc.write(line + '\n')

            if cnt_of_blocks == list_of_list[2][1] and line[0] != '\n' and cnt_of_empty_lines >= 0:
                file_sp.write(line + '\n')

            if cnt_of_empty_lines == 2:
                cnt_of_blocks = cnt_of_blocks + 1
                cnt_of_empty_lines = 0

        file.close()
        file_strike.close()
        file_sp.close()
        file_tc.close()



read = ReadFunVar()

list_of_list = read.read_fun("FUN.BB11001.tsv")

# read.read_VAR("VAR.BB11001.tsv",list_of_list)
