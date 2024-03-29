// Usage example(s).

use std::collections::HashSet;

use modgeosys_nav::a_star::a_star;
use modgeosys_nav::types::{Node, Edge, Graph};
use modgeosys_nav::distance::manhattan_distance;



fn main()
{
    // Define a graph.
    let nodes = vec![Node::new(vec![0.0, 0.0]),
                     Node::new(vec![0.0, 2.0]),
                     Node::new(vec![1.0, 0.0]),
                     Node::new(vec![2.0, 1.0]),
                     Node::new(vec![2.0, 3.0])];
    let edges = vec![Edge::new(2.0, HashSet::from([0, 1])),
                     Edge::new(1.0, HashSet::from([0, 2])),
                     Edge::new(1.0, HashSet::from([2, 3])),
                     Edge::new(3.0, HashSet::from([1, 4])),
                     Edge::new(1.0, HashSet::from([3, 4]))];
    let graph = Graph::new(nodes, edges);

    // Call the A* function.
    let path = a_star(&graph, 0, 4, manhattan_distance).unwrap();

    // Report the resulting path.
    println!("{:?}", path);
}
