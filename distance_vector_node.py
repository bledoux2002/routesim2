from simulator.node import Node
import json
import copy

class Distance_Vector_Node(Node):
    def __init__(self, id):
        super().__init__(id)
        self.distance_vector = {} # { dest: cost } 
        self.neighbors_dict = {} # { direct_neighbor: (cost, next_hop)}
        self.seen = {} # Tracking sequence numbers { dest: seq }
        self.sequence_number = 0
 
    # Return a string
    def __str__(self):
        """
        Prints represenation of node state for debugging purposes,
        not strictly necessary to implement but helpful
        
        Parameters:
        None

        Returns:
        state (str): representation of node state
        
        """
        return "Rewrite this function to define your node dump printout"

    # Called to inform Node that outgoing link properties have changed
    def link_has_been_updated(self, neighbor, latency):
        """
        Updates node tables with new latency to reach neighbor,
        and forwards this update to node's neighbors.

        Parameters:
        neighbor (Node): neighbor sending the update
        latency (float): new latency to reach neighbor

        Returns:
        None
        """

        if latency == -1:
            self.neighbors_dict[neighbor] = latency # Set to -1
        else:
            # New node... Add it to the distance vector and neighbors dict
            if neighbor not in self.neighbors_dict:
                self.distance_vector[neighbor] = (latency, neighbor)
            self.neighbors_dict[neighbor] = latency

        # Calculate Bellman-Ford algorithm. If DV changes, forward to neighbors.

                    


    def process_incoming_routing_message(self, m):
        """
        Choose course of action for message, sending message to
        neighbor(s) and/or updating tables

        Parameters:
        m (str): routing message

        Returns:
        None
        
        """
        message = json.loads(m)
        print("Received message:", message)

        neighbor = message['neighbor']
        neighbor_dv = message['neighbor_dv']
        seq = self.sequence_number

        if neighbor in self.seen:
            if seq <= self.seen[neighbor]:
                return  
        
        # New message!
        self.seen[neighbor] = seq  

        # Calculate Bellman-Ford algorithm. If DV changes, send to neighbors
                
            
    def bellman_ford(self):
        pass

    # Return a neighbor, -1 if no path to destination
    def get_next_hop(self, destination):
        """
        Node is asked which hop it THINKS is next on path to destination
        
        Parameters:
        destination (Node): final destination being searched for
        
        Returns:
        hops (int): next Node to reach destination
        
        """
        print("NEXT HOP")
        print(self.distance_vector)
        print(self.id)
        print(destination)
        if destination in self.distance_vector:
            _, next_hop = self.distance_vector[destination]
            return next_hop
        return -1

        


