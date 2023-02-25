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
            Ss = request.POST.get("ssc-school")
            Sy = request.POST.get("ssc-passing-year")
            Sp = request.POST.get("ssc-percentage")
            Hs = request.POST.get("hsc-school")
            Hy = request.POST.get("hsc-passing-year")
            Hp = request.POST.get("hsc-percentage")
            Ds = request.POST.get("diploma-school")
            Dy = request.POST.get("diploma-passing-year")
            Dp = request.POST.get("diploma-percentage")
            
         



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
        "Ds":Ds, "Dy":Dy, "Dp":Dp
    })