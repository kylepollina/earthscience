all: index field-work

index:
	embedmd templates/index-template.html > index.html

field-work: FORCE
	embedmd templates/summer-survey-template.html > tmp
	jinja -D current_page earthscience -D title "summer 2020" tmp > field-work/summer-survey.html
	rm tmp

FORCE: ;
