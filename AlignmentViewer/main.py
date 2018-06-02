'''
author: Marco Muñoz Perez
email: marcomunozperez@uma.es
bitbucket: @mampz

TODO CONVERT INTO CLASS.
'''

from collections import OrderedDict
from string import ascii_lowercase
import plotly
from Bio import SeqIO

LETTERS = {letter: index for index, letter in enumerate(ascii_lowercase, start=1)}
LETTERS['-'] = -1


def alphabet_position(text):
    text = text.lower()
    numbers = [LETTERS[character] for character in text if character in LETTERS]
    return numbers


def plot_alignment(numbered_sequences):
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


def process_fna(filepath):
    fna = SeqIO.parse(filepath, "fasta")
    sequence_dict = OrderedDict()
    for sequence in fna:
        sequence_dict[str(sequence.id)] = alphabet_position(sequence)

    return sequence_dict


def reduce_alignment_color(alignment_dict):
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


plot_alignment(reduce_alignment_color(process_fna('filtered_haplotypes.afa')))
