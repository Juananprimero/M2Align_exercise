from string import ascii_lowercase
import plotly

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
    trace = plotly.graph_objs.Heatmap(z=z, x=x, y=y)
    layout = plotly.graph_objs.Layout(
        title='MSA Preview',
        xaxis=dict(ticks=''),
        yaxis=dict(ticks='')
    )
    data = [trace]
    fig = plotly.graph_objs.Figure(data=data, layout=layout)
    plotly.offline.plot(fig, filename='alignment_representation.html')


def process_fna(filepath):
    with open(filepath, 'r') as fna:
        sequence_dict = dict()
        header = fna.readline()
        while header != '':
            sequence_dict[header] = alphabet_position(fna.readline().strip())
            header = fna.readline()
    return sequence_dict


#plot_alignment(process_fna('VAR.BB11001.tsv'))
