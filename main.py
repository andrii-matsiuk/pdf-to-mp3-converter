from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path

def pdf_to_mp3(file_path='test.pdf', language='en'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        
        print(f'[+] Processing...')
        
        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]    
        text = ''.join(pages)
        with open('text1.txt', 'w') as file:
            file.write(text)
            
        text = text.replace('\n', '')
        with open('text2.txt', 'w') as file:
            file.write(text) 
            
        my_audio = gTTS(text=text, lang=language)
        file_name = Path(file_path).stem
        my_audio.save(f'{file_name}.mp3')
        
        return f'[+] {file_name}.mp3 saved successfully!\n---Have a good day!---'       
        # return 'File exist!'
    else:
        return 'File does not exist! Check file path'

def main():
    tprint('PDF>>TO>>MP3', font='bulhead')
    print(pdf_to_mp3())
          
if __name__ == '__main__':
    main()