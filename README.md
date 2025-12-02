# word-ladder
A hopeless quest to find the longest possible word ladder in Catalan.

## Project Description
Have you ever wondered what is the longest possible word ladder in Catalan? But first things first -- what is that? A word ladder is a chain of words, where each word differs in exactly one letter from the preceding word. For example, _think->thing->ting->king->kin_ is a word ladder of length five.

Well, at least I asked myself that. So I decided to look for a practical answer by writing a program that models the Catalan thesaurus as a graph, where each node is a word, and two nodes are connected iff they differ in exactly one letter (i.e., they lie at a Levenshtein distance of one from each other). Then we just have to solve the [longest path problem](https://en.wikipedia.org/wiki/Longest_path_problem) using [DFS](https://en.wikipedia.org/wiki/Depth-first_search)! Except... that the longest path problem is [NP-hard](https://en.wikipedia.org/wiki/NP-hardness), so my program would take centuries to run 😔

However, there is something that can be said: the length of the longest possible ladder, given the thesaurus, is upper-bounded by 30766 (the node count of the largest connected component). With my code I found one that starts with _pobil_ (=only child) and ends with _atufament_ (=stinkyness), with a length of 11203! You can find the whole ladder in [longest_lader.txt](longest_ladder.txt)

By the way, below you have a picture of the graph. A subset of ~50% of the words are interconnected to one another.

## Resources
I use the Catalan vocabulary from [Softcatalà](https://huggingface.co/datasets/softcatala/catalan-dictionary).

## Gallery
Here is the word graph:

<img width="600" height="595" alt="network" src="https://github.com/user-attachments/assets/4e191747-cfbe-4e1a-91df-307717d92c6a" />
