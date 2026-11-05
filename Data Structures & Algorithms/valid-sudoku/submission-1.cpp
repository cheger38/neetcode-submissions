class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        auto getBox = [](int i, int j) {
            return (i / 3) * 3 + j / 3;
        };

        vector<set<int>> rows(9);
        vector<set<int>> cols(9);
        vector<set<int>> boxes(9);

        for (int i = 0; i < 9; i++) {
            for (int j = 0; j < 9; j++) {
                char val = board[i][j];
                if (val == '.') {
                    continue;
                }

                if (
                    rows[i].contains(val) ||
                    cols[j].contains(val) ||
                    boxes[getBox(i, j)].contains(val)
                ) {
                    return false;
                }

                rows[i].insert(val);
                cols[j].insert(val);
                boxes[getBox(i, j)].insert(val);
            }
        }

        return true;

    }
};
