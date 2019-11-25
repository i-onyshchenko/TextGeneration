from generation import TextGenerator
from grammar import GrammarChecker


def demo_console():
    prompt = input("Enter your text >>")

    print("Your text: ", prompt)
    grammar_checker = GrammarChecker()
    length = 20

    models = ['gpt2', 'gpt2-medium', 'gpt2-large']

    for model in models:
        gpt2 = TextGenerator(model_name_or_path=model)
        output_text = gpt2.generate(prompt, length=length)
        print(model + '\n' + output_text + '\n')
        grammar_checker.check(output_text)


def demo_file():
    # tale = "Once upon a time there were Three Bears, who lived together in a house of their own, in a wood. One of them was a Little, Small Wee Bear; and one was a Middle-sized Bear, and the other was a Great, Huge Bear. They had each a pot for their porridge, a little pot for the Little, Small, Wee Bear; and a middle-sized pot for the Middle Bear, and a great pot for the Great, Huge Bear. And they had each a chair to sit in; a little chair for the Little, Small, Wee Bear; and a middle-sized chair for the Middle Bear; and a great chair for the Great, Huge Bear. And they had each a bed to sleep in; a little bed for the Little, Small, Wee Bear; and a middle-sized bed for the Middle Bear; and a great bed for the Great, Huge Bear."
    tale = "Once upon a time down on an old farm, lived a duck family, and Mother Duck had been sitting on a clutch of new eggs. One nice morning, the eggs hatched and out popped six chirpy ducklings. But one egg was bigger than the rest, and it didn't hatch. Mother Duck couldn't recall laying that seventh egg. How did it get there? TOCK! TOCK! The little prisoner was pecking inside his shell."
    article = "The core idea behind the Transformer model is self-attention—the ability to attend to different positions of the input sequence to compute a representation of that sequence. Transformer creates stacks of self-attention layers and is explained below in the sections Scaled dot product attention and Multi-head attention."
    news = "Two Soviet-born Americans who form a key link between Donald Trump and Ukraine “weren’t James Bond”, the president’s lawyer, Rudy Giuliani, said on Saturday, insisting the men “didn’t have personal communications with the president” during a time period under intense scrutiny in the impeachment inquiry."

    print("Length of Tale {} words".format(tale.count(' ') + 1))
    print("Length of Article {} words".format(article.count(' ') + 1))
    print("Length of News {} words".format(news.count(' ') + 1))

    grammar_checker = GrammarChecker()

    f = open('gen_results_grammar', 'w+')
    # f.write(tale + '\n\n')
    # f.write(article + '\n\n')
    # f.write(news)

    length = 100

    models = ['gpt2', 'gpt2-medium', 'gpt2-large']

    for item in [tale, article, news]:
        f.write(item + '\n')

    f.write('\n\nGenerated\n')

    for model in models:
        gpt2 = TextGenerator(model_name_or_path=model)
        f.write(model + '\n')
        for i, item in enumerate([tale, article, news]):
            output_text = gpt2.generate(item, length=length)
            f.write(str(i+1) + '. ' + output_text + '\n')
            grammar_checker.check(output_text, f)

        f.write('\n')


    # gpt2_small = TextGenerator(model_name_or_path='gpt2')
    # gpt2_medium = TextGenerator(model_name_or_path='gpt2-medium')
    # gpt2_large = TextGenerator(model_name_or_path='gpt2-large')
    # gpt2_xl = TextGenerator(model_name_or_path='gpt2-xl')
    #
    # for item in [tale, article, news]:
    #     f.write(item + '\nGenerated:\n')
    #     for i, gpt2 in enumerate([gpt2_small, gpt2_medium, gpt2_large, gpt2_xl]):
    #         f.write(str(i+1) + ". " + gpt2.generate(item, length=length) + '\n\n')
    #
    #     f.write('\n')

    f.close()


if __name__ == "__main__":
    demo_console()