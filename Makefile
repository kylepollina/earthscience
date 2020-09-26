all: index field-work research clean

index:
	embedmd templates/index-template.html > index.html

field-work: summer-survey fall-survey research

summer-survey: field-work/summer-survey.md
	embedmd templates/summer-survey-template.html > tmp
	jinja -D current_page earthscience -D title "summer 2020" tmp > field-work/summer-survey.html

fall-survey: field-work/fall-survey.md
	embedmd templates/fall-survey-template.html > tmp
	jinja -D current_page earthscience -D title "fall 2020" tmp > field-work/fall-survey.html

research: research/life-under-the-waves.md
	embedmd templates/life-under-the-waves-template.html > tmp
	jinja -D current_page earthscience -D title "Cool Life" tmp > research/life-under-the-waves.html

clean:
	rm tmp
