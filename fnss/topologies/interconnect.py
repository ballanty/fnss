import networkx as nx
from fnss.topologies.topology import Topology

__all__ = ['hypercube_topology']

def hypercube_topology(n):
    """
    Return a hypercube topology of 2^n hosts/switches.

    See: https://en.wikipedia.org/wiki/Hypercube_internetwork_topology

    Parameters
    ----------
      n : int
         The order of the hypercube.  Order n means 2^n nodes.

    Returns
    -------
    topology: Topology object
    """

    # validate input size
    if not isinstance(n, int):
        raise TypeError('n must be an integer')
    if n < 1:
        raise ValueError('n must be >= 1')

    interconnect = Topology(nx.hypercube_graph(n))
    interconnect.name = 'hypergraph_topology(n=%d, size=%d)' % (n, 2**n)
    interconnect.graph['type'] = 'hypergraph'
    return interconnect