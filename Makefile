all: index field-work

index:
	embedmd templates/index-template.html > index.html

field-work: FORCE summer-survey fall-survey

summer-survey:
	embedmd templates/summer-survey-template.html > tmp
	jinja -D current_page earthscience -D title "summer 2020" tmp > field-work/summer-survey.html
	rm tmp

fall-survey:
	embedmd templates/fall-survey-template.html > tmp
	jinja -D current_page earthscience -D title "fall 2020" tmp > field-work/fall-survey.html
	rm tmp

FORCE: ;
