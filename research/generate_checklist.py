# Fermilab link
# https://www.fnal.gov/cgi-bin/ecology/wildlife/bigbar?Greater+White-fronted+Goose

import pandas as pd

def generate_checklists():
    final_html = """
    <!-- template.html -->

    <!DOCTYPE html>
    <html>
      <head>
        <meta charset="UTF-8">

        <!-- CSS -->

        <!-- Fonts -->

        <title></title>
      </head>
      <body>
        <div id="container">
    """

    final_html_end = """
        </div>
      </body>
    </html>
    """

    df = pd.read_csv('bird_data.csv')

    for index, row in df.iterrows():
        bird = row['bird']
        abundance = row['abundance']
        img = row['img']
        ebird = row['ebird']
        wikipedia = row['wikipedia']
        migration = row['migration']
        recording = row['recording']
        male = row['male']
        female = row['female']

        final_html += f"""
        <div>
            <h1>{bird}</div>
            <img src='{img}'/>
        </div>
        """

    final_html += final_html_end

    with open('output.html', 'w') as f:
        f.write(final_html)

if __name__ == "__main__":
    generate_checklists()
