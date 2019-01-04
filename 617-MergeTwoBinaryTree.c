struct TreeNode* mergeTrees (struct TreeNode* t1, struct TreeNode* t2) {
    if (t1 && t2) {
        t1->val = t1->val + t2->val;
        t1->left = mergeTrees(t1->left, t2->left);
        t1->right = mergeTrees(t1->right, t2->right);
        return t1;
    }
    return t1 ? t1 : t2;
}