from bs4 import BeautifulSoup
import pandas as pd

# Description: This script parses the HTML content of the business ideas and saves it to a CSV file
# Source: https://offers.hubspot.com/business-idea-database

html_content = """
<div id="hs_cos_wrapper_widget_1709668248051" class="hs_cos_wrapper hs_cos_wrapper_widget hs_cos_wrapper_type_module" style="" data-hs-cos-general-type="widget" data-hs-cos-type="module">
  <section id="widget_1709668248051" class="csol-section csol-full-width-cta-card -light -padding-top-md -padding-bottom-md">
    <div class="csol-section-wrapper">
      <div class="csol-full-width-cta-card-container cl-card -border -right ">
        <div class=" csol-full-width-cta-card-image">
          <div class="csol-full-width-cta-card-graphic-container "></div>
          <div class="csol-full-width-cta-card-background">
            <img src="https://www.hubspot.com/hs-fs/hubfs/61-2.png?width=1080&amp;height=1080&amp;name=61-2.png" alt="61-2" class="csol-full-width-cta-card-background-image" width="1080" height="1080" loading="lazy" srcset="https://www.hubspot.com/hs-fs/hubfs/61-2.png?width=540&amp;height=540&amp;name=61-2.png 540w, https://www.hubspot.com/hs-fs/hubfs/61-2.png?width=1080&amp;height=1080&amp;name=61-2.png 1080w, https://www.hubspot.com/hs-fs/hubfs/61-2.png?width=1620&amp;height=1620&amp;name=61-2.png 1620w, https://www.hubspot.com/hs-fs/hubfs/61-2.png?width=2160&amp;height=2160&amp;name=61-2.png 2160w, https://www.hubspot.com/hs-fs/hubfs/61-2.png?width=2700&amp;height=2700&amp;name=61-2.png 2700w, https://www.hubspot.com/hs-fs/hubfs/61-2.png?width=3240&amp;height=3240&amp;name=61-2.png 3240w" sizes="(max-width: 1080px) 100vw, 1080px">
          </div>
        </div>
        <div class="csol-full-width-cta-card-content">
          <h3 class="csol-full-width-cta-card-header">Creator-Driven Brands</h3>
          <p class="csol-full-width-cta-card-description -large">Partner with popular musicians, figures, creators, and influencers to develop a range of products aligned to the partner’s personal brand and persona with them as the face of the brand. Think WrestleMania with Logan Paul/KSI.</p>
          <div>
            <div class="csol-full-width-cta-card-ctas">
              <a class="cl-button -primary -medium -light" href="https://youtu.be/eV8Wf4XWn-A?si=3tApEysxFMSL7sRM&amp;t=1271&amp;hubs_signup-url=offers.hubspot.com%2Fmfm-business-idea&amp;hubs_signup-cta=Submit" rel="noreferrer " target="_blank">
                Listen to the Episode
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</div>
"""

with open("ideas.html", "r") as file:
  html_content = file.read()

soup = BeautifulSoup(html_content, "html.parser")


ideas = {}

divs = soup.findAll("div", class_="csol-full-width-cta-card-container")

for i, div in enumerate(divs):
  try:
    title = div.find("h3", class_="csol-full-width-cta-card-header").text
    title = title.replace('  ', '')
    title = title.replace('\n', ' ')
  except:
    title = "No title"
  try:
    description = div.find("p", class_="csol-full-width-cta-card-description").text
    description = description.replace('  ', '')
    description = description.replace('\n', ' ')
    description = description.replace('. ', '.')
  except:
    description = "No description"
  try:
    url = div.find("a", class_="cl-button")["href"]
    url = url.split('?si')[0] if '?si' in url else url
    url = url.split('?si')[0] if '?si' in url else url
    url = url.split('&hubs')[0] if '&hubs' in url else url
  except:
    url = "NA"
  
  idea = {
    "Title": title,
    "Description": description,
    "URL": url
  }
  
  ideas[f"Idea {i+1}"] = idea

print(ideas)

# Your existing code...

# Convert the dictionary to a DataFrame
df = pd.DataFrame.from_dict(ideas, orient='index')

# Save the DataFrame to a CSV file
df.to_csv('business_ideas.csv', index_label='Ideas')

