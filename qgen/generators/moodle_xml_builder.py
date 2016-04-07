import os

generated_quiz_path = os.getcwd() + "/generated_quizzes/"


# TODO: Evaluate generation of an xml title
class QuizBuilder(object):
    def __init__(self, xml_title):
        self.xml_title = xml_title.lower().replace(" ", "_")

    def setup(self):
        if not os.path.exists(generated_quiz_path):
            os.makedirs(generated_quiz_path)

        result = "<?xml version=\"1.0\" encoding=\"UTF-8\"?>"
        result += "<quiz>\n" \
                  "<!-- question: 0  -->\n" \
                  "\t<question type=\"category\">\n" \
                  "\t\t<category>\n" \
                  "\t\t\t<text>Generated by QGen</text>\n" \
                  "\t\t</category>\n" \
                  "\t</question>\n"
        with open (generated_quiz_path + self.xml_title + ".xml", "w") as output_file:
            output_file.write(result)
        output_file.close()

    def build_question_for_xml(self, title=None, text=None, type=None):
        result = "\n\t<question type=\"" + type + "\">"
        result += "<name>\n" + "\t\t<text>" + title + "</text>\n" + "\t\t</name>"
        result += "<questiontext format=\"html\">\n" + "\t\t<text>" + text + "</text>\n" + "\t\t</questiontext>"
        result += "<generalfeedback format=\"html\">\n" \
                  "\t\t<text></text>\n" \
                  "\t\t</generalfeedback>\n" \
                  "\t\t<defaultgrade>1.0000000</defaultgrade>\n" \
                  "\t\t<penalty>0.1000000</penalty>\n" \
                  "\t\t<hidden>0</hidden>\n" \
                  "\t\t<single>true</single>\n" \
                  "\t\t<shuffleanswers>true</shuffleanswers>\n" \
                  "\t\t<answernumbering>abc</answernumbering>\n" \
                  "\t\t<correctfeedback format=\"html\">\n" \
                  "\t\t\t<text></text>\n" \
                  "\t\t</correctfeedback>\n" \
                  "\t\t<partiallycorrectfeedback format=\"html\">\n" \
                  "\t\t\t<text></text>\n" \
                  "\t\t</partiallycorrectfeedback>\n" \
                  "\t\t<incorrectfeedback format=\"html\">\n" \
                  "\t\t\t<text></text>\n" \
                  "\t\t</incorrectfeedback>\n"
        with open (generated_quiz_path + self.xml_title + ".xml", "a+") as output_file:
            output_file.write(result)
        output_file.close()

    def build_answer_for_xml(self, text, correct_feedback=None, fraction_amount="100"):
        if correct_feedback is None:
            correct_feedback = ''
        if fraction_amount == '':
            fraction_amount = "100"
        result = "\n\t\t<answer fraction=\"" + fraction_amount + "\" format=\"moodle_auto_format\">\n" + "\t\t\t<text>" + text + \
                 "</text>\n" \
                 "\t\t\t<feedback format=\"html\">\n" \
                 "\t\t\t\t<text>" + correct_feedback + "</text>\n" \
                                                       "\t\t\t</feedback>\n" \
                                                       "\t\t</answer>\n"
        with open(generated_quiz_path + self.xml_title + ".xml", "a+") as output_file:
            output_file.write(result)
        output_file.close()

    def build_distractor_for_xml(self, text, incorrect_feedback=None, fraction_amount="0"):
        if incorrect_feedback is None:
            incorrect_feedback = ''
            if fraction_amount == '':
                fraction_amount = "0"
        result = "\n\t\t<answer fraction=\"" + fraction_amount + "\" format=\"moodle_auto_format\">\n" + "\t\t\t<text>" + text + \
                 "</text>\n" \
                 "\t\t\t<feedback format=\"html\">\n" \
                 "\t\t\t\t<text>" + incorrect_feedback + "</text>\n" \
                                                         "\t\t\t</feedback>\n" \
                                                         "\t\t</answer>\n"
        with open(generated_quiz_path + self.xml_title + ".xml", "a+") as output_file:
            output_file.write(result)
        output_file.close()

    def build_question_end_tag(self):
        result = "\t</question>\n\n"
        with open(generated_quiz_path + self.xml_title + ".xml", "a+") as output_file:
            output_file.write(result)
        output_file.close()

    def build_quiz_end_tag(self):
        result = "</quiz>"
        with open(generated_quiz_path + self.xml_title + ".xml", "a+") as output_file:
            output_file.write(result)
        output_file.close()