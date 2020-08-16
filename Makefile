all: index ecology resources

index:
	embedmd template.html > index.html

ecology:
	embedmd ecological-survey-template.html > ecological-survey.html

resources:
	embedmd resources-template.html > resources.html
