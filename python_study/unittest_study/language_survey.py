from unittest_study import anonymous_survey

question = "What language did you first learn to speak?"
my_survey = anonymous_survey.AnonymousSurvey(question)

my_survey.show_question()
print("Enter 'q' at any time to quit")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)
print("\nThank you to everyone who participated my survey")
my_survey.show_result()