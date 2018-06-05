'''
author: Marco Muñoz Perez
email: marcomunozperez@uma.es
github: @mmp1100000
bitbucket: @mampz
'''

from collections import OrderedDict
from string import ascii_lowercase
import plotly
from Bio import SeqIO
import sys


class ViewMSA:
    """
    This class generates a HTML heatmap that visualizes a MSA. Output file is
    alignment_representation.html.

    Usage: python3 /msa/file/path.afa
    """

    def __init__(self, file_in):
        self.LETTERS = {letter: index for index, letter in enumerate(ascii_lowercase, start=1)}
        self.LETTERS['-'] = -1
        # self.plot_alignment(self.reduce_alignment_color(self.process_fna(file_out)))
        self.plot_alignment(self.process_fna(file_in))

    def alphabet_position(self, text):
        """
        Converts a string (sequence to a list of numbers).
        :param sequence:
        :return: list of numbers
        """
        text = text.lower()
        numbers = [self.LETTERS[character] for character in text if character in self.LETTERS]
        return numbers

    @staticmethod
    def plot_alignment(numbered_sequences):
        """
        Plots the dictionary as a heatmap in Plotly
        :param numbered_sequences:
        :return:
        """
        y = list(numbered_sequences)
        z = list(numbered_sequences.values())
        x = list(range(len(z[0])))
        trace = plotly.graph_objs.Heatmap(z=z,
                                          x=x,
                                          y=y,
                                          showscale=False)
        layout = plotly.graph_objs.Layout(
            title='MSA Preview',
            xaxis=dict(ticks=''),
            yaxis=dict(ticks=''),
            showlegend=True
        )
        data = [trace]
        fig = plotly.graph_objs.Figure(data=data, layout=layout)
        plotly.offline.plot(fig, filename='alignment_representation.html')

    def process_fna(self, file_path):
        """
        Read the fasta file and store sequences to ordered dictionary
        :param file_path:
        :return: dictionary of sequence id:sequence as numbers
        """
        fna = SeqIO.parse(file_path, "fasta")
        sequence_dict = OrderedDict()
        for sequence in fna:
            sequence_dict[str(sequence.id)] = self.alphabet_position(sequence)

        return sequence_dict

    @staticmethod
    def reduce_alignment_color(alignment_dict):
        # Optional function as an alternative to the main plot representation
        for sequence_position in range(len(alignment_dict[list(alignment_dict.keys())[0]])):
            number = alignment_dict[list(alignment_dict.keys())[0]][sequence_position]
            value = 0
            for key in alignment_dict:
                if alignment_dict[key][sequence_position] != number:
                    value = 1
                    break
            for key in alignment_dict:
                alignment_dict[key][sequence_position] = value

        return alignment_dict


if __name__ == "__main__":
    ViewMSA(sys.argv[1])
