class AnonymousSurvey(object):
    """
    收集调查答案
    """
    def __init__(self, question: str) -> None:
        """
        init class AnonymousSurvey
        :param question:
        :return:
        """
        super(AnonymousSurvey, self).__init__()
        self.question = question
        self.responses = list()

    def show_question(self) -> None:
        """
        show question
        :return: str
        """
        question = self.question
        print(question)

    def store_response(self, new_responses: str) -> None:
        """
        store response
        :param new_responses:
        :return:
        """
        self.responses.append(new_responses)

    def show_result(self) -> None:
        """
        show all result
        :return:
        """
        print("Survey result:")
        for response in self.responses:
            print(f"- {response}")
