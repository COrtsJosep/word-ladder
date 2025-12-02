import tqdm
import rapidfuzz
import networkx as nx
from datasets import load_dataset

ds = load_dataset('softcatala/catalan-dictionary')
words = {entry.split(' ')[1].lower() for entry in ds['train']['text']}
words_from = list(words)
words_to = list(words)
words_to.reverse()

G = nx.Graph()
for w0 in tqdm.tqdm(words_from):
    for w1 in words_to:
        distance = rapidfuzz.distance.Levenshtein.distance(
                w0,
                w1,
                weights = (1, 1, 1),
                score_cutoff = 1,
            )
        if distance == 1:
            G.add_edge(w0, w1)
    _ = words_to.pop()

graph_filename = Path('G.graphml')
nx.write_graphml(G, graph_filename)
