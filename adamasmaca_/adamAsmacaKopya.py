# Problem Seti 2, adamAsmaca.py
# Ä°sim:
# Ortak Ã§alÄ±Åanlar:
# Harcanan zaman:

# Adam Asmaca Oyunu
#------------------------------------
# YardÄ±mcÄ± kod
# Bu yardÄ±mcÄ± kodu anlamanÄ±za gerek yok,
# ama fonksiyonlarÄ± nasÄ±l kullanacaÄÄ±nÄ± bilmeniz gerekecek
# (dÃ¶kÃ¼manlarÄ± okuduÄunuzdan emin olun!)
import random
import string

WORDLIST_FILENAME = "kelimeler.txt"


def load_words():
    
    print("Dosyadan kelime listesi yükleniyor...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "kelimeler yüklendi.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): kelime listesi(strings)
    
    Kelime listesinden rastgele bir kelime dÃ¶ndÃ¼rÃ¼r
    """
    return random.choice(wordlist)

# yardÄ±mcÄ± kodun sonu

#------------------------------------

# Programdaki herhangi bir yerden eriÅilebilmesi iÃ§in
# kelime listesini deÄiÅken kelime listesine yÃ¼kleyin
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, kullanÄ±cÄ±nÄ±n tahmin ettiÄi kelime;
    tÃ¼m harflerin kÃ¼Ã§Ã¼k olduÄunu varsayar
    letter_guessed: Åimdiye kadar hangi harflerin tahmin edildiÄi (harflerin listesi);
     tÃ¼m harflerin kÃ¼Ã§Ã¼k olduÄunu varsayar
     returns: boolean, secret_word'Ã¼n tÃ¼m harfleri letter_guessed iÃ§indeyse True;
     Aksi takdirde yanlÄ±Å
    '''
    for letter in secret_word:
        if letter not in letters_guessed:
            return False
        else:
            return True
# BURAYA KODUNUZU GÄ°RÄ°N VE "pass"Ä± SÄ°LÄ°N
    



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, kullanÄ±cÄ±nÄ±n tahmin ettiÄi kelime
    letter_guessed: Åimdiye kadar hangi harflerin tahmin edildiÄi (harflerin listesi)
    returns: harflerden, alt Ã§izgilerden (_) ve Åu ana kadar secret_word
     iÃ§indeki hangi harflerin tahmin edildiÄini gÃ¶steren boÅluklardan oluÅan dize.
    '''
    guessed_word= ""
    for letter in secret_word:
        if letter in letters_guessed:
            guessed_word += letter
        else:
            guessed_word+="-"
    return guessed_word       
# BURAYA KODUNUZU GÄ°RÄ°N VE "pass"Ä± SÄ°LÄ°N
   



def get_available_letters(letters_guessed):
    '''
    letter_guessed: Åimdiye kadar hangi harflerin tahmin edildiÄi (harflerin listesi)
    returns: dize (harfler), hangi harflerin henÃ¼z tahmin edilmediÄini temsil eden harflerden oluÅur.
    '''
    avaliable_letters=""
    for letter in string.ascii_lowercase:
        if letter not in letters_guessed:
            avaliable_letters += letter
    return avaliable_letters  
# BURAYA KODUNUZU GÄ°RÄ°N VE "pass"Ä± SÄ°LÄ°N
    
    

def adamAsmaca(secret_word):
    '''
    secret_word: string, tahmin edilecek gizli kelime.
    
     EtkileÅimli bir Adam Asmaca oyununu baÅlatÄ±r.
    
     * Oyunun baÅÄ±nda, kullanÄ±cÄ±ya secret_word'Ã¼n kaÃ§ harf iÃ§erdiÄini
        ve kaÃ§ tahminle baÅladÄ±ÄÄ±nÄ± bildirin.
      
     * KullanÄ±cÄ± 6 tahminle baÅlamalÄ±dÄ±r

     * Her turdan Ã¶nce kullanÄ±cÄ±ya kaÃ§ tahmin kaldÄ±ÄÄ±nÄ± ve
        kullanÄ±cÄ±nÄ±n henÃ¼z tahmin etmediÄi harfleri gÃ¶stermelisiniz.
    
     * KullanÄ±cÄ±dan tur baÅÄ±na bir tahmin vermesini isteyin.
        KullanÄ±cÄ±nÄ±n bir mektup yazdÄ±ÄÄ±ndan emin olmayÄ± unutmayÄ±n!
    
     * KullanÄ±cÄ±, her tahminden hemen sonra tahminlerinin bilgisayarÄ±n
        kelimesinde gÃ¶rÃ¼nÃ¼p gÃ¶rÃ¼nmediÄi hakkÄ±nda geri bildirim almalÄ±dÄ±r.

     * Her tahminden sonra, o ana kadar kÄ±smen tahmin edilen kelimeyi
         kullanÄ±cÄ±ya gÃ¶stermelisiniz.
    
     Problem yazÄ±mÄ±nda detaylandÄ±rÄ±lan diÄer sÄ±nÄ±rlamalarÄ± takip eder.
    '''
    print("Adam asmaca oyununa hos geldiniz!!")
    print(f"{len(secret_word)} harfli bir kelime düşündüm.")
    print("Unutma, sadece 6 hakkın var!")
    print("-----------------------------")


    guesses=6
    letters_guessed= []
    available_letters="abcdefghijklmnoprstuvwxyz"
    Warning=3

    while True:
        print("Geriye kalan tahmin sayınız:",guesses)
        print("Kullanabileceğin harfler:",available_letters)


        letter=input("Lütfen bir harf tahmin et:").lower()
        if not letter.isalpha():
            Warning -=1
            print("Harf girmelisiniz!")
            print("Uyarı hakkınız:",Warning)
            
        elif letter in letters_guessed:
             Warning-=1
             print("Bu harfi daha önce girdiniz.Başka bir harf deneyin. Uyarı hakkınız:", Warning)
        else:
             letters_guessed.append(letter)
             if letter in secret_word:
                 print("Güzel tahmin!")
             else:
                 if letter in "aeiou":
                     guesses -=2
                 else:
                     guesses-=1

                 print("Bu harf benim kelimemde yok!!")

        if Warning==0:
             guesses-=1
             print("Dikkatli ol! Uyarı hakkınız bitti ve bir sonraki uyarınızda tahmin hakkınızdan 1 azaltılacak.")
             Warning=3
        if guesses==0:
             print("tahmin hakkınız bitti.KAYBETTİNİZ!")
             break


        available_letters=get_available_letters(letters_guessed)
        current_word= get_guessed_word(secret_word, letters_guessed)
        print(f"Kelime: {current_word}")
        print("----------------------------")

        if current_word==secret_word:
             print("Tebrikler,kazandınız!!")
             puan=guesses*len(letters_guessed)
             print("Toplam puanınız:",puan)
             return

        print("Üzgünüm, kaybettin!")
        print("Gizli kelime:",secret_word)            


    secret_word=random.choice(wordlist)
    adamAsmaca(secret_word)                     

# BURAYA KODUNUZU GÄ°RÄ°N VE "pass"Ä± SÄ°LÄ°N
    



# Adam asmaca iÅlevinizi tamamladÄ±ÄÄ±nÄ±zda, dosyanÄ±n
#en altÄ±na gidin ve test edilecek ilk iki satÄ±rÄ±n yorumunu kaldÄ±rÄ±n
# (ipucu: kendi testinizi yaparken kendi secret_word'Ã¼nÃ¼zÃ¼
# seÃ§mek isteyebilirsiniz)

# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: _ karakterli dize, gizli kelimenin geÃ§erli tahmini
    other_word: string, normal Ä°ngilizce kelime
    returns: boolean, True, eÄer my_word'Ã¼n tÃ¼m gerÃ§ek harfleri other_word'Ã¼n karÅÄ±lÄ±k gelen harfleriyle eÅleÅiyorsa veya harf Ã¶zel sembol _ ise ve my_word ile other_word aynÄ± uzunluktaysa; Aksi takdirde False:
    '''
# BURAYA KODUNUZU GÄ°RÄ°N VE "pass"Ä± SÄ°LÄ°N
    



def show_possible_matches(my_word):
    '''
    my_word: _ karakterli dize, gizli kelimenin geÃ§erli tahmini
    returns: hiÃ§bir Åey, ancak kelime listesindeki my_word ile eÅleÅen
        her kelimeyi yazdÄ±rmalÄ±dÄ±r.
    adamAsmaca ile bir harf tahmin edildiÄinde, o harfin gizli kelimede
        geÃ§tiÄi tÃ¼m pozisyonlarÄ±n ortaya Ã§Ä±ktÄ±ÄÄ±nÄ± unutmayÄ±n.
    Bu nedenle, gizli harf(_ ) zaten ortaya Ã§Ä±kmÄ±Å olan kelimedeki
     harflerden biri olamaz.
    '''
# BURAYA KODUNUZU GÄ°RÄ°N VE "pass"Ä± SÄ°LÄ°N
    



def adamAsmaca_ipuclu(secret_word):
    '''
    secret_word: string, tahmin edilecek gizli kelime.
    
     EtkileÅimli bir Adam Asmaca oyunu baÅlatÄ±r.
    
     * Oyunun baÅÄ±nda, kullanÄ±cÄ±ya secret_word'Ã¼n kaÃ§ harf iÃ§erdiÄini ve
        kaÃ§ tahminle baÅladÄ±ÄÄ±nÄ± bildirin.
      
     * KullanÄ±cÄ± 6 tahminle baÅlamalÄ±dÄ±r
    
     * Her turdan Ã¶nce kullanÄ±cÄ±ya kaÃ§ tahmin kaldÄ±ÄÄ±nÄ± ve kullanÄ±cÄ±nÄ±n
        henÃ¼z tahmin etmediÄi harfleri gÃ¶stermelisiniz.
    
     * KullanÄ±cÄ±dan tur baÅÄ±na bir tahmin vermesini isteyin.
        KullanÄ±cÄ±nÄ±n bir harf tahmin ettiÄini kontrol ettiÄinizden emin olun.
      
     * KullanÄ±cÄ±, her tahminden hemen sonra tahminlerinin bilgisayarÄ±n
        kelimesinde gÃ¶rÃ¼nÃ¼p gÃ¶rÃ¼nmediÄi hakkÄ±nda geri bildirim almalÄ±dÄ±r.

     * Her tahminden sonra, o ana kadar kÄ±smen tahmin edilen kelimeyi
         kullanÄ±cÄ±ya gÃ¶stermelisiniz.
      
     * Tahmin sembolÃ¼ * ise, kelime listesindeki mevcut tahmin edilen
        kelimeyle eÅleÅen tÃ¼m kelimeleri yazdÄ±rÄ±n.
    
     Problem yazÄ±mÄ±nda detaylandÄ±rÄ±lan diÄer sÄ±nÄ±rlamalarÄ± takip eder.
    '''
# BURAYA KODUNUZU GÄ°RÄ°N VE "pass"Ä± SÄ°LÄ°N
    



# adamAsmaca_ipuclu iÅlevinizi tamamladÄ±ÄÄ±nÄ±zda, yukarÄ±daki adam asmaca
# fonksiyonunu Ã§alÄ±ÅtÄ±rmak iÃ§in kullanÄ±lan benzer iki satÄ±rÄ± yorumlayÄ±n ve
# ardÄ±ndan bu iki satÄ±rÄ±n yorumunu kaldÄ±rÄ±n ve test etmek iÃ§in bu dosyayÄ± Ã§alÄ±ÅtÄ±rÄ±n!
# Ä°pucu: Test ederken kendi secret_word'Ã¼nÃ¼zÃ¼ seÃ§mek isteyebilirsiniz.


if __name__ == "__main__":
    

    # 2. bÃ¶lÃ¼mÃ¼ test etmek iÃ§in yukarÄ±daki pass satÄ±rÄ±nda # iÅaretini kullanÄ±n ve aÅaÄÄ±daki iki satÄ±rda # iÅaretini silin
    
    secret_word = choose_word(wordlist)
    adamAsmaca(secret_word)

###############
    
# 3. bÃ¶lÃ¼mÃ¼ test etmek iÃ§in yukarÄ±daki satÄ±rlarlarda yeniden # iÅaretini kullanÄ±n ve aÅaÄÄ±daki iki satÄ±rda # iÅaretini silin

    #secret_word = choose_word(wordlist)
    #adamAsmaca_ipuclu(secret_word)
