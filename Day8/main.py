import numpy

SAMPLE_DATA: bool = False
filename = "sample_data.txt" if SAMPLE_DATA else "data.txt"
with open(filename, 'r') as f:
    data = f.read().splitlines()

visible_count = 0
scenic_score = 1
tree_map = numpy.array([[int(x, 10) for x in line] for line in data])
for i in range(len(tree_map)):
    for j in range(len(tree_map[i])):
        num = tree_map[i,j]

        left = tree_map[i,:j][::-1]
        right = tree_map[i, j+1:]
        top = tree_map[0: i, j][::-1]
        bottom = tree_map[i+1:, j]

        on_egde = False
        # part 1
        if any((len(x) == 0 for x in [left, right, top, bottom])):
            visible_count += 1
            on_egde = True
        elif any((numpy.max(x) < num for x in [left, right, top, bottom])):
            visible_count += 1
        cur_tree_scores = []
        # part 2
        
        if on_egde:
            continue
        for line in [left, right, top, bottom]:
            score_line = line < num
            if numpy.all(score_line):
                cur_line_score = len(line)
            else:
                cur_line_score = numpy.argmin(score_line) + 1
            cur_tree_scores.append(cur_line_score)
        cur_tree_scenic_score = numpy.prod(cur_tree_scores)
        if cur_tree_scenic_score > scenic_score:
            scenic_score = cur_tree_scenic_score
print(f'{visible_count} {scenic_score}')
