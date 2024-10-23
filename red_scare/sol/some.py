"""
Discussed solution:
Use BFS, spanning tree, or another shortest path algorithm, from each red node to 
find paths to both the start and end nodes.
It will maybe be needed to do this from all red nodes.
We may be able to use dynamic programming to avoid redundant work - but we
can not see how to do this so far.

Another discussed solution:
Use a path algorithm from s to t and from t to s.
Here we should save the set of all the red nodes encountered when running.
After we can compare if these two sets include a common element.
OBS: Ensure that the path finding does not continue after finding either s or t.

Return:
True if a path from s to t includes a red node, False otherwise.
"""
