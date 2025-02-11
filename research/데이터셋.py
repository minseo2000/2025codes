import datasets
dataset = datasets.load_dataset("jaehy12/news3")
element = dataset["train"][1]
print(element)
