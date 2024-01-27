# nav-algorithms: Navigation Algorithms

A repository for [hopefully] clean, readable, and easily-called implementations of some navigation,
path planning, and obstacle avoidance algorithms I will be using in the near future, written in modern
Python and/or Rust with Python bindings. I'll be adding more algorithm implementations over time.

## Algorithms: Currently implemented + planned
* [A*](https://en.wikipedia.org/wiki/A*_search_algorithm) - Graph path search algorithm.
  * code-complete in both Python and Rust, but Rust needs to be modified to accept other distance heuristics.
  * Needs a more thorough test suite.
* [Probabilistic Roadmap (PRM)](https://en.wikipedia.org/wiki/Probabilistic_roadmap) - Robot navigation algorithm with obstacle avoidance.
  * Planned.

## Usage

### A\* (Python)
```python
from modgeosys.nav.a_star import a_star
from modgeosys.nav.types import Edge, Graph
from modgeosys.nav.distance import manhattan_distance, euclidean_distance

# Define a graph.
nodes = [(0.0, 0.0), (0.0, 2.0), (1.0, 0.0), (2.0, 1.0), (2.0, 3.0)]
edges = (Edge(weight=2.0, node_indices=frozenset((0, 1)), f=None, g=None),
         Edge(weight=1.0, node_indices=frozenset((0, 2)), f=None, g=None),
         Edge(weight=1.0, node_indices=frozenset((2, 3)), f=None, g=None),
         Edge(weight=3.0, node_indices=frozenset((1, 4)), f=None, g=None),
         Edge(weight=1.0, node_indices=frozenset((3, 4)), f=None, g=None))
graph = Graph(nodes=nodes, edges=edges)

# Call the A* function.
path = a_star(graph=graph, start_node_index=0, goal_node_index=4, heuristic_distance=manhattan_distance)

# Report the resulting path.
print(path)
```

### A\* (Rust)
```rust
use modgeosys::nav::a_star::a_star;
use modgeosys::nav::types::{Node, Edge, Graph};
use modgeosys::nav::distance::{manhattan_distance, euclidean_distance};

// Define a graph.
let nodes = vec![Node::new(0.0, 0.0), Node::new(0.0, 2.0), Node::new(1.0, 0.0), Node::new(2.0, 1.0), Node::new(2.0, 3.0)];
let edges = vec![Edge::new(2.0, HashSet::from([0, 1]), None, None),
                 Edge::new(1.0, HashSet::from([0, 2]), None, None),
                 Edge::new(1.0, HashSet::from([2, 3]), None, None),
                 Edge::new(3.0, HashSet::from([1, 4]), None, None),
                 Edge::new(1.0, HashSet::from([3, 4]), None, None)];
let graph = Graph::new(nodes, edges);

// Call the A* function.
let path = a_star(&graph, 0, 4).unwrap();

// Report the resulting path.
println!("{:?}", path);
```