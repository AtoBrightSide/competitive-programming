
// Definition for a binary tree node.
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val === undefined ? 0 : val)
        this.left = (left === undefined ? null : left)
        this.right = (right === undefined ? null : right)
    }
}

class FindElements {
    allNodes: Set<number>;
    constructor(root: TreeNode) {
        this.allNodes = new Set();
        const traverse = (root: TreeNode | null, currVal: number) => {
            if (root === null) return

            this.allNodes.add(currVal);
            traverse(root.left, currVal * 2 + 1);
            traverse(root.right, currVal * 2 + 2);
        }

        root.val = 0;
        traverse(root, 0)
    }

    find(target: number): boolean {
        return this.allNodes.has(target);
    }
}

/**
 * Your FindElements object will be instantiated and called as such:
 * var obj = new FindElements(root)
 * var param_1 = obj.find(target)
 */