all: index ecology

index:
	embedmd templates/template.html > index.html

ecology:
	embedmd templates/ecological-survey-template.html > ecological-survey.html
