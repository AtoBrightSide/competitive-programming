function mostProfitablePath(edges: number[][], bob: number, amount: number[]): number {
    let graph = new Map(), bobTimer = new Map();
    let bobPath: number[] = [];

    // function to build the tree
    const buildGraph = () => {
        for (const [a, b] of edges) {
            if (!graph.has(a)) graph.set(a, []);
            if (!graph.has(b)) graph.set(b, []);

            graph.get(a).push(b);
            graph.get(b).push(a);
        }
    }

    // function to find bob's path to node 0
    const findPathToRoot = (node: number, seen: Set<number>): boolean => {
        bobPath.push(node);
        seen.add(node);

        if (node === 0) return true;

        for (const adjacentNode of graph.get(node)) {
            if (!(seen.has(adjacentNode)) && findPathToRoot(adjacentNode, seen)) {
                return true;
            }
        }

        bobPath.pop();
        return false;
    }

    // function to check who got to this node first
    const whoReachedFirst = (node: number, time: number): number => {
        if (!bobTimer.has(node)) {
            return amount[node];
        } else if (bobTimer.get(node) === time) {
            return amount[node] / 2;
        } else if (bobTimer.get(node) < time) {
            return 0
        } else {
            return amount[node]
        }
    }

    // function to find alice's max income by travelling to the optimal leaf node
    const getMaxIncome = (node: number, time: number, seen: Set<number>): number => {
        // if a leaf node has been found
        if (node !== 0 && graph.get(node).length === 1) return whoReachedFirst(node, time);

        const currIncome = whoReachedFirst(node, time);

        seen.add(node);
        let maxIncome = -Infinity;
        for (const adjacentNode of graph.get(node)) {
            if (!seen.has(adjacentNode)) {
                maxIncome = Math.max(maxIncome, getMaxIncome(adjacentNode, time + 1, seen));
            }
        }

        return currIncome + maxIncome;
    }

    buildGraph();
    findPathToRoot(bob, new Set())

    // store the time bob reaches each node in his path
    bobPath.forEach((node, index) => {
        bobTimer.set(node, index);
    })

    const maxIncome = getMaxIncome(0, 0, new Set());
    return maxIncome;
};