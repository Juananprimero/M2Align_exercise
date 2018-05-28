
class Read_FUN_VAR:
    def __init__(self):
        pass

    def read_FUN(self,fileName):
        #Returns a list of list with the best Strike,TC,SP and the position of the line where are they. That line is the number of the block int the next function read_VAR

        cnt_of_line =0
        best_STRIKE=[0,0]
        best_TC=[0,0]
        best_SP=[0,0]
        file = open(fileName,'r')
        for line in file:
            cnt_of_line = cnt_of_line+1

            data=line.split('\t')
            STRIKE=float(data[0])
            TC =float(data[1])
            SP =float(data[2])

            if(best_STRIKE[0]<STRIKE):
                best_STRIKE[0] = STRIKE
                best_STRIKE[1]= cnt_of_line

            if(best_TC[0]<TC):
                best_TC[0]=TC
                best_TC[1]=cnt_of_line

            if(best_SP[0]<SP):
                best_SP[0]=SP
                best_SP[1]=cnt_of_line

        file.close()

       # result_dictionary = {best_STRIKE[0]:best_STRIKE[1],best_TC[0]:best_TC[1],best_SP[0]:best_SP[1]}


        return [best_STRIKE,best_TC,best_SP]
        #print(result_dictionary)
       # lista_de_bloques = [best_STRIKE[1],best_TC[1],best_SP[1]]
        #print(lista_de_bloques)


    def read_VAR(self, fileName, list_of_lists):
        cnt_of_blocks = 1
        cnt_of_empty_lines=0


        file = open(fileName, 'r')
        file_STRIKE = open("Best_strike_seq.txt",'w')
        file_STRIKE.write("Best STRIKE :" + str(list_of_list[0][0]) + '\n')

        file_TC = open("Best_TC_seq.txt", 'w')
        file_TC.write("Best TC :" + str(list_of_list[1][0]) + '\n')

        file_SP = open("Best_SP_seq.txt", 'w')
        file_SP.write("Best SP :" + str(list_of_list[2][0]) + '\n')


        for line in file:


            if (line[0]=='\n'):

                cnt_of_empty_lines= cnt_of_empty_lines+1

            if (cnt_of_blocks == list_of_list[0][1] and line[0] != '\n' and  cnt_of_empty_lines>=0):

                file_STRIKE.write(line+'\n')

            if (cnt_of_blocks == list_of_list[1][1] and line[0] != '\n' and  cnt_of_empty_lines>=0):

                file_TC.write(line+'\n')

            if (cnt_of_blocks == list_of_list[2][1] and line[0] != '\n' and  cnt_of_empty_lines>=0):

                file_SP.write(line+'\n')

            if( cnt_of_empty_lines==2):
                cnt_of_blocks = cnt_of_blocks+1
                cnt_of_empty_lines=0


        file.close()
        file_STRIKE.close()
        file_SP.close()
        file_TC.close()

read= Read_FUN_VAR()

list_of_list = read.read_FUN("FUN.BB11001.tsv")

read.read_VAR("VAR.BB11001.tsv",list_of_list)