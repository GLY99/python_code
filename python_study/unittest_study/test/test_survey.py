import unittest
from unittest_study import anonymous_survey


class TestAnonymousSurvey(unittest.TestCase):
    """
    test anonymous survey
    """
    def setUp(self) -> None:
        question = "What language did you first learn to speak?"
        self.my_survey = anonymous_survey.AnonymousSurvey(question)
        self.responses = ["English", "Chinese", "Mandarin"]

    def test_store_single_response(self) -> None:
        """
        测试单个答案会被存储
        :return:
        """
        self.my_survey.store_response(self.responses[0])
        self.assertIn("English", self.my_survey.responses)

    def test_store_three_response(self) -> None:
        """
        测试单个答案会被存储
        :return:
        """
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()