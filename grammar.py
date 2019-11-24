# import the client library
from grammarbot import GrammarBotClient


class GrammarChecker:
    def __init__(self):
        self.client = GrammarBotClient(api_key='KS9C5N3Y')

    def check(self, text, file=None):
        res = self.client.check(text)
        for match in res.matches:
            if file:
                file.write("Position {} \n Replacements {} \n Rule {} Category {} Type {}\n".format(match.replacement_offset, match.replacements, match.rule,
                                                                                       match.category, match.type))
            else:
                print("Position {} \n Replacements {} \n Rule {} Category {} Type {}\n".format(match.replacement_offset, match.replacements, match.rule,
                                                                                         match.category, match.type))
        return res


