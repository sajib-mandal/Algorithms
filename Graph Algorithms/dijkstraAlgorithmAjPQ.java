import java.util.*;

public class Dijkstra_Algorithm {
    public static void main(String arg[]) {
        int Vertex = 6;
        int source_vertex = 0;
        //representation of graph will be the adjacency list
        List<List<Node> > Node_list = new ArrayList<List<Node> >();
        // For every node in the graph Initialize adjacency list
        for (int i = 0; i < Vertex; i++) {
            List<Node> item = new ArrayList<Node>();
            Node_list.add(item);
        }

        //The edges of the graph
        Node_list.get(0).add(new Node(1, 5));
        Node_list.get(0).add(new Node(4, 2));
        Node_list.get(0).add(new Node(2, 3));
        Node_list.get(1).add(new Node(5, 2));
        Node_list.get(1).add(new Node(4, 3));
        Node_list.get(2).add(new Node(3, 3));
        Node_list.get(2).add(new Node(4, 2));

        // Run the Dijkstra_Algorithm on the graph
        Graph_priority_queue gpq = new Graph_priority_queue(Vertex);
        gpq.Dijkstra_Algo(Node_list, source_vertex);

        // Printing the shortest path from source node to all other the nodes
        System.out.println("The shortest paths from source nodes to all other nodes:");
        System.out.println("Source_Node\t\t" + "Other_Node#\t\t" + "Path_Distance");
        for (int x = 0; x < gpq.distance.length; x++)
            System.out.println(source_vertex + " \t\t\t " + x + " \t\t\t "  + gpq.distance[x]);
    }
}

class Graph_priority_queue {
    int distance[];
    Set<Integer> visited_Node;
    PriorityQueue<Node> Priority_Queue;
    int Vertex; // vertices
    List<List<Node> > node_list;
    //constructor
    public Graph_priority_queue(int Vertex) {
        this.Vertex = Vertex;
        distance = new int[Vertex];
        visited_Node = new HashSet<Integer>();
        Priority_Queue = new PriorityQueue<Node>(Vertex, new Node());
    }

    // Dijkstra's Algorithm implementation
    public void Dijkstra_Algo(List<List<Node> > node_list, int source_vertex) {
        this.node_list = node_list;

        for (int x = 0; x < Vertex; x++) {
            distance[x] = Integer.MAX_VALUE;
        }
        // add the source vertex to the Priority Queue
        Priority_Queue.add(new Node(source_vertex, 0));

        // Distance of the source from source itself is 0
        distance[source_vertex] = 0;
        while (visited_Node.size() != Vertex) {

            //ux is deleted from the Priority Queue which has minimum distance
            int ux = Priority_Queue.remove().dj_node;

            // add the ux node to finalized list which is visited
            visited_Node.add(ux);
            Adjacent_Nodes_Graph(ux);
        }
    }
    // process all the neighbors of the just visited node
    private void Adjacent_Nodes_Graph(int ux){
        int Edge_Distance = -1;
        int New_Distance = -1;

        // process all neighboring nodes of ux
        for (int x = 0; x < node_list.get(ux).size(); x++) {
            Node vx = node_list.get(ux).get(x);

            //  if current node is not in 'visited'
            if (!visited_Node.contains(vx.dj_node)) {
                Edge_Distance = vx.dj_cost;
                New_Distance = distance[ux] + Edge_Distance;

                // compare the distances
                if (New_Distance < distance[vx.dj_node])
                    distance[vx.dj_node] = New_Distance;

                // Add the current vertex to the PriorityQueue
                Priority_Queue.add(new Node(vx.dj_node, distance[vx.dj_node]));
            }
        }
    }
}

// The Class to handle nodes
class Node implements Comparator<Node> {
    public int dj_node;
    public int dj_cost;
    public Node() { }

    public Node(int dj_node, int dj_cost) {
        this.dj_node = dj_node;
        this.dj_cost = dj_cost;
    }
    @Override
    public int compare(Node dj_node1, Node dj_node2) {
        if (dj_node1.dj_cost < dj_node2.dj_cost)
            return -1;
        if (dj_node1.dj_cost > dj_node2.dj_cost)
            return 1;
        return 0;
    }
}
