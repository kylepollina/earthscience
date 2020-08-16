all: index ecology

index:
	embedmd template.html > index.html

ecology:
	embedmd ecological-survey-template.html > ecological-survey.html
