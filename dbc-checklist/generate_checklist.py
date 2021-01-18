# Fermilab link
# https://www.fnal.gov/cgi-bin/ecology/wildlife/bigbar?Greater+White-fronted+Goose

import pandas as pd
import math


html_start = """
<!-- template.html -->

<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">

    <!-- CSS -->

    <link rel="stylesheet" href="../../styles.css">
    <!-- Fonts -->

    <title></title>
  </head>
  <body>
    <div id="container">
        <div id="posts">
        <div id="birds">
    <h1>Dupage Birding Club Visual Checklist</h1>
"""

html_end = """
    </div>
    </div>
    </div>
  </body>
</html>
"""


def build_page(bird_data, output_file):
    html = html_start

    season, abundance = output_file.split('/')
    abundance = abundance.replace('.html', '')

    html += f'<u><h1>{season}</h1></u>'

    for s in ['winter', 'early-spring', 'late-spring', 'summer', 'post-breeding', 'early-fall', 'late-fall']:
        html += "<a href='https://kylepollina.github.io/earthscience/dbc-checklist/{}/common.html'>".format(s)
        html += "{}</a>".format(s.replace('-', ' '))
        if s != 'late-fall':
            html += " - "


    html += "<u><h3>{}</h3></u>".format(abundance.replace('-', ' '))

    for abd in ['abundant', 'common', 'fairly-common', 'uncommon', 'rare', 'extremely-rare']:
        html += "<a href='https://kylepollina.github.io/earthscience/dbc-checklist/{}/{}.html'>".format(season, abd)
        html += "{}</a>".format(abd.replace('-', ' '))
        if abd != 'extremely-rare':
            html += " - "

    for bird, row in bird_data.iterrows():
        html += f"<h1>{bird}</h1>"
        html += '<img src="{}" />'.format(row['img']) if isinstance(row['img'], str) else ''
        html += row['recording_embed_link']
        html += '<img src="{}" />'.format(row['migration'])

    html += html_end

    with open(output_file, 'w+') as f:
        f.write(html)


if __name__ == "__main__":
    df = pd.read_csv('bird_data.csv', index_col='bird')

    winter_birds = df.dropna(subset=['winter'])
    build_page(winter_birds[winter_birds['winter'] == '1 - abundant'], 'winter/abundant.html')
    build_page(winter_birds[winter_birds['winter'] == '2 - common'], 'winter/common.html')
    build_page(winter_birds[winter_birds['winter'] == '3 - fairly common'], 'winter/fairly-common.html')
    build_page(winter_birds[winter_birds['winter'] == '4 - uncommon'], 'winter/uncommon.html')
    build_page(winter_birds[winter_birds['winter'] == '5 - rare'], 'winter/rare.html')
    build_page(winter_birds[winter_birds['winter'] == '6 - extremely rare'], 'winter/extremely-rare.html')

    early_spring_birds = df.dropna(subset=['early spring'])
    build_page(early_spring_birds[early_spring_birds['early spring'] == '1 - abundant'], 'early-spring/abundant.html')
    build_page(early_spring_birds[early_spring_birds['early spring'] == '2 - common'], 'early-spring/common.html')
    build_page(early_spring_birds[early_spring_birds['early spring'] == '3 - fairly common'], 'early-spring/fairly-common.html')
    build_page(early_spring_birds[early_spring_birds['early spring'] == '4 - uncommon'], 'early-spring/uncommon.html')
    build_page(early_spring_birds[early_spring_birds['early spring'] == '5 - rare'], 'early-spring/rare.html')
    build_page(early_spring_birds[early_spring_birds['early spring'] == '6 - extremely rare'], 'early-spring/extremely-rare.html')

    # es_birds = df.dropna(subset=['early spring'])
    # build_page(es_birds, 'es_birds.html')

    # ls_birds = df.dropna(subset=['late spring'])
    # build_page(ls_birds, 'ls_birds.html')

    # summer_birds = df.dropna(subset=['summer'])
    # build_page(summer_birds, 'summer_birds.html')

    # pb_birds = df.dropna(subset=['post breeding'])
    # build_page(pb_birds, 'pb_birds.html')

    # ef_birds = df.dropna(subset=['early fall'])
    # build_page(ef_birds, 'ef_birds.html')

    # lf_birds = df.dropna(subset=['late fall'])
    # build_page(lf_birds, 'lf_birds.html')
