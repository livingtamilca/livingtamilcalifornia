import os, urllib.parse
os.chdir(os.path.expanduser('~/mnt/workspace/livingtamil-website'))
YT="https://www.youtube.com/watch?v="
def q(s): return "https://www.google.com/search?q="+urllib.parse.quote(s)
WIKI={"The Killers":"https://en.wikipedia.org/wiki/The_Killers_(Hemingway_short_story)",
 "The Snows of Kilimanjaro":"https://en.wikipedia.org/wiki/The_Snows_of_Kilimanjaro_(short_story)",
 "Hills Like White Elephants":"https://en.wikipedia.org/wiki/Hills_Like_White_Elephants",
 "A Clean, Well-Lighted Place":"https://en.wikipedia.org/wiki/A_Clean,_Well-Lighted_Place",
 "War and Peace":"https://en.wikipedia.org/wiki/War_and_Peace"}
# (id, kind, title, author, speaker)  kind: intro|story|talk
S=[
("November 2026","ஜெயகாந்தன்","Jayakanthan",[
 ("6UFeDquYoKQ","intro","Introducing Jayakanthan","Jayakanthan","Padmanabha"),
 ("b5Qjfm0k40k","story","Gurupeedam · குருபீடம்","Jayakanthan","Ilango"),
 ("2n_4kHf6VMI","story","Mun Nilavum Pin Paniyum · முன் நிலவும் பின் பனியும்","Jayakanthan","Swetha"),
 ("7cJ5ZLNeT3Y","story","Naan Enna Seyyattum Sollungo · நான் என்ன செய்யட்டும் சொல்லுங்கோ","Jayakanthan","Jyothsna"),
 ("Y4TDRmN-gcU","story","Agnipravesam · அக்னிப்பிரவேசம்","Jayakanthan","Narayanan")]),
("October 2026","சுஜாதா","Sujatha",[
 ("n2ZYnX0-504","intro","Introducing Sujatha","Sujatha","RV"),
 ("kU9OOGHgdGo","story","Maanju · மாஞ்சு","Sujatha","Sarathy"),
 ("eltqshqBaZo","story","Kuthirai · குதிரை","Sujatha","Sudha"),
 ("JQlXT2M4S_Y","story","Nagaram · நகரம்","Sujatha","Ravi"),
 ("w2CPVMd3HJQ","story","Oru Uthama Dinam · ஒரு உத்தம தினம்","Sujatha","Visu")]),
("August 2026","எர்னஸ்ட் ஹெமிங்வே","Ernest Hemingway · World literature",[
 ("d4K0Qt8WXs8","intro","Introducing Ernest Hemingway","Ernest Hemingway","Mani"),
 ("-WCQc-DkMxs","story","A Clean, Well-Lighted Place","Ernest Hemingway","Vijay"),
 ("Cd6k97py82w","story","Hills Like White Elephants","Ernest Hemingway","Sathya"),
 ("d3Lh9rftVUc","story","The Snows of Kilimanjaro","Ernest Hemingway","Sarathy"),
 ("b-JzYfBRDCM","story","The Killers","Ernest Hemingway","Pratap")]),
("June 2026","இந்திரா பார்த்தசாரதி · கிருஷ்ணன் நம்பி","Indira Parthasarathy & Krishnan Nambi",[
 ("KDJuiSNOMiQ","intro","Introducing Krishnan Nambi & Indira Parthasarathy","Krishnan Nambi & Indira Parthasarathy","Sharada"),
 ("hqdU44oi7sE","story","Oru Cup Coffee · ஒரு கப் காப்பி","Indira Parthasarathy","Balakumar"),
 ("bBaHlMB9zUE","story","Tholaivu · தொலைவு","Indira Parthasarathy","Prasad"),
 ("jiUuZ41KqGA","story","Thanga Oru · தங்க ஒரு","Krishnan Nambi","Mani"),
 ("joMIF68cmMM","story","Marumagal Vaakku · மருமகள் வாக்கு","Krishnan Nambi","Prathap")]),
("May 2026","ம. நவீன்","Ma. Navin · with the author",[
 ("IGNYa3xR8Fc","intro","Ma. Navin's literary world","Ma. Navin","Sarathy"),
 ("MxiSAb4iPoQ","story","Boyak · போயாக்","Ma. Navin","Bansi"),
 ("kEkPm9H2QpA","story","Vembadiyan · வேம்படியான்","Ma. Navin","Arutselvan")]),
("March 2026","சமகாலச் சிறுகதைகள்","Contemporary Tamil stories",[
 ("d_eCFVu_zjA","story","Kaagalam · காகளம்","Senthil Jagannathan","Balajee"),
 ("1pt_l6nOdvs","story","Kullan Binu · குள்ளன் பினு","Samraj","Ravi"),
 ("GLVu322J2fU","story","Vilasam · விலாசம்","Thiruchendazhai","Visu")]),
("Early 2026","நவீனச் சிறுகதைகள்","Modern Tamil short stories",[
 ("jQ5MNKS3-xQ","story","சொல்ல முடிந்தது","Su. Venugopal","Bansi"),
 ("w3qpB-nepWY","story","அறையில் புகுந்த தனிமை","Chandra Thangaraj","RV"),
 ("mlmFKAc_hBE","story","வைரம்","Ma. Navin","Prasad"),
 ("anRhymUzvXU","story","அம்புப்படுக்கை","Sunil Krishnan","Padmanabha"),
 ("tqT4k2qitC0","story","ஒரு பழைய கிழவரும் ஒரு புதிய உலகமும்","Aadhavan","Guhan"),
 ("-X5uXz1l_cM","story","முதலில் இரவு வரும்","Aadhavan","Ragul"),
 ("2MzmVH4tIyk","story","டெரிலின் ஷர்ட்டும் எட்டு முழ வேட்டி அணிந்த மனிதரும்","G. Nagarajan","Aingaran"),
 ("as9oCdRMf2k","story","யாரோ முட்டாள் சொன்ன கதை","G. Nagarajan","Sarathy"),
 ("Sg_Me4X7G6M","story","இரணிய வதம்","Sa. Kandasamy","Pandu"),
 ("pmyXGHMtwEM","story","தக்கையின் மீது நான்கு கண்கள்","Sa. Kandasamy","Mani"),
 ("AslLo16ZN_s","story","நீலம்","Pramil","Sudarshan")]),
("2025","தமிழ்ச் சிறுகதையின் முன்னோடிகள்","Masters of the Tamil short story",[
 ("euG8YVefQOY","story","கபாடபுரம்","Puthumaipithan",""),
 ("OvqhaJRmAEA","story","சாப விமோசனம்","Puthumaipithan",""),
 ("hjnmQH2kFVE","intro","எழுத்தாளர் ந. பிச்சமூர்த்தி – அறிமுகம்","Na. Pichamurthy",""),
 ("hQyZFekU9oE","story","அடகு","Na. Pichamurthy",""),
 ("frni5ssflYg","story","ஒருநாள்","Na. Pichamurthy",""),
 ("4kqPX_nhf0Y","story","ஞானப்பால்","Na. Pichamurthy",""),
 ("ERyH3uULU0s","story","விடியுமா","Ku. Pa. Ra",""),
 ("RCzHtbUAaKI","story","சிறிது வெளிச்சம்","Ku. Pa. Ra",""),
 ("xhE2KDY9vs8","story","ஆற்றாமை","Ku. Pa. Ra",""),
 ("2gqJ_OLuYTw","story","பிரபஞ்ச கானம்","Mouni",""),
 ("jDgKcY3bEPQ","story","அழியாச்சுடர்","Mouni",""),
 ("v_UBzZwKoCE","story","மாறுதல்","Mouni",""),
 ("sTA6JxRfA-o","intro","எழுத்தாளர் லா.ச.ரா – அறிமுகம்","La. Sa. Ra",""),
 ("PHTopc8Iwrw","story","ஜனனி","La. Sa. Ra",""),
 ("bKp4odHq4JE","story","புற்று","La. Sa. Ra",""),
 ("n1Jl5AoPDfk","story","பாற்கடல்","La. Sa. Ra",""),
 ("C21z90Pzx5s","story","பச்சைக்கனவு","La. Sa. Ra",""),
 ("9iGyonCR-uE","story","அன்பளிப்பு","Ku. Alagirisamy",""),
 ("HmerlWfWaes","story","அழகம்மாள்","Ku. Alagirisamy",""),
 ("Lc7ZfBUpncQ","story","ராஜா வந்திருக்கிறார்","Ku. Alagirisamy",""),
 ("BnSnDx6zVTU","story","இருவர் கண்ட ஒரே கனவு","Ku. Alagirisamy",""),
 ("flD-ti4u4_8","intro","எழுத்தாளர் தி. ஜானகிராமன் – அறிமுகம்","Thi. Janakiraman",""),
 ("ZhjRmlxzfrg","story","தீர்மானம்","Thi. Janakiraman",""),
 ("j9157Nyw1GQ","story","பரதேசி வந்தான்","Thi. Janakiraman",""),
 ("nCUYTrJcch0","story","பாயசம்","Thi. Janakiraman",""),
 ("qO76t3IonK8","story","சிலிர்ப்பு","Thi. Janakiraman",""),
 ("zH1nq0-DVv0","intro","எழுத்தாளர் கி.ரா – அறிமுகம்","Ki. Ra",""),
 ("mjobU3B9r40","story","நாற்காலி","Ki. Ra",""),
 ("a2PTHhGmoUs","story","கன்னிமை","Ki. Ra",""),
 ("UhW2ZnjecLc","story","பேதை","Ki. Ra",""),
 ("CCvAPeBQu04","story","நிலைநிறுத்தல்","Ki. Ra",""),
 ("mwozx5QmAMk","intro","எழுத்தாளர் சுந்தர ராமசாமி – அறிமுகம்","Sundara Ramaswamy",""),
 ("fa0BCt15Bto","story","பல்லக்கு தூக்கிகள்","Sundara Ramaswamy",""),
 ("aLfq603z8dc","story","வாழ்வும் வசந்தமும்","Sundara Ramaswamy",""),
 ("EcEIOaVupRw","story","பிரசாதம்","Sundara Ramaswamy",""),
 ("8HvlgUhZV6Y","story","ஜன்னல்","Sundara Ramaswamy",""),
 ("69l1vaIALzI","intro","எழுத்தாளர் அசோகமித்திரன் – அறிமுகம்","Ashokamitran",""),
 ("iDr8UPFfzpM","story","காந்தி","Ashokamitran",""),
 ("heOKjJQARu8","story","ஐநூறு கோப்பை தட்டுக்கள்","Ashokamitran",""),
 ("Ll_mtIXTfkE","story","நகல்","Ashokamitran","")]),
("2025","உலக இலக்கியம்","World literature · Leo Tolstoy",[
 ("aA_d8iLHkmA","story","War and Peace · போரும் அமைதியும் – Part 1","Leo Tolstoy",""),
 ("TaziQgin1-U","story","War and Peace · போரும் அமைதியும் – Part 2","Leo Tolstoy",""),
 ("pillT4miQcA","story","War and Peace · போரும் அமைதியும் – Part 3","Leo Tolstoy",""),
 ("YvZPn0XzWzM","story","War and Peace · போரும் அமைதியும் – Part 4","Leo Tolstoy","")]),
]
FREE={"Puthumaipithan","Ku. Pa. Ra","Na. Pichamurthy","Ku. Alagirisamy","Jayakanthan"}
TA={"Jayakanthan":"ஜெயகாந்தன்","Sujatha":"சுஜாதா","Ernest Hemingway":"Ernest Hemingway","Indira Parthasarathy":"இந்திரா பார்த்தசாரதி","Krishnan Nambi":"கிருஷ்ணன் நம்பி","Ma. Navin":"ம. நவீன்","Senthil Jagannathan":"செந்தில் ஜெகன்நாதன்","Samraj":"சாம்ராஜ்","Thiruchendazhai":"திருச்செந்தாழை","Su. Venugopal":"சு. வேணுகோபால்","Chandra Thangaraj":"சந்திரா தங்கராஜ்","Sunil Krishnan":"சுனில் கிருஷ்ணன்","Aadhavan":"ஆதவன்","G. Nagarajan":"ஜி. நாகராஜன்","Sa. Kandasamy":"சா. கந்தசாமி","Pramil":"பிரமிள்","Puthumaipithan":"புதுமைப்பித்தன்","Na. Pichamurthy":"ந. பிச்சமூர்த்தி","Ku. Pa. Ra":"கு. ப. ராஜகோபாலன்","Mouni":"மௌனி","La. Sa. Ra":"லா. ச. ராமாமிர்தம்","Ku. Alagirisamy":"கு. அழகிரிசாமி","Thi. Janakiraman":"தி. ஜானகிராமன்","Ki. Ra":"கி. ராஜநாராயணன்","Sundara Ramaswamy":"சுந்தர ராமசாமி","Ashokamitran":"அசோகமித்திரன்","Jeyamohan":"ஜெயமோகன்","Leo Tolstoy":"Leo Tolstoy"}
EXTRA={"விடியுமா":("https://elevenreader.io/audiobooks/vidiyumaa-audiobook/GyP8a6gqz1YcviZi5XYm","Listen (audiobook)")}
def ws(t): return "https://ta.wikisource.org/w/index.php?search="+urllib.parse.quote(t)
def card(v):
    vid,kind,title,author,spk=v
    base=title.split(" · ")[0].split(" – Part")[0]
    ta_title=title.split(' · ')[-1]
    if base in WIKI: textlink, lab = WIKI[base], "Read about it"
    elif kind=="story" and author in FREE: textlink, lab = ws(ta_title), "Free text (Wikisource)"
    elif kind=="story": textlink, lab = q(f"{ta_title} {TA.get(author,author)} சிறுகதை"), "Find the text"
    else: textlink, lab = "", ""
    tag={"intro":"Introduction","talk":"Talk","story":"Story"}[kind]
    if "War and Peace" in title: tag="Novel"
    by=f'<span class="r-spk">Presented by {spk}</span>' if spk else ''
    links=f'<a href="{YT}{vid}" target="_blank" rel="noopener">▶ Watch</a>'
    if textlink: links+=f' <a href="{textlink}" target="_blank" rel="noopener">{lab} ↗</a>'
    if ta_title in EXTRA: links+=f' <a href="{EXTRA[ta_title][0]}" target="_blank" rel="noopener">{EXTRA[ta_title][1]} ↗</a>'
    return f'''<li class="r-item r-{kind}">
            <a class="r-thumb" href="{YT}{vid}" target="_blank" rel="noopener"><img src="https://i.ytimg.com/vi/{vid}/mqdefault.jpg" alt="" loading="lazy"><span class="r-tag">{tag}</span></a>
            <div class="r-body"><h4>{title}</h4><p class="r-author">{author}</p>{by}<p class="r-links">{links}</p></div>
          </li>'''
WIKIW={"Puthumaipithan": ["https://tamil.wiki/wiki/%E0%AE%AA%E0%AF%81%E0%AE%A4%E0%AF%81%E0%AE%AE%E0%AF%88%E0%AE%AA%E0%AF%8D%E0%AE%AA%E0%AE%BF%E0%AE%A4%E0%AF%8D%E0%AE%A4%E0%AE%A9%E0%AF%8D", "https://tamil.wiki/images/b/b8/Pudhumaipithan.jpg", "புதுமைப்பித்தன்"], "Na. Pichamurthy": ["https://tamil.wiki/wiki/%E0%AE%A8._%E0%AE%AA%E0%AE%BF%E0%AE%9A%E0%AF%8D%E0%AE%9A%E0%AE%AE%E0%AF%82%E0%AE%B0%E0%AF%8D%E0%AE%A4%E0%AF%8D%E0%AE%A4%E0%AE%BF", "https://tamil.wiki/images/thumb/9/9c/Na_Pichamurthy.jpg/300px-Na_Pichamurthy.jpg", "ந. பிச்சமூர்த்தி"], "Ku. Pa. Ra": ["https://tamil.wiki/wiki/%E0%AE%95%E0%AF%81.%E0%AE%AA._%E0%AE%B0%E0%AE%BE%E0%AE%9C%E0%AE%95%E0%AF%8B%E0%AE%AA%E0%AE%BE%E0%AE%B2%E0%AE%A9%E0%AF%8D", "https://tamil.wiki/images/thumb/9/91/%E0%AE%95%E0%AF%81%E0%AE%AA%E0%AE%B0%E0%AE%BE.jpg/300px-%E0%AE%95%E0%AF%81%E0%AE%AA%E0%AE%B0%E0%AE%BE.jpg", "கு.ப.ரா"], "Mouni": ["https://tamil.wiki/wiki/%E0%AE%AE%E0%AF%8C%E0%AE%A9%E0%AE%BF", "https://tamil.wiki/images/8/82/%E0%AE%AE%E0%AF%8C%E0%AE%A9%E0%AE%BF.jpg", "மௌனி"], "La. Sa. Ra": ["https://tamil.wiki/wiki/%E0%AE%B2%E0%AE%BE.%E0%AE%9A._%E0%AE%B0%E0%AE%BE%E0%AE%AE%E0%AE%BE%E0%AE%AE%E0%AE%BF%E0%AE%B0%E0%AF%8D%E0%AE%A4%E0%AE%AE%E0%AF%8D", "https://tamil.wiki/images/8/84/La.Sa.Ra.jpg", "லா.ச.ரா"], "Ku. Alagirisamy": ["https://tamil.wiki/wiki/%E0%AE%95%E0%AF%81._%E0%AE%85%E0%AE%B4%E0%AE%95%E0%AE%BF%E0%AE%B0%E0%AE%BF%E0%AE%9A%E0%AE%BE%E0%AE%AE%E0%AE%BF", "https://tamil.wiki/images/thumb/9/93/%E0%AE%95%E0%AF%81.%E0%AE%85%E0%AE%B4%E0%AE%95%E0%AE%BF%E0%AE%B0%E0%AE%BF%E0%AE%9A%E0%AE%BE%E0%AE%AE%E0%AE%BF.png/300px-%E0%AE%95%E0%AF%81.%E0%AE%85%E0%AE%B4%E0%AE%95%E0%AE%BF%E0%AE%B0%E0%AE%BF%E0%AE%9A%E0%AE%BE%E0%AE%AE%E0%AE%BF.png", "கு. அழகிரிசாமி"], "Thi. Janakiraman": ["https://tamil.wiki/wiki/%E0%AE%A4%E0%AE%BF.%E0%AE%9C%E0%AE%BE%E0%AE%A9%E0%AE%95%E0%AE%BF%E0%AE%B0%E0%AE%BE%E0%AE%AE%E0%AE%A9%E0%AF%8D", "https://tamil.wiki/images/thumb/8/80/%E0%AE%A4%E0%AE%BF.%E0%AE%9C%E0%AE%BE%E0%AE%A9%E0%AE%95%E0%AE%BF%E0%AE%B0%E0%AE%BE%E0%AE%AE%E0%AE%A9%E0%AF%8D.png/281px-%E0%AE%A4%E0%AE%BF.%E0%AE%9C%E0%AE%BE%E0%AE%A9%E0%AE%95%E0%AE%BF%E0%AE%B0%E0%AE%BE%E0%AE%AE%E0%AE%A9%E0%AF%8D.png", "தி. ஜானகிராமன்"], "Ki. Ra": ["https://tamil.wiki/wiki/%E0%AE%95%E0%AE%BF._%E0%AE%B0%E0%AE%BE%E0%AE%9C%E0%AE%A8%E0%AE%BE%E0%AE%B0%E0%AE%BE%E0%AE%AF%E0%AE%A3%E0%AE%A9%E0%AF%8D", "https://tamil.wiki/images/thumb/b/bd/Ki.Ra2.jpg/300px-Ki.Ra2.jpg", "கி.ரா"], "Sundara Ramaswamy": ["https://tamil.wiki/wiki/%E0%AE%9A%E0%AF%81%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%B0_%E0%AE%B0%E0%AE%BE%E0%AE%AE%E0%AE%9A%E0%AE%BE%E0%AE%AE%E0%AE%BF", "https://tamil.wiki/images/8/85/Sunth.jpg", "சுந்தர ராமசாமி"], "Ashokamitran": ["https://tamil.wiki/wiki/%E0%AE%85%E0%AE%9A%E0%AF%8B%E0%AE%95%E0%AE%AE%E0%AE%BF%E0%AE%A4%E0%AF%8D%E0%AE%A4%E0%AE%BF%E0%AE%B0%E0%AE%A9%E0%AF%8D", "https://tamil.wiki/images/thumb/7/72/Asokamithranhero.jpeg/300px-Asokamithranhero.jpeg", "அசோகமித்திரன்"], "Jayakanthan": ["https://tamil.wiki/wiki/%E0%AE%9C%E0%AF%86%E0%AE%AF%E0%AE%95%E0%AE%BE%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%A9%E0%AF%8D", "https://tamil.wiki/images/thumb/2/24/Jeya1.jpg/300px-Jeya1.jpg", "ஜெயகாந்தன்"], "Sujatha": ["https://tamil.wiki/wiki/%E0%AE%9A%E0%AF%81%E0%AE%9C%E0%AE%BE%E0%AE%A4%E0%AE%BE", "https://tamil.wiki/images/thumb/a/a1/Sujatha.png/300px-Sujatha.png", "சுஜாதா"], "Indira Parthasarathy": ["https://tamil.wiki/wiki/%E0%AE%87%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%BF%E0%AE%B0%E0%AE%BE_%E0%AE%AA%E0%AE%BE%E0%AE%B0%E0%AF%8D%E0%AE%A4%E0%AF%8D%E0%AE%A4%E0%AE%9A%E0%AE%BE%E0%AE%B0%E0%AE%A4%E0%AE%BF", "https://tamil.wiki/images/9/98/%E0%AE%87%E0%AE%AA%E0%AE%BE.jpg", "இந்திரா பார்த்தசாரதி"], "Krishnan Nambi": ["https://tamil.wiki/wiki/%E0%AE%95%E0%AE%BF%E0%AE%B0%E0%AF%81%E0%AE%B7%E0%AF%8D%E0%AE%A3%E0%AE%A9%E0%AF%8D_%E0%AE%A8%E0%AE%AE%E0%AF%8D%E0%AE%AA%E0%AE%BF", "https://tamil.wiki/images/9/9b/%E0%AE%95%E0%AE%BF%E0%AE%B0%E0%AF%81%E0%AE%B7%E0%AF%8D%E0%AE%A3%E0%AE%A9%E0%AF%8D_%E0%AE%A8%E0%AE%AE%E0%AF%8D%E0%AE%AA%E0%AE%BF_.png", "கிருஷ்ணன் நம்பி"], "Aadhavan": ["https://tamil.wiki/wiki/%E0%AE%86%E0%AE%A4%E0%AE%B5%E0%AE%A9%E0%AF%8D_%28%E0%AE%8E%E0%AE%B4%E0%AF%81%E0%AE%A4%E0%AF%8D%E0%AE%A4%E0%AE%BE%E0%AE%B3%E0%AE%B0%E0%AF%8D%29", "https://tamil.wiki/images/thumb/7/79/%E0%AE%86%E0%AE%A4%E0%AE%B5%E0%AE%A9%E0%AF%8D1.jpg/300px-%E0%AE%86%E0%AE%A4%E0%AE%B5%E0%AE%A9%E0%AF%8D1.jpg", "ஆதவன்"], "G. Nagarajan": ["https://tamil.wiki/wiki/%E0%AE%9C%E0%AE%BF._%E0%AE%A8%E0%AE%BE%E0%AE%95%E0%AE%B0%E0%AE%BE%E0%AE%9C%E0%AE%A9%E0%AF%8D", "https://tamil.wiki/images/thumb/7/77/Gnagarajan2.jpg/300px-Gnagarajan2.jpg", "ஜி. நாகராஜன்"], "Sa. Kandasamy": ["https://tamil.wiki/wiki/%E0%AE%9A%E0%AE%BE.%E0%AE%95%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%9A%E0%AE%BE%E0%AE%AE%E0%AE%BF", "https://tamil.wiki/images/thumb/5/59/Sakanda.png/300px-Sakanda.png", "சா. கந்தசாமி"], "Pramil": ["https://tamil.wiki/wiki/%E0%AE%AA%E0%AE%BF%E0%AE%B0%E0%AE%AE%E0%AE%BF%E0%AE%B3%E0%AF%8D", "https://tamil.wiki/images/thumb/b/ba/%E0%AE%AA%E0%AE%BF%E0%AE%B0%E0%AE%AE%E0%AE%BF%E0%AE%B3%E0%AF%8D.jpg/300px-%E0%AE%AA%E0%AE%BF%E0%AE%B0%E0%AE%AE%E0%AE%BF%E0%AE%B3%E0%AF%8D.jpg", "பிரமிள்"], "Jeyamohan": ["https://tamil.wiki/wiki/%E0%AE%9C%E0%AF%86%E0%AE%AF%E0%AE%AE%E0%AF%8B%E0%AE%95%E0%AE%A9%E0%AF%8D", "https://tamil.wiki/images/thumb/f/f3/Jeyamohan_new3.jpg/300px-Jeyamohan_new3.jpg", "ஜெயமோகன்"], "Ma. Navin": ["https://tamil.wiki/wiki/%E0%AE%AE._%E0%AE%A8%E0%AE%B5%E0%AF%80%E0%AE%A9%E0%AF%8D", "https://tamil.wiki/images/thumb/6/6e/Naveen1.jpg/300px-Naveen1.jpg", "ம. நவீன்"], "Su. Venugopal": ["https://tamil.wiki/wiki/%E0%AE%9A%E0%AF%81._%E0%AE%B5%E0%AF%87%E0%AE%A3%E0%AF%81%E0%AE%95%E0%AF%8B%E0%AE%AA%E0%AE%BE%E0%AE%B2%E0%AF%8D", "https://tamil.wiki/images/thumb/2/28/Venugopal3.jpg/300px-Venugopal3.jpg", "சு. வேணுகோபால்"], "Chandra Thangaraj": ["https://tamil.wiki/wiki/%E0%AE%9A%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%BF%E0%AE%B0%E0%AE%BE_%E0%AE%A4%E0%AE%99%E0%AF%8D%E0%AE%95%E0%AE%B0%E0%AE%BE%E0%AE%9C%E0%AF%8D", "https://tamil.wiki/images/thumb/b/b9/Chandra2.jpg/300px-Chandra2.jpg", "சந்திரா தங்கராஜ்"], "Sunil Krishnan": ["https://tamil.wiki/wiki/%E0%AE%9A%E0%AF%81%E0%AE%A9%E0%AE%BF%E0%AE%B2%E0%AF%8D_%E0%AE%95%E0%AE%BF%E0%AE%B0%E0%AF%81%E0%AE%B7%E0%AF%8D%E0%AE%A3%E0%AE%A9%E0%AF%8D", "https://tamil.wiki/images/thumb/6/63/Suneel-krishanin-ambu-padukkai-muthal-mana-pathivugal_528.jpg/300px-Suneel-krishanin-ambu-padukkai-muthal-mana-pathivugal_528.jpg", "சுனில் கிருஷ்ணன்"], "Samraj": ["https://tamil.wiki/wiki/%E0%AE%9A%E0%AE%BE%E0%AE%AE%E0%AF%8D%E0%AE%B0%E0%AE%BE%E0%AE%9C%E0%AF%8D", "https://tamil.wiki/images/thumb/9/90/Samraj_%281%29.jpg/300px-Samraj_%281%29.jpg", "சாம்ராஜ்"], "Senthil Jagannathan": ["https://tamil.wiki/wiki/%E0%AE%9A%E0%AF%86%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%BF%E0%AE%B2%E0%AF%8D_%E0%AE%9C%E0%AF%86%E0%AE%95%E0%AE%A8%E0%AF%8D%E0%AE%A8%E0%AE%BE%E0%AE%A4%E0%AE%A9%E0%AF%8D", "https://tamil.wiki/images/8/8d/Senthil-217_%281%29.jpg", "செந்தில் ஜெகந்நாதன்"], "Thiruchendazhai": ["https://tamil.wiki/wiki/%E0%AE%AA%E0%AE%BE._%E0%AE%A4%E0%AE%BF%E0%AE%B0%E0%AF%81%E0%AE%9A%E0%AF%8D%E0%AE%9A%E0%AF%86%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%BE%E0%AE%B4%E0%AF%88", "https://tamil.wiki/images/thumb/1/1e/%E0%AE%AA%E0%AE%BE.%E0%AE%A4%E0%AE%BF%E0%AE%B0%E0%AF%81%E0%AE%9A%E0%AF%8D%E0%AE%9A%E0%AF%86%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%BE%E0%AE%B4%E0%AF%88.jpg/300px-%E0%AE%AA%E0%AE%BE.%E0%AE%A4%E0%AE%BF%E0%AE%B0%E0%AF%81%E0%AE%9A%E0%AF%8D%E0%AE%9A%E0%AF%86%E0%AE%A8%E0%AF%8D%E0%AE%A4%E0%AE%BE%E0%AE%B4%E0%AF%88.jpg", "பா. திருச்செந்தாழை"]}
def writers(vids):
    names=[]
    for v in vids:
        for a in v[3].split(" & "):
            if a not in names: names.append(a)
    out=[]
    for a in names:
        if a in WIKIW:
            url,pic,t=WIKIW[a]
            out.append(f'<a class="w-chip" href="{url}" target="_blank" rel="noopener"><img src="{pic}" alt="" loading="lazy">{t}</a>')
        else:
            out.append(f'<a class="w-chip" href="https://en.wikipedia.org/wiki/{a.replace(" ","_")}" target="_blank" rel="noopener">{a}</a>')
    return " ".join(out)
nstory=sum(1 for s in S for v in s[3] if v[1]=="story")
authors=sorted({v[3] for s in S for v in s[3]})
sessions="\n".join(f'''      <section class="r-session"><div class="wrap">
        <div class="r-head"><span class="r-when">{when}</span><div><p class="card-ta" lang="ta">{ta}</p><h2>{en}</h2></div></div>
        <p class="r-writers">About the writers: {writers(vids)}</p>
        <ul class="r-list">
          {"".join(card(v) for v in vids)}
        </ul>
      </div></section>''' for when,ta,en,vids in S)

TALKS=[("Zi7Zjj6iiKY","ஜெயமோகன்","Jeyamohan","புத்தக வாசிப்பு குழுக்கள்","On book reading circles: why reading together matters."),
       ("4RrqAq5f_2Q","ம. நவீன்","Ma. Navin","VLC Bay Area உரை","The Malaysian Tamil writer's address to VLC Bay Area, after our session on his stories.")]
talks_html="\n".join(f'''<li class="t-item">
            <a class="t-video" href="{YT}{vid}" target="_blank" rel="noopener"><img src="https://i.ytimg.com/vi/{vid}/hqdefault.jpg" alt="" loading="lazy"><span class="t-play">▶</span></a>
            <div class="t-body"><p class="t-name-ta" lang="ta">{ta}</p><h3>{en}</h3><p class="t-title" lang="ta">{title}</p><p class="muted">{blurb}</p>
            <p class="r-links"><a href="{YT}{vid}" target="_blank" rel="noopener">▶ Watch the talk</a></p></div>
          </li>''' for vid,ta,en,title,blurb in TALKS)
talks_section=f'''      <section class="r-talks"><div class="wrap">
        <p class="label" lang="ta">படைப்பாளிகளின் உரைகள்</p>
        <h2>Authors in Their Own Words</h2>
        <p class="muted">Talks given to our circle by the writers themselves.</p>
        <ul class="t-list">
          {talks_html}
        </ul>
      </div></section>'''
tpl=open('events.html',encoding='utf-8').read()
head=tpl[:tpl.index('<main id="main">')+len('<main id="main">')].replace('<title>Events ·','<title>Reading Archive ·').replace(' aria-current="page"','')
tail=tpl[tpl.index('</main>'):].replace('<script src="js/site.js"></script>','<script src="js/site.js"></script>\n  <script src="js/readings-live.js"></script>')
body=f'''
    <section class="page-head"><div class="wrap">
      <p class="label" lang="ta">நாங்கள் வாசித்தவை</p>
      <h1>Our Reading Archive</h1>
      <p class="lede">Every story, novel and writer we have taken up at The Literary Circle, with the recorded talks and discussions from our <a href="https://www.youtube.com/channel/UCCyEoEuhA17D2YzN9v149PA" target="_blank" rel="noopener">VLC Bay Area YouTube channel</a>.</p>
      <p class="r-stats"><span><b>{nstory}</b> stories &amp; novel parts</span><span><b>{len(set(authors)|{"Jeyamohan"})}</b> writers</span><span><b>{sum(len(s[3]) for s in S)+len(TALKS)}</b> recordings</span></p>
      <p class="muted small">The Literary Circle follows the same reading tradition as <a href="https://livingtamil.org" target="_blank" rel="noopener noreferrer">Living Tamil</a> in India: read closely, present, and discuss together.</p>
      <p class="muted small">Dates are approximate, based on when each recording was posted. Conversations are in Tamil.</p>
    </div></section>
{talks_section}
{sessions}
  '''
open('readings.html','w',encoding='utf-8').write(head+body+tail)
# link from events page
e=open('events.html',encoding='utf-8').read()
btn='<p><a class="btn btn-yt"'
if 'readings.html' not in e:
    e=e.replace(btn,'<p><a class="btn btn-ghost-light" href="readings.html">Browse our reading archive</a></p>\n        '+btn,1)
    open('events.html','w',encoding='utf-8').write(e)
c=open('css/style.css',encoding='utf-8').read()
if '.r-talks' not in c:
    c+='''
/* Authors' talks */
.r-talks { background: var(--navy); color: #e9e4d6; }
.r-talks h2 { color: #fff; } .r-talks .label { color: var(--gold); } .r-talks .muted { color: #bdb8aa; }
.t-list { list-style: none; padding: 0; margin: 1.5rem 0 0; display: grid; gap: 1.75rem; grid-template-columns: repeat(auto-fit, minmax(20rem, 1fr)); }
.t-item { background: var(--navy2); border-radius: var(--radius); overflow: hidden; box-shadow: 0 0 0 1px rgba(201,162,39,.4); }
.t-video { position: relative; display: block; aspect-ratio: 16/9; background: #000; }
.t-video img { width: 100%; height: 100%; object-fit: cover; opacity: .85; transition: opacity .3s; }
.t-video:hover img { opacity: 1; }
.t-play { position: absolute; inset: 0; margin: auto; width: 3.6rem; height: 3.6rem; border-radius: 50%; background: var(--gold); color: var(--navy); display: grid; place-items: center; font-size: 1.3rem; padding-left: .2rem; }
.t-body { padding: 1.1rem 1.25rem 1.3rem; }
.t-name-ta { font: 700 1rem var(--display); color: var(--gold); margin: 0; }
.t-body h3 { color: #fff; margin: .1rem 0 .35rem; }
.t-title { font: 600 1rem var(--display); color: #f4efe3; margin: 0 0 .4rem; }
.r-talks .r-links a { color: var(--gold); }
'''
if '.r-writers' not in c:
    c+='\n.r-writers { margin: -.75rem 0 1.25rem; font: 500 .85rem var(--label); color: var(--muted); }\n.r-writers a { color: var(--accent2); }\n'
if '.r-session' not in c:
    c+='''
/* Reading archive */
.r-stats { display: flex; gap: .75rem; flex-wrap: wrap; margin: 1.25rem 0 .5rem; }
.r-stats span { font: 500 .85rem var(--label); background: #fff; border: 1px solid var(--line); border-radius: 999px; padding: .4rem .9rem; color: var(--muted); }
.r-stats b { font: 700 1rem var(--display); color: var(--accent); margin-right: .2rem; }
.r-session { padding: 2.5rem 0; }
.r-head { display: flex; align-items: center; gap: 1.25rem; margin-bottom: 1.5rem; }
.r-when { flex: none; font: 600 .75rem var(--label); letter-spacing: .1em; text-transform: uppercase; color: var(--gold); background: var(--navy); border-radius: 999px; padding: .45rem .9rem; }
.r-head h2 { margin: 0; font-size: 1.4rem; }
.r-list { list-style: none; padding: 0; margin: 0; display: grid; gap: 1.25rem; grid-template-columns: repeat(auto-fill, minmax(15rem, 1fr)); }
.r-item { background: #fff; border: 1px solid var(--line); border-radius: var(--radius); overflow: hidden; display: flex; flex-direction: column; transition: transform .25s, box-shadow .25s; }
.r-item:hover { transform: translateY(-3px); box-shadow: 0 10px 24px rgba(6,12,38,.12); }
.r-intro, .r-talk { border-top: 3px solid var(--gold); }
.r-thumb { position: relative; display: block; aspect-ratio: 16/9; background: var(--navy2); }
.r-thumb img { width: 100%; height: 100%; object-fit: cover; }
.r-tag { position: absolute; left: .6rem; top: .6rem; font: 600 .68rem var(--label); letter-spacing: .08em; text-transform: uppercase; background: rgba(6,12,38,.85); color: var(--gold); padding: .2rem .55rem; border-radius: 999px; }
.r-body { padding: .9rem 1rem 1rem; display: flex; flex-direction: column; gap: .2rem; flex: 1; }
.r-body h4 { font: 700 1rem/1.45 var(--display); margin: 0; color: var(--ink); }
.r-author { margin: 0; font: 600 .85rem var(--label); color: var(--accent); }
.r-spk { font: 500 .8rem var(--label); color: var(--muted); }
.r-links { margin: auto 0 0; padding-top: .6rem; display: flex; gap: 1rem; font: 600 .8rem var(--label); }
.r-links a { text-decoration: none; }
.btn-ghost-light { background: transparent; color: var(--gold); border-color: var(--gold); }
'''
    open('css/style.css','w',encoding='utf-8').write(c)
print('stories',nstory,'authors',len(authors))
