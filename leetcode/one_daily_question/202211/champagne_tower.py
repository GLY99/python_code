class Solution:
    @staticmethod
    def champagne_tower(poured: int, query_row: int, query_glass: int) -> float:
        """
        :param self:
        :param poured: 倾倒香槟的总杯数
        :param query_row: 行数, 0 <= query_row < 100
        :param query_glass: 杯子的位置数 0 <= query_glass < 100
        :return: 第query_row行 第query_glass个杯子香槟的容积数
        """
        dp_arr = [[0.0] * (query_row + 2) for _ in range(0, query_row + 2)]
        # 第一个杯子装入所有的酒
        dp_arr[0][0] = poured
        # 遍历所有的杯子
        for i in range(0, query_row + 1):
            for j in range(0, query_glass + 1):
                # 如果这个杯子可以装满
                if dp_arr[i][j] >= 1:
                    remain = dp_arr[i][j] - 1
                    dp_arr[i][j] = 1

                    # 下面的杯子平分溢出的酒
                    dp_arr[i + 1][j] += remain / 2.0
                    dp_arr[i + 1][j + 1] += remain / 2.0
        return dp_arr[query_row][query_glass]
