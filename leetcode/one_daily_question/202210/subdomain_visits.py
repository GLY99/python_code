from typing import List


class Solution:
    def subdomain_visits(self, cpdomains: List[str]) -> List[str]:
        """
        子域名访问计数
        :param cpdomains:
        :return:
        """
        visits_dict = dict()
        for domain_str in cpdomains:
            visit_count = int(domain_str.split(' ')[0])
            domains = domain_str.split(' ')[1]
            domain_list = domains.split('.')
            for loop_count in range(len(domain_list)):
                domain = '.'.join(domain_list[loop_count:])
                visits_dict[domain] = visits_dict.get(domain, 0) + visit_count
        return [str(count) + '' + domain for domain, count in visits_dict.items()]


if __name__ == "__main__":
    solution = Solution()
    cpdomains = ["9001 discuss.leetcode.com"]
    ans_list = solution.subdomain_visits(cpdomains)
    print(ans_list)