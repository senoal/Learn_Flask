import pandas as pd
from flask import Flask, render_template, request, redirect
import datetime as dt


def purchased(p):
    p = request.method=='POST'
    if p:
        
        # Definisikan harga setiap item
        tisu_kotak = 40000
        sunligh = 14000
        sabun_tangan = 15000
        superpell = 15000
        sapu_lidi = 25000
        gula_pasir = 17000
        kopi_bubuk = 52000
        teh_kotak = 8000
        plastik_sampah = 15000
        tisu_gulung = 35000
        prostex_wc = 25000
        lap_piring = 10000

        # request input jumlah setiap item
        nmr = request.form['nmr']
        tisuk = request.form['tisuk']
        sunl = request.form['sunl']
        st = request.form['st']
        spl = request.form['spl']
        sapu = request.form['sapu']
        glp = request.form['glp']
        kpb = request.form['kpb']
        tehk = request.form['tehk']
        plss = request.form['plss']
        tsg = request.form['tsg']
        ptw = request.form['ptw']
        lpp = request.form['lpp']
        dll = request.form['dll']


        jml_item = float(tisuk) + float(sunl) + float(st) + float(spl) + float(sapu) + float(glp) + float(kpb) + float(tehk) + float(plss) + float(tsg) + float(ptw) + float(lpp)
        print(jml_item)
        
        # hitung harga total per item
        jml_tk = float(tisuk) * float(tisu_kotak)
        jml_sl = float(sunl) * float(sunligh)
        jml_st = float(st) * float(sabun_tangan)
        jml_spl = float(spl) * float(superpell)
        jml_sapu = float(sapu) * float(sapu_lidi)
        jml_glp = float(glp) * float(gula_pasir)
        jml_kpb = float(kpb) * float(kopi_bubuk)
        jml_tehk = float(tehk) * float(teh_kotak)
        jml_plss = float(plss) * float(plastik_sampah)
        jml_tsg = float(tsg) * float(tisu_gulung)
        jml_ptw = float(ptw) * float(prostex_wc)
        jml_lpp = float(lpp) * float(lap_piring)
        # jml_dll = float(dll)
        # hitung total jumlah harga
        total = float(jml_tk)+float(jml_sl)+float(jml_st)+float(jml_spl)+float(jml_sapu)+float(jml_glp)+float(jml_kpb)+float(jml_tehk)+float(jml_plss)+float(jml_tsg)+float(jml_ptw)+float(jml_lpp)+float(dll)
        
        now = dt.datetime.now()
        showh = now.strftime("%H:%M:%S")
        showt = now.strftime("%Y-%m-%d")
        year = now.strftime("%Y")

        # buat dataframe
        data_content=['LAPORAN', 'GROCERIES', 'Tahun', year,
                'No.', nmr, '  ', '  ',
                '  ', '  ', '  ', '  ',
                'ITEM', 'HARGA', 'JUMLAH', 'TOTAL',
                'Tisu Kotak', tisu_kotak, tisuk, jml_tk,
                'Sunligh', sunligh, sunl, jml_sl,
                'Sabun Tangan', sabun_tangan, st, jml_st,
                'Super Pell', superpell, spl, jml_spl,
                'Sapu Lidi', sapu_lidi, sapu, jml_sapu,
                'Gula Pasir', gula_pasir, glp, jml_glp,
                'Kopi Bubuk', kopi_bubuk, kpb, jml_kpb,
                'Teh Kotak', teh_kotak, tehk, jml_tehk,
                'Plastik Sampah', plastik_sampah, plss, jml_plss,
                'Tissu Gulung', tisu_gulung, tsg, jml_tsg,
                'Prosetex Wc', prostex_wc, ptw, jml_ptw,
                'Lap Piring', lap_piring, lpp, jml_lpp,
                'Biaya Lainnya', '-', '-', dll,
                'Total', '-', jml_item, total,
                '  ', '  ', '  ', '  ',
                'Jumalah', 'Total : ', 'Rp.', total,
                'Pembelanja : ', 'Ibu', 'Tini', '........',
                'Kasir : ', 'Dian F.S', 'Primasanti','........',
                'Depart : ', 'Operational', ' ', ' ',
                'Tercatat : ', showt, showh, ' ']

        data = list(zip(*[iter(data_content)]*4))
        report = pd.DataFrame(data[1:], columns=data[0])
        # report = report.set_index('LAPORAN')
        # print(report)
        # report.to_csv('Purch_report.csv')
        report.set_index('LAPORAN').to_csv('Purch_report.csv')
        print(report)

        return redirect('/showPurch')