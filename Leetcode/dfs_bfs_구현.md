```python 
def recursive_dfs(v, graph, discorved=[], searching=[]):
  searching.append(v)
  discorved.append(v)
  if not graph[v] or all(ele in discorved for ele in graph[v]):
    for vertext in searching:
        print(vertext, "->", end="")
    print()
  for w in graph[v]:
    if w not in discorved:
        recursive_dfs(w, graph, discorved, searching)
  searching.remove(v)
  
def iterative_dfs(v, graph):
    from collections import deque, defaultdict
    
    searching_stack = deque()
    searching_stack.append(v)
    discorved = [v]
    parent_child_dict = defaultdict(int)
    parent_child_dict[1] = 0
    while searching_stack:
        peek = searching_stack[-1]
        if not graph[peek] or all(ele in discorved for ele in graph[peek]):
            while parent_child_dict[peek]:
                print("<-", peek, end="")
                peek = parent_child_dict[peek]
            print("<-", v, end="")
            print()
            searching_stack.pop()
            continue
        root = searching_stack.pop()
        for w in graph[root]:
            if w not in discorved:
                discorved.append(w)
                parent_child_dict[w] = root
                searching_stack.append(w)
                
def iterative_bfs(v, graph):
    from collections import defaultdict, deque
    
    discorved = set()
    discorved.add(v)
    searching_queue = deque()
    searching_queue.append(v)
    while searching_queue:
        poped = searching_queue.popleft()
        print(poped, "->", end="")
        if graph[poped] and any([child for child in graph[poped] if child not in discorved]):
            print("(", end="")
            for child in graph[poped]:
                if child not in discorved:
                    print(child, ", ", end="")
                    discorved.add(child)
                    searching_queue.append(child)
            print("), ", end="")
        else:
            print("None ", end="")
    print()
        
```

