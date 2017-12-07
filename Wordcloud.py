from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt


String = "Technology affects people all over the world both postively and negatively While I do agree that advances in technology have made our countries safer and our lives easier they have also negatively affected our lives My parents did not grow up in front of a customer or a PlayStation They did not spend hours each day looking at what their virtual friends are doing on Facebook Instagram and Twitter Instead they went out with flesh and blood friends played football or simply took a walk in the woods But of course they didnt pay for an IceCream using a credit card and didnt buy movie tickets online"
wordcloud = WordCloud(stopwords = STOPWORDS, background_color = "white", width = 1200, height = 1000).generate(String)
plt.imshow(wordcloud)
plt.axis("off")
plt.show()

