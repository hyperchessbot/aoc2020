import re

bags_re = re.compile(r'(?P<quantity>\d{1,2}) (?P<bag_colour>[a-zA-Z ]+) bags?')

data = """shiny gold bags contain 2 dark red bags.
dark red bags contain 2 dark orange bags.
dark orange bags contain 2 dark yellow bags.
dark yellow bags contain 2 dark green bags.
dark green bags contain 2 dark blue bags.
dark blue bags contain 2 dark violet bags.
dark violet bags contain no other bags."""
data = data.split('\n')
with open('01.txt', 'r') as f:
    data = f.readlines()

graph = {}
graph_reverse = {}
for line in data:
    container, contained = line.split(' contain ')
    container = container.rsplit(' ', 1)[0]
    graph[container] = dict()
    for result in bags_re.findall(contained):
        graph[container][result[1]] = int(result[0])
        if result[1] in graph_reverse:
            graph_reverse[result[1]].append(container)
        else:
            graph_reverse[result[1]] = [container]
print(graph)
print(graph_reverse)

search = ['shiny gold']
results = set()
while search:
    item = search.pop()
    for cont in graph_reverse.get(item, ()):
        if cont not in results:
            results.add(cont)
            search.append(cont)
print("Part 1:", len(results))

search = ['shiny gold']
total = 0
while search:
    item = search.pop()
    for bag in graph[item]:
        for times in range(graph[item][bag]):
            search.append(bag)
            total += 1
print("Part 2:", total)