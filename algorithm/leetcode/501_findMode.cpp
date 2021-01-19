class Solution {
public:
	vector<int> findMode(TreeNode* root) {
		vector<int>res;
		vector<int>v;
		if (root == NULL)return res;


		inOrder(root, v);
		int curTimes = 1, maxTimes = 1;
		res.push_back(v[0]);//初始化
		for (int i = 1; i < v.size(); i++)//求递增数组v的众数
		{
			if (v[i] == v[i - 1])
				curTimes++;
			else
				curTimes = 1;
			if (curTimes == maxTimes)
				res.push_back(v[i]);//因为可能出现多个众数，他们的出现次数均相同
			else if (curTimes > maxTimes)
			{
				res.clear();
				maxTimes = curTimes;
				res.push_back(v[i]);
			}
		}



		return res;

	}
	void inOrder(TreeNode* root, vector<int>& v)
	{
		if (root == NULL) return;//递归结束的条件
		//递归左子树
		inOrder(root->left, v);
		
		v.push_back(root->val);
		
		//递归右子树
		inOrder(root->right, v);

	}
};
