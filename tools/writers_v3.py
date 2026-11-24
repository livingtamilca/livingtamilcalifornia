# -*- coding: utf-8 -*-
import os, glob, urllib.parse
os.chdir(os.path.expanduser('~/mnt/workspace/livingtamil-website'))
B="https://tamil.wiki"
# key (as used in the archive) : (Tamil Wiki title, display name, portrait path)
W={
"Puthumaipithan":("புதுமைப்பித்தன்","புதுமைப்பித்தன்","/images/b/b8/Pudhumaipithan.jpg"),
"Na. Pichamurthy":("ந. பிச்சமூர்த்தி","ந. பிச்சமூர்த்தி","/images/thumb/9/9c/Na_Pichamurthy.jpg/300px-Na_Pichamurthy.jpg"),
"Ku. Pa. Ra":("கு.ப. ராஜகோபாலன்","கு.ப.ரா","/images/thumb/9/91/குபரா.jpg/300px-குபரா.jpg"),
"Mouni":("மௌனி","மௌனி","/images/8/82/மௌனி.jpg"),
"La. Sa. Ra":("லா.ச. ராமாமிர்தம்","லா.ச.ரா","/images/8/84/La.Sa.Ra.jpg"),
"Ku. Alagirisamy":("கு. அழகிரிசாமி","கு. அழகிரிசாமி","/images/thumb/9/93/கு.அழகிரிசாமி.png/300px-கு.அழகிரிசாமி.png"),
"Thi. Janakiraman":("தி.ஜானகிராமன்","தி. ஜானகிராமன்","/images/thumb/8/80/தி.ஜானகிராமன்.png/281px-தி.ஜானகிராமன்.png"),
"Ki. Ra":("கி. ராஜநாராயணன்","கி.ரா","/images/thumb/b/bd/Ki.Ra2.jpg/300px-Ki.Ra2.jpg"),
"Sundara Ramaswamy":("சுந்தர ராமசாமி","சுந்தர ராமசாமி","/images/8/85/Sunth.jpg"),
"Ashokamitran":("அசோகமித்திரன்","அசோகமித்திரன்","/images/thumb/7/72/Asokamithranhero.jpeg/300px-Asokamithranhero.jpeg"),
"Jayakanthan":("ஜெயகாந்தன்","ஜெயகாந்தன்","/images/thumb/2/24/Jeya1.jpg/300px-Jeya1.jpg"),
"Sujatha":("சுஜாதா","சுஜாதா","/images/thumb/a/a1/Sujatha.png/300px-Sujatha.png"),
"Indira Parthasarathy":("இந்திரா பார்த்தசாரதி","இந்திரா பார்த்தசாரதி","/images/9/98/இபா.jpg"),
"Krishnan Nambi":("கிருஷ்ணன் நம்பி","கிருஷ்ணன் நம்பி","/images/9/9b/கிருஷ்ணன்_நம்பி_.png"),
"Aadhavan":("ஆதவன் (எழுத்தாளர்)","ஆதவன்","/images/thumb/7/79/ஆதவன்1.jpg/300px-ஆதவன்1.jpg"),
"G. Nagarajan":("ஜி. நாகராஜன்","ஜி. நாகராஜன்","/images/thumb/7/77/Gnagarajan2.jpg/300px-Gnagarajan2.jpg"),
"Sa. Kandasamy":("சா.கந்தசாமி","சா. கந்தசாமி","/images/thumb/5/59/Sakanda.png/300px-Sakanda.png"),
"Pramil":("பிரமிள்","பிரமிள்","/images/thumb/b/ba/பிரமிள்.jpg/300px-பிரமிள்.jpg"),
"Jeyamohan":("ஜெயமோகன்","ஜெயமோகன்","/images/thumb/f/f3/Jeyamohan_new3.jpg/300px-Jeyamohan_new3.jpg"),
"Ma. Navin":("ம. நவீன்","ம. நவீன்","/images/thumb/6/6e/Naveen1.jpg/300px-Naveen1.jpg"),
"Su. Venugopal":("சு. வேணுகோபால்","சு. வேணுகோபால்","/images/thumb/2/28/Venugopal3.jpg/300px-Venugopal3.jpg"),
"Chandra Thangaraj":("சந்திரா தங்கராஜ்","சந்திரா தங்கராஜ்","/images/thumb/b/b9/Chandra2.jpg/300px-Chandra2.jpg"),
"Sunil Krishnan":("சுனில் கிருஷ்ணன்","சுனில் கிருஷ்ணன்","/images/thumb/6/63/Suneel-krishanin-ambu-padukkai-muthal-mana-pathivugal_528.jpg/300px-Suneel-krishanin-ambu-padukkai-muthal-mana-pathivugal_528.jpg"),
"Samraj":("சாம்ராஜ்","சாம்ராஜ்","/images/thumb/9/90/Samraj_(1).jpg/300px-Samraj_(1).jpg"),
"Senthil Jagannathan":("செந்தில் ஜெகந்நாதன்","செந்தில் ஜெகந்நாதன்","/images/8/8d/Senthil-217_(1).jpg"),
"Thiruchendazhai":("பா. திருச்செந்தாழை","பா. திருச்செந்தாழை","/images/thumb/1/1e/பா.திருச்செந்தாழை.jpg/300px-பா.திருச்செந்தாழை.jpg"),
}
def page(t): return B+"/wiki/"+urllib.parse.quote(t.replace(" ","_"))
def img(p): return B+urllib.parse.quote(p)

# ---- 1) Writer links + mini avatars in the Reading Archive (via generator) ----
g='../make_readings_v2.py'; s=open(g,encoding='utf-8').read()
if 'WIKIW' not in s:
    import json
    s=s.replace("def writers(vids):","WIKIW="+json.dumps({k:[page(v[0]),img(v[2]),v[1]] for k,v in W.items()},ensure_ascii=False)+"\ndef writers(vids):",1)
    s=s.replace('''        t=TA.get(a,a)
        url=("https://en.wikipedia.org/wiki/"+a.replace(" ","_")) if t==a else "https://tamil.wiki/index.php?search="+urllib.parse.quote(t)
        out.append(f'<a href="{url}" target="_blank" rel="noopener">{t}</a>')''','''        if a in WIKIW:
            url,pic,t=WIKIW[a]
            out.append(f'<a class="w-chip" href="{url}" target="_blank" rel="noopener"><img src="{pic}" alt="" loading="lazy">{t}</a>')
        else:
            out.append(f'<a class="w-chip" href="https://en.wikipedia.org/wiki/{a.replace(" ","_")}" target="_blank" rel="noopener">{a}</a>')''')
    s=s.replace('return " · ".join(out)','return " ".join(out)')
    open(g,'w',encoding='utf-8').write(s)

# ---- 2) Portrait ribbon on every page except Home ----
order=["Puthumaipithan","Na. Pichamurthy","Ku. Pa. Ra","Mouni","La. Sa. Ra","Ku. Alagirisamy","Thi. Janakiraman","Ki. Ra","Sundara Ramaswamy","Ashokamitran","Jayakanthan","Sujatha","Indira Parthasarathy","Krishnan Nambi","Aadhavan","G. Nagarajan","Sa. Kandasamy","Pramil","Jeyamohan","Ma. Navin","Su. Venugopal","Chandra Thangaraj","Sunil Krishnan","Samraj","Senthil Jagannathan","Thiruchendazhai"]
faces="\n".join(f'      <a class="wr-face" href="{page(W[k][0])}" target="_blank" rel="noopener" data-name="{W[k][1]}"><img src="{img(W[k][2])}" alt="{W[k][1]}" loading="lazy"></a>' for k in order)
ribbon=f'''<!-- writers-ribbon:start -->
<aside class="writers-ribbon" aria-label="Writers we have read">
  <div class="wrap">
    <p class="label" lang="ta">நாம் வாசித்த படைப்பாளிகள்</p>
    <p class="wr-sub">Writers we have read together · portraits courtesy of <a href="https://tamil.wiki" target="_blank" rel="noopener">Tamil Wiki</a></p>
    <div class="wr-faces">
{faces}
    </div>
  </div>
</aside>
<!-- writers-ribbon:end -->
'''
n=0
for f in glob.glob('*.html'):
    if f=='index.html': continue
    t=open(f,encoding='utf-8').read()
    if '<!-- writers-ribbon:start -->' in t:
        a=t.index('<!-- writers-ribbon:start -->'); b=t.index('<!-- writers-ribbon:end -->')+len('<!-- writers-ribbon:end -->\n')
        t=t[:a]+t[b:]
    t=t.replace('  <footer class="site-footer">', ribbon+'  <footer class="site-footer">',1); n+=1
    open(f,'w',encoding='utf-8').write(t)

c=open('css/style.css',encoding='utf-8').read()
if '.writers-ribbon' not in c:
    c+='''
/* ===== Writers ribbon (all pages except Home) ===== */
.writers-ribbon { background: var(--band); border-top: 1px solid var(--line); padding: 2.25rem 0 2.5rem; text-align: center; }
.writers-ribbon .label { margin-bottom: .2rem; }
.wr-sub { font: 500 .8rem var(--label); color: var(--muted); margin: 0 0 1.4rem; }
.wr-sub a { color: var(--muted); }
.wr-faces { display: flex; flex-wrap: wrap; justify-content: center; gap: .55rem .35rem; max-width: 60rem; margin: 0 auto; }
.wr-face { position: relative; display: block; width: 3.4rem; height: 3.4rem; border-radius: 50%; box-shadow: 0 0 0 2px var(--paper), 0 0 0 3.5px rgba(201,162,39,.7); transition: transform .25s, box-shadow .25s; }
.wr-face img { width: 100%; height: 100%; border-radius: 50%; object-fit: cover; object-position: center 25%; filter: grayscale(1) sepia(.15) contrast(1.05); transition: filter .3s; background: var(--navy2); }
.wr-face:hover, .wr-face:focus-visible { transform: translateY(-4px) scale(1.12); box-shadow: 0 0 0 2px var(--paper), 0 0 0 4px var(--gold), 0 8px 18px rgba(6,12,38,.25); z-index: 2; }
.wr-face:hover img, .wr-face:focus-visible img { filter: none; }
.wr-face::after { content: attr(data-name); position: absolute; left: 50%; bottom: calc(100% + .6rem); transform: translateX(-50%) translateY(4px); white-space: nowrap; font: 600 .78rem var(--display); color: #f4efe3; background: var(--navy); padding: .3rem .6rem; border-radius: 6px; opacity: 0; pointer-events: none; transition: opacity .2s, transform .2s; }
.wr-face:hover::after, .wr-face:focus-visible::after { opacity: 1; transform: translateX(-50%); }
@media (max-width: 640px) { .wr-face { width: 2.8rem; height: 2.8rem; } }
/* writer chips with mini portraits in the Reading Archive */
.w-chip { display: inline-flex; align-items: center; gap: .4rem; margin: .2rem .5rem .2rem 0; padding: .15rem .65rem .15rem .15rem; border: 1px solid var(--line); border-radius: 999px; background: #fff; text-decoration: none; font: 600 .82rem var(--display); color: var(--accent2); }
.w-chip img { width: 1.6rem; height: 1.6rem; border-radius: 50%; object-fit: cover; object-position: center 25%; filter: grayscale(1); }
.w-chip:hover img { filter: none; }
.r-writers { margin: -.5rem 0 1.25rem !important; }
'''
    open('css/style.css','w',encoding='utf-8').write(c)
print('ribbon pages:',n)

