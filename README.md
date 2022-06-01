# Build@Mercari Training Program 2022 ([Ja](https://mercan.mercari.com/articles/33259/))

### Training Tasks 

(details on branch: main)
- [x] **STEP1** Git ([JA](document/step1.ja.md)/[EN](document/step1.en.md))
- [x] **STEP2** Setup environment ([JA](document/step2.ja.md)
  /[EN](document/step2.en.md))
- [x] **STEP3** Develop API ([JA](document/step3.ja.md)
  /[EN](document/step3.en.md))
- [x] **STEP4** Docker ([JA](document/step4.ja.md)/[EN](document/step4.en.md))
- [x] **STEP5** (Stretch) Frontend ([JA](document/step5.ja.md)
  /[EN](document/step5.en.md))
- [x] **STEP6** (Stretch)  Run on docker-compose ([JA](document/step6.ja.md)
  /[EN](document/step6.en.md))
	

# Hackweek 5/23-5/31
 
**Theme**:[　Mercari](https://www.mercari.com/)'s new listing feature

**Our app**: AI Checker - Assessment of product condition using image analysis -



## Presentation slides and details 
[Google Slides in English and Japanese](https://docs.google.com/presentation/d/12a401t-DC8ZXhVuus-8bgVfyw_2gj0nC/edit?usp=sharing&ouid=117876754317720359991&rtpof=true&sd=true)
  
  
  
	
## DEMO VIDEO

[Youtube　Video(might be deleted soon)](https://youtu.be/Gzsw_WLsBCM)


https://user-images.githubusercontent.com/30760730/171305684-cac0b528-c5b3-42cb-907b-39c956ca7fae.mp4

	
	
	
## How to run

after cloning repo, you may want to install dependencies in requriement.txt 
	
1. Open terminal
	
	```
	cd python
	uvicorn main:app --reload --port 9000
	```
	
2. On the other terminal
	
	```
	cd typescript/simple-mercari-web
	```
	
	* install node dependencies([JA](document/step5.ja.md))
	
	```
	npm ci 
	```
	
	* run
	```
	npm start
	```
	
3. Open http://localhost:3000/



## Branch運用


	  main—------(念の為おいておく)
				|- HackWeek (デモ用)
					|- frontend(typescript用) :森本さん
					|- Backend:大村さん　(以前の評価関数)
					|- Unit Tests : 中川
					|- checker (以前のDB) :中川
					|- newDB (最新):中川
						|_newOpenCV(新しい評価関数)：中川
---

(23日時点フロントエンド)

<img width="1334" alt="Screen Shot 0004-05-23 at 17 00 44" src="https://user-images.githubusercontent.com/30760730/169860383-c2940bc9-a7b1-4fc2-8354-8ab2048249ba.png">


## 注意⚠️
  
- ブランチは近日中に整理します
