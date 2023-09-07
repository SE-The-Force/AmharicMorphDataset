import os
from bs4 import BeautifulSoup, NavigableString

def extract_words_from_html(file_path):
    # content html example:
    #
    #<div class="textBody" id="textBody">
    #<h3>ምዕራፍ 1 </h3>
    #<!--... the Word of God:--><span class="dimver">
    #</span>
    #<p><!--span class="verse" id="1">1  </span-->በመጀመሪያ እግዚአብሔር ሰማይንና ምድርን ፈጠረ።
    #<p><!--span class="verse" id="2">2  </span-->በመጀመሪያ እግዚአብሔር ሰማይንና ምድርን ፈጠረ።
    #<p><!--span class="verse" id="3">3  </span-->በመጀመሪያ እግዚአብሔር ሰማይንና ምድርን ፈጠረ።
    #<!-- more content -->
    #</div>
    # extract the amharic sentence from the html file
    with open(file_path, 'r',encoding="utf-8") as f:
        html_doc = f.read()
        soup = BeautifulSoup(html_doc, 'html.parser')
        text_body = soup.find('div', attrs={'class': 'textBody'})
        if not text_body:
            return []
        
        verses = text_body.find_all('p')
        words = []
        for verse in verses:
            verse_text = verse.get_text()
            words.extend(verse_text.split())
        return words


def main(directory):
    all_words = []
    
    # Loop through all subfolders and their files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.htm'):
                file_path = os.path.join(root, file)
                words = extract_words_from_html(file_path)
                all_words.extend(words)
                
    # Remove duplicates
    unique_words = list(set(all_words))

    # Write the unique words to a .txt file
    with open('words_list.txt', 'w', encoding='utf-8') as f:
        for word in unique_words:
            f.write(word + '\n')
    return unique_words

if __name__ == "__main__":
    directory_path = "./am_new"  # Replace with the path to your main folder
    result = main(directory_path)
    

