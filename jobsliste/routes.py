from jobsliste import app
from flask import render_template, request
from jobsliste.models import Item,Item1
import time
import os
import sqlite3





databasevillach = []
databaseklagenfurt = []
dbvillach = ["StepstonejobsVillach.db", "amsjobVillach.db", "archiviojobsVillach.db","indeedjobsVillach.db","jobVillach.db","karriereVillach.db"]
htmlberuf = ["AllJobsBeruf.html","StepstoneJobsBeruf.html", "AmsListeBeruf.html", "CarinziaJobsBeruf.html","IndeedJobsBeruf.html","JobListeBeruf.html","KarriereJobListeBeruf.html"]
htmlfirma = ["AllJobsFirma.html","StepstoneJobsFirma.html", "AmsListeFirma.html", "CarinziaJobsFirma.html","IndeedJobsFirma.html","JobListeFirma.html","KarriereJobListeFirma.html","StandardJobListeFirma.html"]
linkvillach = ["https://www.stepstone.at/5/ergebnisliste.html?ws=Villach&radius=20&ag=age_7&of=1&action=paging_next", "https://jobs.ams.at/public/emps/jobs?page=1&location=villach&JOB_OFFER_TYPE=SB_WKO&PERIOD=LAST_WEEK&sortField=PERIOD", "https://www.kaerntnerjobs.at/jobs/villach","https://at.indeed.com/Jobs?l=Villach&sort=date&fromage=7","https://www.job.at/ergebnisliste.html?zoomcompanies=&resultsPerPage=100&what=&where=villach","https://www.karriere.at/jobs/villach?radius=20"]
nomevillach = ["Stepstone", "AMS", "kaerntnerjobs.at","Indeed","Job.at","Karriere.at"]
dbklagenfurt = ["StepstonejobsKlagenfurt.db", "amsjobKlagenfurt.db", "archiviojobsKlagenfurt.db","indeedjobsKlagenfurt.db","jobKlagenfurt.db","karriereKlagenfurt.db","standardKlagenfurt.db"]
linkklagenfurt = ["https://www.stepstone.at/5/ergebnisliste.html?ws=Klagenfurt&radius=20&ag=age_7", "https://jobs.ams.at/public/emps/jobs?page=1&location=klagenfurt&JOB_OFFER_TYPE=SB_WKO&PERIOD=LAST_WEEK&sortField=PERIOD", "https://www.kaerntnerjobs.at/jobs/klagenfurt","https://at.indeed.com/Jobs?l=Klagenfurt&sort=date&fromage=7","https://www.job.at/ergebnisliste.html?zoomcompanies=&resultsPerPage=150&what=&where=klagenfurt","https://www.karriere.at/jobs/klagenfurt?radius=20","https://jobs.derstandard.at/jobsuche/"]
nomeklagenfurt = ["Stepstone", "AMS", "kaerntnerjobs.at","Indeed","Job.at","Karriere.at","Standard.at"]
summerow = 0
numerofile = 0
for nomefile in dbvillach:
    print(nomefile)
    numero = 0
    con = sqlite3.connect(nomefile)
    cur = con.cursor()
    for row in cur.execute('SELECT * FROM archiviojobs ORDER BY Firma, Beruf, Ort'):
            numero += 1
    numerofile += 1                                
    summerow = summerow + numero
    databasevillach.append("["+str(numerofile)+"] = " + nomevillach[numerofile-1]+" ["+str(numero)+"]")
    con.commit()
    con.close()
print("################################")
print("################ Archivio Villach:")
print("################################")
print(databasevillach)
summerow = 0
numerofile = 0
for nomefile in dbklagenfurt:
    #print(nomefile)
    numero = 0
    con = sqlite3.connect(nomefile)
    cur = con.cursor()
    for row in cur.execute('SELECT * FROM archiviojobs ORDER BY Firma, Beruf, Ort'):
            numero += 1
    numerofile += 1                                
    summerow = summerow + numero
    databaseklagenfurt.append("["+str(numerofile)+"] = " + nomeklagenfurt[numerofile-1]+" ["+str(numero)+"]")
    con.commit()
    con.close()
print("################################")
print("################ Archivio Klagenfurt:")
print("################################")
print(databaseklagenfurt)
nomefile = "AllJobs.db"
filetime = os.path.getmtime(nomefile)  
filetime = time.ctime(filetime)
filetime = time.strptime(filetime)
filetime = time.strftime("%d.%m.%Y %H:%M", filetime)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', filetime=filetime)


@app.route('/FirmaVillach', methods=['GET', 'POST'])
def firma_page():
    items = Item.query.order_by(Item.firma.asc()).all()
    totalerows = len(items)
    return render_template('Jobliste.html', items=items ,totalerows=totalerows, ordine='Firma', ort='Villach', databasearray=databasevillach, linkvillach=linkvillach, nomevillach=nomevillach, htmlberuf=htmlberuf, htmlfirma=htmlfirma)

@app.route('/BerufVillach', methods=['GET', 'POST'])
def beruf_page():
    items = Item.query.order_by(Item.beruf.asc()).all()
    totalerows = len(items)
    return render_template('Jobliste.html', filetime=filetime, items=items ,totalerows=totalerows, ordine='Beruf', ort='Villach', databasearray=databasevillach, linkvillach=linkvillach, nomevillach=nomevillach, htmlberuf=htmlberuf, htmlfirma=htmlfirma)

@app.route('/FirmaVillach/<beruf>', methods=['GET', 'POST'])
def firma_page_beruf(beruf):
    items = Item.query.filter(Item.beruf.like('%' + beruf + '%'))
    totalerows = beruf
    return render_template('Jobliste.html', items=items ,totalerows=totalerows, ordine='Firma', ort='Villach')

@app.route('/Villach/ricercaberuf', methods=['GET', 'POST'])
def ricerca_page_beruf():
    beruf = request.form['beruf']
    items = Item.query.filter(Item.beruf.like('%' + beruf + '%'))
    totalerows = beruf
    return render_template('Jobliste.html', items=items ,totalerows=totalerows, ordine='Search', ort='Villach',  beruf=beruf)

@app.route('/Villach/ricercafirma', methods=['GET', 'POST'])
def ricerca_page_firma():
    firma = request.form['firma']
    items = Item.query.filter(Item.firma.like('%' + firma + '%'))
    totalerows = firma
    return render_template('Jobliste.html', items=items ,totalerows=totalerows, ordine='Search', ort='Villach',  firma=firma)



@app.route('/BerufVillach/<beruf>', methods=['GET', 'POST'])
def beruf_page_beruf(beruf):
    items = Item.query.filter(Item.beruf.like('%' + beruf + '%'))
    totalerows = beruf
    return render_template('Jobliste.html', items=items ,totalerows=totalerows, ordine='Firma', ort='Villach', beruf=beruf)

@app.route('/FirmaKlagenfurt', methods=['GET', 'POST'])
def firma_page1():
    items1 = Item1.query.order_by(Item1.firma.asc()).all()
    totalerows = len(items1)
    return render_template('Jobliste1.html', items1=items1 ,totalerows=totalerows, ordine='Firma', ort='Klagenfurt', databasearray1=databaseklagenfurt, linkklagenfurt=linkklagenfurt, nomeklagenfurt=nomeklagenfurt, htmlberuf=htmlberuf, htmlfirma=htmlfirma)

@app.route('/FirmaKlagenfurt/<beruf>', methods=['GET', 'POST'])
def firma_page_beruf1(beruf):
    items1 = Item1.query.filter(Item1.beruf.like('%' + beruf + '%'))
    totalerows = beruf
    return render_template('Jobliste1.html', items1=items1 ,totalerows=totalerows, ordine='Firma', ort='Klagenfurt')

@app.route('/BerufKlagenfurt', methods=['GET', 'POST'])
def beruf_page1():
    items1 = Item1.query.order_by(Item1.beruf.asc()).all()
    totalerows = len(items1)
    return render_template('Jobliste1.html', filetime=filetime, filetime=filetime, items1=items1 ,totalerows=totalerows, ordine='Beruf', ort='Klagenfurt', databasearray1=databaseklagenfurt, linkklagenfurt=linkklagenfurt, nomeklagenfurt=nomeklagenfurt, htmlberuf=htmlberuf, htmlfirma=htmlfirma)

@app.route('/BerufKlagenfurt/<beruf>', methods=['GET', 'POST'])
def beruf_page_beruf1(beruf):
    items1 = Item1.query.filter(Item1.beruf.like('%' + beruf + '%'))
    totalerows = beruf
    return render_template('Jobliste1.html', items1=items1 ,totalerows=totalerows, ordine='Firma', ort='Klagenfurt')

@app.route('/Klagenfurt/ricerca', methods=['GET', 'POST'])
def ricerca_page1():
    beruf = request.form['beruf']
    items1 = Item1.query.filter(Item1.beruf.like('%' + beruf + '%'))
    totalerows = beruf
    return render_template('Jobliste1.html', items1=items1 ,totalerows=totalerows, ordine='Search', ort='Klagenfurt', beruf=beruf)

@app.route('/Klagenfurt/ricercaberuf', methods=['GET', 'POST'])
def ricerca_page_beruf1():
    beruf = request.form['beruf']
    items1 = Item1.query.filter(Item1.beruf.like('%' + beruf + '%'))
    totalerows = beruf
    return render_template('Jobliste1.html', items1=items1 ,totalerows=totalerows, ordine='Search', ort='Klagenfurt',  beruf=beruf)

@app.route('/Klagenfurt/ricercafirma', methods=['GET', 'POST'])
def ricerca_page_firma1():
    firma = request.form['firma']
    items1 = Item1.query.filter(Item1.firma.like('%' + firma + '%'))
    totalerows = firma
    return render_template('Jobliste1.html', items1=items1 ,totalerows=totalerows, ordine='Search', ort='Klagenfurt',  firma=firma)


