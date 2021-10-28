import wikipedia, webbrowser
wikipage = wikipedia.random(1)
wikiload = wikipedia.page(wikipage)
print(wikipedia.summary(wikipage))
