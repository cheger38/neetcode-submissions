/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */

class Solution {
    public TreeNode buildTree(int[] preorder, int[] inorder) {
        if (preorder.length == 0) return null;
        if (preorder.length == 1) return new TreeNode(preorder[0]);

        TreeNode root = new TreeNode(preorder[0]);
        int rootIndex = -1;

        for (int i = 0; i < inorder.length; i++) {
            if (inorder[i] == root.val) {
                rootIndex = i;
                break;
            }
        }

        int[] leftin = new int[rootIndex];
        for (int i = 0; i < rootIndex; i++) {
            leftin[i] = inorder[i];
        }

        int[] rightin = new int[inorder.length - rootIndex - 1];
        for (int i = 0; i < rightin.length; i++) {
            rightin[i] = inorder[i + rootIndex + 1];
        }


        int preIndex = -1;
        for (int i = 0; i < preorder.length; i++) {
            if (preorder[i] == root.val) {
                preIndex = i;
                break;
            }
        }

        int[] leftpre = new int[leftin.length];
        for (int i = 0; i < leftpre.length; i++) {
            leftpre[i] = preorder[i + preIndex + 1];
        }

        int[] rightpre = new int[rightin.length];
        for (int i = 0; i < rightpre.length; i++) {
            rightpre[i] = preorder[i + preIndex + leftpre.length + 1];
        }

        root.left = buildTree(leftpre, leftin);
        root.right = buildTree(rightpre, rightin);
        return root;

        /**
        System.out.println("Root: " + root.val);

        System.out.print("Left Preorder: ");
        for (int i : leftpre) {
            System.out.print(i + " ");
        }
        System.out.println();

        System.out.print("Left Inorder: ");
        for (int i : leftin) {
            System.out.print(i + " ");
        }
        System.out.println();

        System.out.print("Right Preorder: ");
        for (int i : rightpre) {
            System.out.print(i + " ");
        }
        System.out.println();

        System.out.print("Right Inorder: ");
        for (int i : rightin) {
            System.out.print(i + " ");
        }
        System.out.println();
        
        return null;
        */

    }
}
