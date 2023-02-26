from django.shortcuts import render
from django.http import HttpResponse
from django import forms

class NewCardForm(forms.Form):
    pass

# Create your views here.
def index(request):
    return render(request, "f2p/form.html", {
        "form" : NewCardForm()
    })

def card(request):
    if request.method == "POST":
        form = NewCardForm(request.POST)
        if form.is_valid():
            fname = request.POST.get("fullname").title()
            Rd = request.POST.get("Rd")
            AdYr = request.POST.get("admissionyear")
            Fadd = request.POST.get("address").strip().split(" ")
            Cadd1 = Fadd[:(len(Fadd)//2)]
            Cadd2 = Fadd[(len(Fadd)//2):]
            Sadd = request.POST.get("address2").strip().split(" ")
            Sadd1 = Sadd[:(len(Fadd)//2)]
            Sadd2 = Sadd[(len(Fadd)//2):]
            Pcode = request.POST.get("postalcode")
            Sn = request.POST.get("student-contact-number")
            Pn = request.POST.get("parent-contact-number")
            Eml = request.POST.get("email").strip()
            Dob = request.POST.get("dob")
            Rlgn = request.POST.get("religion").strip().capitalize()
            Cst = request.POST.get("cast").strip().capitalize()
            Cat = request.POST.get("category").strip().capitalize()
            Bgrp = request.POST.get("blood-group").strip().capitalize()
            Bf = request.POST.get("bus-facility").strip().capitalize()
            Hl = request.POST.get("hostel").strip().capitalize()
            Pfname = request.POST.get("father-name").title()
            Pfo = request.POST.get("father-occupation").title()
            Pfn = request.POST.get("father-contact-number").strip()
            Pfl= request.POST.get("father-job-location").strip()
            Pfon = request.POST.get("father-office-contact-number").strip()
            Pmname = request.POST.get("mother-name").title()
            Pmo = request.POST.get("mother-occupation").title()
            Pmn = request.POST.get("mother-contact-number").strip()
            Pml= request.POST.get("mother-job-location").strip()
            Pmon = request.POST.get("mother-office-contact-number").strip()
            Pgname = request.POST.get("lg-name").title()
            Pgn = request.POST.get("lg-contact-number").strip()
            Pgl= request.POST.get("lg-location").strip()
            Ss = request.POST.get("ssc-school").strip()
            Sy = request.POST.get("ssc-passing-year").strip()
            Sp = request.POST.get("ssc-percentage").strip()
            Hs = request.POST.get("hsc-school").strip()
            Hy = request.POST.get("hsc-passing-year").strip()
            Hp = request.POST.get("hsc-percentage").strip()
            Ds = request.POST.get("diploma-school").strip()
            Dy = request.POST.get("diploma-passing-year").strip()
            Dp = request.POST.get("diploma-percentage").strip()

            fsm1 = request.POST.get("fy-sem1-total-marks")
            fsp1 = request.POST.get("fy-sem1-percentage")
            fsb1 = request.POST.get("fy-sem1-backlog")
            fsr1 = request.POST.get("fy-sem1-remark")
            fsm2 = request.POST.get("fy-sem2-total-marks")
            fsp2 = request.POST.get("fy-sem2-percentage")
            fsb2 = request.POST.get("fy-sem2-backlog")
            fsr2 = request.POST.get("fy-sem2-remark")
            fap = request.POST.get("fy-avg-percentage")
            fr = request.POST.get("fy-remark")
            

            ssm1 = request.POST.get("sy-sem1-total-marks")
            ssp1 = request.POST.get("sy-sem1-percentage")
            ssb1 = request.POST.get("sy-sem1-backlog")
            ssr1 = request.POST.get("sy-sem1-remark")
            ssm2 = request.POST.get("sy-sem2-total-marks")
            ssp2 = request.POST.get("sy-sem2-percentage")
            ssb2 = request.POST.get("sy-sem2-backlog")
            ssr2 = request.POST.get("sy-sem2-remark")
            sap = request.POST.get("sy-avg-percentage")
            sr = request.POST.get("sy-remark")

            tsm1 = request.POST.get("ty-sem1-total-marks")
            tsp1 = request.POST.get("ty-sem1-percentage")
            tsb1 = request.POST.get("ty-sem1-backlog")
            tsr1 = request.POST.get("ty-sem1-remark")
            tsm2 = request.POST.get("ty-sem2-total-marks")
            tsp2 = request.POST.get("ty-sem2-percentage")
            tsb2 = request.POST.get("ty-sem2-backlog")
            tsr2 = request.POST.get("ty-sem2-remark")
            tap = request.POST.get("ty-avg-percentage")
            tr = request.POST.get("ty-remark")

            lsm1 = request.POST.get("ly-sem1-total-marks")
            lsp1 = request.POST.get("ly-sem1-percentage")
            lsb1 = request.POST.get("ly-sem1-backlog")
            lsr1 = request.POST.get("ly-sem1-remark")
            lsm2 = request.POST.get("ly-sem2-total-marks")
            lsp2 = request.POST.get("ly-sem2-percentage")
            lsb2 = request.POST.get("ly-sem2-backlog")
            lsr2 = request.POST.get("ly-sem2-remark")
            lap = request.POST.get("ly-avg-percentage")
            lr = request.POST.get("ly-remark")
            
         



        else:
            return render(request, "f2p/form.html"), {
                "form":form
            }

    return render(request, "f2p/card.html", {
        "fname":fname, "Rd":Rd, "AdYr":AdYr, "Cadd1":Cadd1, "Cadd2":Cadd2,
        "Sadd1":Sadd1, "Sadd2":Sadd2, "Pcode":Pcode, "Sn":Sn, "Pn":Pn,
        "Eml":Eml, "Dob":Dob, "Rlgn":Rlgn, "Cst":Cst, "Cat":Cat, "Bgrp":Bgrp,
        "Bf":Bf, "Hl":Hl, "Pfname":Pfname, "Pfo":Pfo, "Pfn":Pfn, "Pfl":Pfl, "Pfon":Pfon,
        "Pmname":Pmname, "Pmo":Pmo, "Pmn":Pmn, "Pml":Pml, "Pmon":Pmon, "Pgname":Pgname,
        "Pgn":Pgn, "Pgl":Pgl, "Ss":Ss, "Sy":Sy, "Sp":Sp, "Hs":Hs, "Hy":Hy, "Hp":Hp,
        "Ds":Ds, "Dy":Dy, "Dp":Dp, "fsm1":fsm1, "fsp1":fsp1, "fsb1":fsb1, "fsr1":fsr1,
        "fsm2":fsm2, "fsp2":fsp2, "fsb2":fsb2, "fsr2":fsr2, 
        "ssm1":ssm1,"ssp1":ssp1, "ssb1":ssb1, "ssr1":ssr1, "ssm2":ssm2,
        "ssp2":ssp2, "ssb2":ssb2, "ssr2":ssr2, "tsm1":tsm1,"tsp1":tsp1,
        "tsb1":tsb1, "tsr1":tsr1, "tsm2":tsm2, "tsp2":tsp2, "tsb2":tsb2,
        "tsr2":tsr2, "lsm1":lsm1,"lsp1":lsp1,
        "lsb1":lsb1, "lsr1":lsr1, "lsm2":lsm2, "lsp2":lsp2, "lsb2":lsb2,
        "lsr2":lsr2, "fap":fap, "fr":fr, "sap":sap, "sr":sr,
        "tap":tap, "tr":tr, "lap":lap, "lr":lr

    })